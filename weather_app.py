import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # You need to install pillow library
import requests
from io import BytesIO

def get_weather(city):
    api_key = 'bd5e378503939ddaee76f12ad7a97608'  # Replace with your actual API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    complete_url = f'{base_url}?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(complete_url)
        data = response.json()

        if data['cod'] != '404':
            main = data['main']
            weather = data['weather'][0]
            temp = main['temp']
            pressure = main['pressure']
            humidity = main['humidity']
            weather_desc = weather['description']
            icon_code = weather['icon']
            
            result = {
                "temp": f"Temperature: {temp}°C",
                "pressure": f"Pressure: {pressure} hPa",
                "humidity": f"Humidity: {humidity}%",
                "description": f"Description: {weather_desc.capitalize()}",
                "icon_code": icon_code
            }
        else:
            result = "City Not Found!"
    except Exception as e:
        result = "Error: Could not retrieve data"
    return result

def show_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        if isinstance(weather_info, dict):
            weather_label.config(text=f"{weather_info['temp']}\n{weather_info['pressure']}\n{weather_info['humidity']}\n{weather_info['description']}")
            icon_url = f"http://openweathermap.org/img/wn/{weather_info['icon_code']}@2x.png"
            icon_response = requests.get(icon_url)
            icon_data = Image.open(BytesIO(icon_response.content))
            icon_image = ImageTk.PhotoImage(icon_data)
            icon_label.config(image=icon_image)
            icon_label.image = icon_image  # Keep a reference to avoid garbage collection
        else:
            weather_label.config(text=weather_info)
            icon_label.config(image='')
    else:
        messagebox.showerror("Input Error", "Please enter a city name")

# Creating the main window
root = tk.Tk()
root.title("Tinker Weather App")
root.geometry("400x500")

# Adding the icon
root.iconbitmap('weather_icon.ico')  # Replace with your icon file path

# Adding components
city_label = tk.Label(root, text="Enter City Name:", font=("Helvetica", 14))
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=10)

get_weather_btn = tk.Button(root, text="Get Weather", command=show_weather, font=("Helvetica", 14))
get_weather_btn.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Helvetica", 14), justify=tk.LEFT)
weather_label.pack(pady=10)

icon_label = tk.Label(root)
icon_label.pack(pady=10)

# Running the application
root.mainloop()
