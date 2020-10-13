# Weather Application

A simple and easy application to know the weather details of any location.

# Description

This simple GUI application fetches the weather data from (https://openweathermap.org/) based on the zip code and country code entered by the user.

# Requirements

Run the following command in your terminal to download all the dependencies.

```
pip install requirements.txt
```

Adapt the command according to your operating system.

# Getting your own API Key
- Head on to (https://home.openweathermap.org/users/sign_up) and create an account.
- After logging in, move to (https://home.openweathermap.org/api_keys)
- Use the existing API key or generate one for the purpose and copy it.
- Open the `weatherApp.py` file and paste the API key as shown below
```py
api_key = "ce7129a1xxxxxxxxxxxxxxxxxxxxxxxx"
```

# Usage

Run the following command in the `WeatherApp-PythonGUI` folder to start the application.
```
python3 weatherApp.py
```

The following window appears on your screen.
![weatherApp](https://files.catbox.moe/ohvfy4.JPG)

Enter the zip code and country code of the location for which you would like to know the weather in the application.
