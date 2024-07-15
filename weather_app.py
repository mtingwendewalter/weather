import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather details
def get_weather(city):
    api_key = 'bd5e378503939ddaee76f12ad7a97608'  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        temperature = main["temp"]
        humidity = main["humidity"]
        wind_speed = wind["speed"]

        return temperature, humidity, wind_speed
    else:
        messagebox.showerror("Error", "City Not Found")
        return None

# Function to display weather
def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        temperature, humidity, wind_speed = weather
        result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")

# Setting up the GUI
app = tk.Tk()
app.title("Weather App")
app.geometry("300x200")

city_label = tk.Label(app, text="Enter City Name:")
city_label.pack(pady=10)

city_entry = tk.Entry(app)
city_entry.pack(pady=5)

get_weather_button = tk.Button(app, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(app, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

app.mainloop()
