🌦 Weather App Using API

📌 Objective

Build a Python program that shows the current weather using the OpenWeatherMap API.

This project demonstrates how to work with public APIs, fetch real-time weather data, and display it in a readable format using Python.

🛠 Tools & Technologies

Python 3.x

Requests Library (pip install requests)

OpenWeatherMap API (Get your free API key here )

🚀 Features

Fetches real-time weather data by city name

Displays:

🌡 Temperature (°C)

💧 Humidity (%)

☁️ Weather condition (e.g., Clear, Rain, Clouds)

Handles errors if the city is not found

📂 Project Structure WeatherApp/ │-- weather.py # Main Python script │-- README.md # Documentation

⚡ Installation & Setup

Install dependencies:

pip install requests

Get your API Key from OpenWeatherMap .

Update your API Key inside weather.py:

API_KEY = "your_api_key_here"

▶️ Usage

Run the program:

python weather.py

Example interaction:

Enter city name: delhi

Weather in Delhi: Temperature: 31.12°C Humidity: 76% Condition: Moderate rain

✅ Outcome

Learned how to use APIs in Python

Practiced JSON data handling with response.json()

Built a real-time Python app that interacts with the internet
