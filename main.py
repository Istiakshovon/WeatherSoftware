from tkinter import *
import requests
import json

root = Tk()
root.title("Weather App")
# root.geometry("400x400")

# https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode=20002&date=2020-12-20T00-0000&distance=25&API_KEY=9DB00556-9736-433C-A4A0-984B80205E1C


try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode=90210&date=2020-12-20T00-0000&distance=25&API_KEY=9DB00556-9736-433C-A4A0-984B80205E1C")

    api = json.loads(api_request.content)

    category = api[0]['Category']['Name']

    if category =="Good":
        weather_color = "green"
    elif category == "Moderate":
        weather_color = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#FF9900"
    elif category == "Unhealthy":
        weather_color = "#FF0000"
    elif category == "Very Unhealthy":
        weather_color = "#990066"
    elif category == "Hazardous":
        weather_color = "#660000"

    root.configure(bg=weather_color)
except Exception as e:
    api = "Error..."

dateObserved = Label(root, text=api[0]['DateObserved'])
dateObserved.grid(row=1, column=0)

hourObserved = Label(root, text=api[0]['HourObserved'])
hourObservdateObserved = Label(root, text=api[0]['DateObserved'])
dateObserved.grid(row=1, column=0)

hourObserved = Label(root, text=api[0]['HourObserved'])
hourObserved.grid(row=2, column=0)

localTimeZone = Label(root, text=api[0]['LocalTimeZone'])
localTimeZone.grid(row=3, column=0)

reportingArea = Label(root, text=api[0]['ReportingArea'])
reportingArea.grid(row=4, column=0)

stateCode = Label(root, text=api[0]['StateCode'])
stateCode.grid(row=5, column=0)

latitude = Label(root, text=api[0]['Latitude'])
latitude.grid(row=6, column=0)

longitude = Label(root, text=api[0]['Longitude'])
longitude.grid(row=7, column=0)

parameterName = Label(root, text=api[0]['ParameterName'])
parameterName.grid(row=8, column=0)

AQI = Label(root, text=api[0]['AQI'])
AQI.grid(row=9, column=0)

category = Label(root, text=api[0]['Category'])
category.grid(row=10, column=0)

localTimeZone = Label(root, text=api[0]['LocalTimeZone'])
localTimeZone.grid(row=3, column=0)

reportingArea = Label(root, text=api[0]['ReportingArea'])
reportingArea.grid(row=4, column=0)

stateCode = Label(root, text=api[0]['StateCode'])
stateCode.grid(row=5, column=0)

latitude = Label(root, text=api[0]['Latitude'])
latitude.grid(row=6, column=0)

longitude = Label(root, text=api[0]['Longitude'])
longitude.grid(row=7, column=0)

parameterName = Label(root, text=api[0]['ParameterName'])
parameterName.grid(row=8, column=0)

AQI = Label(root, text=api[0]['AQI'])
AQI.grid(row=9, column=0)

category = Label(root, text=api[0]['Category']['Name'])
category.grid(row=10, column=0)




root.mainloop()