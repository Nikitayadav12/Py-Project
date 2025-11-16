import requests

API_KEY = "2ee36774cfcd30af230ada02598d5e9c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")


url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    weather = data['weather'][0]
    
    temperature = main['temp']
    humidity = main['humidity']
    description = weather['description']

    print(f"\nWeather in {city.capitalize()}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description.capitalize()}")
else:
    print("City not found or API error.")
