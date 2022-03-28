import pigLatin as pl
import json
import pip._vendor.requests
from pip._vendor.requests.auth import HTTPBasicAuth
from flask import Flask, request, jsonify

app = Flask(__name__)

# Authentication info for API calls to ZIP API US
email = "truong.jo@northeastern.edu"
password = "zeropassword"
key = "e5b77470f2671c5662e32df58def1a44"

# create_phrase API route
@app.route('/create_phrase', methods=['GET', 'POST'])
def create_phrase():
    data = request.json
    name = data.get("name")
    tokens = name.split(" ")
    zip = data.get("zip")  

    countyReq = pip._vendor.requests.get("https://service.zipapi.us/zipcode/county/{}?X-API-KEY={}"
    .format(zip, key), auth=HTTPBasicAuth(email, password))
    countyjson = json.loads(countyReq.text)
    county = countyjson.get("data").get("county")

    populationReq = pip._vendor.requests.get("https://service.zipapi.us/population/zipcode/{}?X-API-KEY={}&fields=male_population,female_population"
    .format(zip, key), auth=HTTPBasicAuth(email, password))
    populationjson = json.loads(populationReq.text)
    population = population.json.get("data").get("population")

    phrase = (pl.pigLatin(tokens[0]) + " " + pl.pigLatin(tokens[1]) + 
    "'s is in {} and has a population of {}".format(county, population))
    return {
        "output": phrase
    }

if __name__ == "__main__":
    app.run(debug=True)