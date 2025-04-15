from flask import Flask

app = Flask(__name__)

@app.route('/getWeatherForecast')
def getWeatherOnline():
    return "Today is gonna be a great sunny day"