# Weather App

A simple desktop weather application built with Python and Tkinter, integrated
with the OpenWeatherMap API. Users can select an Indian state/UT from a
dropdown and view live weather conditions, description, temperature, and
pressure.

## Features
- Real-time weather data using the OpenWeatherMap API
- Simple, clean Tkinter GUI
- Dropdown selection of Indian states and union territories
- Displays weather condition, description, temperature (°C), and pressure

## Tech Stack
- Python
- Tkinter (GUI)
- Requests (API calls)
- OpenWeatherMap API

## Setup (Run Locally)

1. Clone the repository:
   ```
   git clone https://github.com/kanak826/weather_app.git
   cd weather_app
   ```

2. Install dependencies:
   ```
   pip install requests
   ```

3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
   and set it as an environment variable:

   **Windows (PowerShell):**
   ```
   $env:OPENWEATHER_API_KEY="your_api_key_here"
   ```

   **Windows (Command Prompt):**
   ```
   set OPENWEATHER_API_KEY=your_api_key_here
   ```

   To make this permanent, add `OPENWEATHER_API_KEY` under
   *User variables* in Windows Environment Variables settings.

4. Run the app:
   ```
   python Weatherapp.py
   ```

5. Select a state from the dropdown and click **Done** to view the weather.

## Note
The API key is never hardcoded in the source code — it is read from an
environment variable (`OPENWEATHER_API_KEY`) for security.

## Author
Kanak Baghel — [GitHub](https://github.com/kanak826)
