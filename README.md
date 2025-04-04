# F1 Telemetry Predictor

This Python project uses the FastF1 library to fetch telemetry data for Formula 1 races, and integrates with the Ergast API to retrieve driver names. The project also includes weather data and pit stop information for a selected race session and driver. The telemetry data is visualized with a scatter plot showing the driver's speed over the circuit layout.

## Features:
- Fetches race data for a specific year and Grand Prix.
- Displays available drivers for a chosen race.
- Retrieves telemetry data for the fastest lap of the selected driver.
- Displays weather information (if available) and pit stops for the session.
- Plots telemetry data using `matplotlib` for visual analysis.

## Requirements:
- Python 3.7+
- `requests` library
- `fastf1` library
- `matplotlib` library
- `pandas` library
- Internet connection to fetch data from the Ergast API and FastF1 API.

## Installation Instructions:

1. **Clone the Repository**:
   To get started, clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/f1-telemetry-predictor.git
   cd f1-telemetry-predictor
   ```

2. **Create a Virtual Environment** (Optional but recommended):
   If you're using Python 3.7+ (recommended), you can create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   On Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install Dependencies**:
   Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should include the following:
   ```
   requests
   fastf1
   matplotlib
   pandas
   ```

## Usage:

1. **Run the Script**:
   After setting up, you can run the script to fetch telemetry data and display it:
   ```bash
   python main.py
   ```

2. **Follow the Prompts**:
   - Enter the **name of the race** (e.g., `Silverstone`, `Monaco`).
   - Enter the **year** of the race (e.g., `2020`, `2021`).
   - Choose a driver by selecting a number corresponding to the available drivers for that session.

3. **View Telemetry and Visuals**:
   - The telemetry of the fastest lap for the selected driver will be plotted.
   - Weather and pit stop information will be displayed in the console.

## Debugging and Troubleshooting:

If you encounter any issues, use the following tips for debugging:

1. **Check for Missing Libraries**:
   If you get an error about missing libraries, make sure all required libraries are installed by running:
   ```bash
   pip install -r requirements.txt
   ```

2. **Ensure Proper Session Loading**:
   If the script fails to load a session, ensure that:
   - The race name and year are correct.
   - The race data is available in the FastF1 library for the specified year and race.
   - The internet connection is active for fetching the data.

3. **Pit Stop and Weather Data Missing**:
   Some races may not have detailed pit stop or weather data. If you encounter a KeyError or missing information, ensure the column or attribute exists by checking the session data structure.

4. **Check Session Availability**:
   If no lap data is available or the script doesn't display any telemetry:
   - Double-check that the driver has participated in the session.
   - Some sessions may not have laps or telemetry data available.

5. **Verbose Debug Output**:
   You can add extra print statements or logs in the code to display detailed information during execution. For example, if you're unsure about the structure of the session's data:
   ```python
   print(session.__dict__)  # This will show the session object structure
   ```

6. **API Rate Limits**:
   If the script encounters API rate limits, wait for a while and try again. Ergast API and FastF1 may have limitations on the number of requests per minute.

## Example Output:
After running the script and selecting a driver, you will see output similar to:

```
Available drivers in British Grand Prix 2020:
1. Hamilton, Lewis (44)
2. Bottas, Valtteri (77)
3. Verstappen, Max (33)
4. Leclerc, Charles (16)
...
Enter the driver number (e.g., 1 for first driver): 1
Selected driver: Hamilton, Lewis (44)
Weather: Cloudy, 22°C
Number of Pit Stops: 2
```

A plot will be displayed showing the telemetry of the fastest lap, with speed variations across the circuit.

## Debug Info:
If you encounter errors or unexpected behavior, the following debug information can be helpful:
- **Error Loading Session**: Ensure the race name and year are correct and that the race session exists in FastF1.
- **No Lap Data Found**: Make sure the race has data available for the selected year.
- **Pit Stop Column Missing**: Not all sessions include pit stop data. You can handle this by checking if the column exists (`'PitStop' in session.laps.columns`).
- **Weather Data Unavailable**: Weather data might not be available for all races. You can check the `session.weather` attribute to ensure it exists.

## Contributing:
Feel free to fork this project and submit pull requests with improvements or bug fixes. If you find any issues or have feature requests, open an issue in the GitHub repository.

---

