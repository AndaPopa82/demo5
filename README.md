# Weather application

The purpose of this application is to receive up to date the weather conditions to a specific city.

**_Table of content_**

[Usage](#usage)

[Built with](#built-with)

[General description](#general-description)
 * [Widgets](#widgets)

 * [Images](#images)

 * [API link and key](#api-link-and-key)

 * [Data input](#data-input)

[Run](#run)

[Logs](#logs)

[Arhitecture Diagram](#arhitecture-diagram)

[Process Flow Diagram](#process-flow-diagram)

[Thanks](#thanks)


## Usage
A simple way to find out information about the weather conditions. You just have 
to insert the name of the city in the entry field and the information will be displayed.

[up](#weather-application)

## Built with
In order to build the application I used the Tkinter GUI.

```
from tkinter import *
from tkinter import messagebox
```

I used the requests module in order to receive "live"
information regarding the meteo conditions.

```
import requests
```
[up](#weather-application)


## General description
### Widgets
I used GUI elements like Labels, Button and Entry in order to create 
the interface of the application.

In the Entry widget is used for inserting the city for which you want to 
receive the data. The information will be displayed after the Search
button is pressed.

[up](#weather-application)

### Images
The application has its one logo on the left top corner 
![text](C:\\Users\Ysa\PycharmProjects\first\icons_vreme\logo_api.ico).

The rest of the images used for this application 
(some small picture are displayed on the interface) are stored in the 
folder ```icons_vreme```.

[up](#weather-application)


### API link and key

The site which I receive the data from (json format) is:
https://openweathermap.org/

The API link that I used for the request is
```https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}```.

The ```{city}``` is the input received from the user (from keyboard).

The ```{key}``` is generated after an account is created on the weather site. 
I saved the key in a different file and is imported in the main file using:

```from api_key import key```

[up](#weather-application)


### Data input
The information (json format) received from the site is a dictionary/list 
format, and the data is displayed on interface using key:value format for 
dictionary, and index for list.

Example of data received:

```
{"coord": {"lon": 10.99, 
           "lat": 44.34}, 
 "weather": [{"id": 501, 
              "main": "Rain", 
              "description": "moderate rain", 
              "icon": "10d"}],
 "base": "stations",
 "main": {"temp": 298.48,
          "feels_like": 298.74,
          "temp_min": 297.56,
          "temp_max": 300.05,
          "pressure": 1015,
          "humidity": 64,
          "sea_level": 1015,
          "grnd_level": 933},
 "visibility": 10000,
 "wind": {"speed": 0.62,
          "deg": 349,
          "gust": 1.18},
 "rain": {"1h": 3.16},
 "clouds":  "all": 100},
 "dt": 1661870592,
 "sys": {"type": 2,
         "id": 2075663,
         "country": "IT",
         "sunrise": 1661834187,
         "sunset": 1661882248},
 "timezone": 7200,
 "id": 3163858,
 "name": "Zocca",
 "cod": 200}
 ```
[up](#weather-application)

## Run
In order to run the application, the following command should be 
inserted in Terminal:

```
poetry install
poetry run python weather.py
```

[up](#weather-application)

## Logs
In order to create a log file, I used the logging module.

```
import logging
```
A file is created when request is made: 
```C:\Users\Ysa\PycharmProjects\first\logs.log```

I inserted logs regarding the missing/wrong city entry and 
a log for technical problems (no internet, no API available).

Example:
```
2023-11-06 18:29:10,875 - INFO - The request for data was made and successfully received!
2023-11-06 18:32:48,440 - WARNING - A wrong city name was provided!
2023-11-06 18:33:58,765 - WARNING - No city name was provided!
2023-11-06 18:34:29,685 - ERROR - There are some technical problems, please check!
```

[up](#weather-application)

## Arhitecture Diagram
![text](C:\Users\Ysa\PycharmProjects\first\icons_vreme\arhitecture.png)

[up](#weather-application)

## Process Flow Diagram
![text](C:\Users\Ysa\PycharmProjects\first\icons_vreme\flow_diagram.svg)

[up](#weather-application)

## Thanks
Many thanks to Filip for his support during this course!
![text](C:\Users\Ysa\PycharmProjects\first\icons_vreme\face.png)


[up](#weather-application)

