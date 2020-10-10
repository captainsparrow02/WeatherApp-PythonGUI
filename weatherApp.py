#!/usr/bin/env python3

from tkinter import *
import json
import requests

root = Tk()
root.title("My Weather App")
root.geometry("270x100")

api_key = ''

def close():
    newRoot.destroy()
    root.destroy()

def update():
    global newRoot
    zip = str(zipcode.get())
    country = str(countrycode.get())
    try:
        api_data = requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+zip+","+country+"&units=metric&appid="+api_key)
        data = json.loads(api_data.content)
        # print(data)

    except Exception as e:
        print('Error')

    newRoot = Tk()
    newRoot.title("Weather Updates")
    newRoot.geometry("220x200")

    location = Label(newRoot, text = "Location: "+data['name'], padx=10, pady=5)
    location.grid(row=0, column=0)

    currTemp = Label(newRoot, text="Current Temperature: " + str(data['main']['temp']), padx=10, pady=5)
    currTemp.grid(row=1, column=0)

    minTemp = Label(newRoot, text="Min. Temperature: " + str(data['main']['temp_min']), padx=10, pady=5)
    minTemp.grid(row=2, column=0)

    maxTemp = Label(newRoot, text="Max. Temperature: " + str(data['main']['temp_max']), padx=10, pady=5)
    maxTemp.grid(row=3, column=0)

    humidity = Label(newRoot, text="Humidity: " + str(data['main']['humidity']), padx=10, pady=5)
    humidity.grid(row=4, column=0)

    quit_btn = Button(newRoot, text="Close App", command=close)
    quit_btn.grid(row=5, column=0)

zipcode_label=Label(root, text="Zipcode")
zipcode_label.grid(row=0, column=0, padx=10, pady=5)

country_label=Label(root, text="Country Code")
country_label.grid(row=1, column=0, padx=10, pady=5)

zipcode = Entry(root, text="zipcode")
zipcode.grid(row=0, column =1 , padx =10 , pady=5, ipadx=5)

countrycode = Entry(root, text="countrycode")
countrycode.grid(row=1, column =1 , padx =10 , pady=5, ipadx=5)

submit_btn = Button(root, text="Get Updates", command=update)
submit_btn.grid(row=2, column =0, columnspan = 2 ,padx=10, pady=5)
root.mainloop()

