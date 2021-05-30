import tkinter as tk
from tkinter import *
import requests
import time


def getWeather(root):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q= " + city + " &appid=17a1bc1a00e0510bfada3baeb2e4dd98"
    json_data = requests.get(api).json()
    climate = json_data['weather'][0]['main']
    climate_des = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    country = json_data['sys']['country']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 19800))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 19800))

    txt1 = climate + "\n" + str(temp) + "°C"
    txt1_5 = climate_des
    txt2 = "Min Temp: " + str(min_temp) + "\nMaximum Temp: " + str(max_temp) + "\nWind Speed: " + str(
        wind_speed) + "\nSunrise: " + str(sunrise) + "\nSunset: " + str(sunset) + "\nPressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\nCountry: " + country + "\n\n"

    label1.config(text=txt1)
    label2.config(text=txt1_5)
    label2.config(text=txt2)


root = tk.Tk()
root.geometry("500x500")
root.title("Weather Api")
root.configure(bg="skyblue")

font1 = ("poopins", 30, "bold")
font2 = ("poopins", 15, "bold")
font3 = ("poopins", 20)

# for input
textfield = tk.Entry(root, justify='center', width=20, font=font1)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

# show information text
label1 = tk.Label(root, font=font1, bg="skyblue", fg="white")
label1.pack()
label2 = tk.Label(root, font=font3, bg="skyblue", fg="white")
label2.pack()
label3 = tk.Label(root, font=font2, bg="skyblue", fg="white")
label3.pack()

root.mainloop()


