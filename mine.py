# mine.py
A code that helps you understand the weather in your city
import requests

from flask import Flask, render_template, request
from nltk.sem.chat80 import city
from torch._inductor.triton_heuristics import foreach

app = Flask(__name__)
api_key='your aoi key is here'
api._route('/',methode['get'],[post])
def index():
    if request.method == 'post':
        city = request.form["city"]
        weather.data=get_weather_data(city)
        return render_template('index.html',weather_data=weather_data)
    return render_template('index.html')
def get_weather_data(city):
    url=f"https://www.irimo.ir/far/index.php"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response=requests.get(url,params=params)
    data=response.json() 
    if data['cod']=='200':
        weather_data={
            'city':data['city']['country'],
             "forecast": []
        }      
        for forecast in data["list"]:

            weather_data["forecast"].append({

                "date": forecast["dt_txt"],

                "temperature": forecast["main"]["temp"],

                "description": forecast["weather"][0]["description"],

                "icon": forecast["weather"][0]["icon"]

            })

        return weather_data

    return None

if __name__ == "__main__":

    app.run(debug=True) 

        
