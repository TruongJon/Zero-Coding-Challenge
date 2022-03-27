import time
from flask import Flask

app = Flask(__name__)

# CreatePhrase route
@app.route("/create_phrase", methods=['GET'])
def create_phrase():
    return {
        "phrase": 'Ohnjay ithsmay’s zip code is in Middlesex County and has a population of 36,614'
    }

if __name__ == "__main__":
    app.run(debug=True)