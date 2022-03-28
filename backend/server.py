from re import X
import pigLatin as pl
from flask import Flask, request, jsonify

app = Flask(__name__)

# create_phrase API route
@app.route('/create_phrase', methods=['GET', 'POST'])
def create_phrase():
    data = request.json
    name = data.get("name")
    zip = data.get("zip")  
    tokens = name.split(" ")
    county = "x"
    population = "y"
    phrase = (pl.pigLatin(tokens[0]) + " " + pl.pigLatin(tokens[1]) + 
    "'s is in {} and has a population of {}".format(county, population))
    return {
        "output": phrase
    }

if __name__ == "__main__":
    app.run(debug=True)