#!/usr/bin/env python3

from tkinter import *
import json
import requests

# Creating root window of the app.
root = Tk()
root.title("My Weather App")
root.geometry("270x100")

api_key = '' # Enter your API Key here.

def close():
    '''This function closes both the windows.'''

    newRoot.destroy()
    root.destroy()

def update():
    '''This function fetches the details from the website, creates a new window and displays the fetched weather report in the new window.'''

    global newRoot
    zip = str(zipcode.get()) # Fetching zipcode.
    country = str(countrycode.get()) # Fetching country code.

    # Fetching data using API Key.
    try:
        api_data = requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+zip+","+country+"&units=metric&appid="+api_key)
        data = json.loads(api_data.content)
        # print(data)

    except Exception as e:
        print('Error')

    # Creating a new window to display fetched weather details.
    newRoot = Tk()
    newRoot.title("Weather Updates")
    newRoot.geometry("220x200")

    # Creating Label for each weather data.
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

    # Creating a quit button to exit the application.
    quit_btn = Button(newRoot, text="Close App", command=close)
    quit_btn.grid(row=5, column=0)

# Creating labels.
zipcode_label=Label(root, text="Zipcode")
zipcode_label.grid(row=0, column=0, padx=10, pady=5)

country_label=Label(root, text="Country Code")
country_label.grid(row=1, column=0, padx=10, pady=5)

# Creatinf entry fields.
zipcode = Entry(root, text="zipcode")
zipcode.grid(row=0, column =1 , padx =10 , pady=5, ipadx=5)

countrycode = Entry(root, text="countrycode")
countrycode.grid(row=1, column =1 , padx =10 , pady=5, ipadx=5)

# Creating the submit button.
submit_btn = Button(root, text="Get Updates", command=update)
submit_btn.grid(row=2, column =0, columnspan = 2 ,padx=10, pady=5)

root.mainloop()
