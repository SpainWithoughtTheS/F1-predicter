import requests
import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt
import warnings
import os
import pickle

# Suppress warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Enable FastF1 plotting without default Matplotlib color modifications
plotting.setup_mpl(color_scheme=None, misc_mpl_mods=False)

# Comprehensive race mapping
RACE_MAP = {
    'australia': 'Australian Grand Prix',
    'bahrain': 'Bahrain Grand Prix',
    'spain': 'Spanish Grand Prix',
    'monaco': 'Monaco Grand Prix',
    'azerbaijan': 'Azerbaijan Grand Prix',
    'canada': 'Canadian Grand Prix',
    'austria': 'Austrian Grand Prix',
    'britain': 'British Grand Prix',
    'hungary': 'Hungarian Grand Prix',
    'belgium': 'Belgian Grand Prix',
    'netherlands': 'Dutch Grand Prix',
    'italy': 'Italian Grand Prix',
    'russia': 'Russian Grand Prix',
    'singapore': 'Singapore Grand Prix',
    'japan': 'Japanese Grand Prix',
    'unitedstates': 'United States Grand Prix',
    'mexico': 'Mexican Grand Prix',
    'brazil': 'Brazilian Grand Prix',
    'abu dhabi': 'Abu Dhabi Grand Prix',
}

# Function to get driver names using Ergast API and cache them
def get_driver_names(year):
    cache_file = f'driver_names_{year}.pkl'
    if os.path.exists(cache_file):
        with open(cache_file, 'rb') as f:
            driver_names = pickle.load(f)
        print(f"Loaded driver names from cache for {year}.")
    else:
        url = f'http://ergast.com/api/f1/{year}/drivers.json'
        response = requests.get(url)
        data = response.json()

        driver_names = {}
        for driver in data['MRData']['DriverTable']['Drivers']:
            driver_names[driver['code']] = driver['familyName'] + ', ' + driver['givenName']

        with open(cache_file, 'wb') as f:
            pickle.dump(driver_names, f)
        print(f"Fetched and cached driver names for {year}.")
    return driver_names

# Function to get the correct race name for input
def get_race_name(race_input):
    return RACE_MAP.get(race_input.lower(), race_input.title())

def get_telemetry():
    # Get user input (case insensitive)
    race = input("Enter the race (e.g., 'Monaco', 'Silverstone', etc.): ").strip().lower()
    year = input("Enter the year: ").strip()

    # Load session based on user input (race and year are case insensitive)
    race = get_race_name(race)  # Map abbreviations to full race names
    try:
        session = fastf1.get_session(int(year), race, 'R')  # 'R' is for race
        session.load()  # Ensure session data is fully loaded
    except Exception as e:
        print(f"Error loading session: {e}")
        return

    # Fetch driver names from Ergast API
    driver_names = get_driver_names(year)
    print(f"Available drivers in {race} {year}:")

    # List available drivers in the session and match their codes with the names
    driver_numbers = {}
    available_drivers = session.drivers
    for i, driver in enumerate(available_drivers):
        driver_name = driver_names.get(driver, driver)  # Use Ergast API for name or fallback to driver number
        driver_numbers[i + 1] = (driver, driver_name)
        print(f"{i + 1}. {driver_name} ({driver})")

    # Let user select a driver by number
    while True:
        try:
            driver_number = int(input("Enter the driver number (e.g., 1 for first driver): ").strip())
            if 1 <= driver_number <= len(available_drivers):
                driver, driver_name = driver_numbers[driver_number]
                break
            else:
                print(f"Invalid number. Please choose between 1 and {len(available_drivers)}.")
        except ValueError:
            print("Invalid input. Please enter a valid driver number.")

    print(f"Selected driver: {driver_name} ({driver})")

    # Check if the session has laps data
    if session.laps is None or session.laps.empty:
        print("No lap data available for this session.")
        return

    # Load laps for the driver
    driver_laps = session.laps.pick_driver(driver)  # Case insensitive driver search
    if driver_laps.empty:
        print(f"No lap data found for {driver_name} in {race} {year}.")
        return

    # Pick the fastest lap
    fastest_lap = driver_laps.pick_fastest()
    telemetry = fastest_lap.get_telemetry()

    # Get weather data if available
    weather = "Data not available"
    if hasattr(session, 'weather') and session.weather is not None:
        weather = session.weather

    # Get the number of pit stops
    pit_stops = 0
    if 'PitStop' in session.laps.columns:
        pit_stops = session.laps[session.laps['PitStop']].shape[0]

    print(f"Weather: {weather}")
    print(f"Number of Pit Stops: {pit_stops}")

    # Plot the telemetry
    fig, ax = plt.subplots()
    sc = ax.scatter(telemetry['X'], telemetry['Y'], c=telemetry['Speed'], cmap='viridis', s=2)
    plt.colorbar(sc, label='Speed [km/h]')
    ax.set_title(f"Telemetry: {driver_name} Fast Lap - {race} {year}")
    plt.axis('equal')
    plt.show()

# Call the function
get_telemetry()
