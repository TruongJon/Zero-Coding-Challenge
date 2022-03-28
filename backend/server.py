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
    # Extracts fields from JSON object received from frontend
    data = request.json
    name = data.get("name")
    zip = data.get("zip")  
    tokens = name.split(" ")

    # API calls to ZIP API US, refer to https://zipapi.us/docs/
    # Requests are in the form of HTTP Basic Auth and two requests are made,
    # one to get the county and the other to get population by zip code
    countyReq = pip._vendor.requests.get("https://service.zipapi.us/zipcode/county/{}?X-API-KEY={}"
    .format(zip, key), auth=HTTPBasicAuth(email, password))
    countyjson = json.loads(countyReq.text)
    county = countyjson.get("data").get("county")[0]

    populationReq = pip._vendor.requests.get("https://service.zipapi.us/population/zipcode/{}?X-API-KEY={}&fields=male_population,female_population"
    .format(zip, key), auth=HTTPBasicAuth(email, password))
    populationjson = json.loads(populationReq.text)
    population = populationjson.get("data").get("population")

    # Display "PigLatin(name)'s, (zip code) is in X county and has a population of Y."
    phrase = (pl.pigLatin(tokens[0]) + " " + pl.pigLatin(tokens[1]) + 
    "'s zip code {} is in {} County and has a population of {}".format(zip, county, population))
    return {
        "output": phrase
    }

if __name__ == "__main__":
    app.run(debug=True)