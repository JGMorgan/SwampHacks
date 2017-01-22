from clarifai import rest
#from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

def canCross():
    if (isCrosswalk() && isWhiteMan() && !(isRedHand() || isDontWalk()))
        return true
    else
        return false;

def isCrosswalk():
    return

def isWhiteMan():
    return

def isRedHand():
    return

def isDontWalk():
    return

if __name__ == "__main__":
    app.run()
