from clarifai import rest
#from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp
from flask import Flask
from flask import request

# parser

with open('../env/api_keys.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]
app = ClarifaiApp(content[0], content[1])

threshold = .85

# get the general model
model = app.models.get("general-v1.3")

link = 'http://www.parking.uci.edu/services/traffic/images/traffic-signals-signage/Pedestrian-Timing/walk.jpg'

# predict with the model
import json
data = json.loads(json.dumps(model.predict_by_url(url=link)['outputs']))[0]['data']['concepts']
hm = {}
for element in data:
    hm[element['name']] = element['value']

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

def canCross():
    if (isCrosswalk() and isWhiteMan() and not(isRedHand() or isDontWalk())):
        return True
    else:
        return False

def isCrosswalk():
    crosswalk = hm.get('cross walk')
    if (crosswalk != "None"):
        if (crosswalk >= threshold):
            return True
    return False

def isWhiteMan():
    whiteMan = hm.get('walk signal')
    if (whiteMan != "None"):
        if (whiteMan >= threshold):
            return True
    return False

def isRedHand():
    redHand = hm.get('red hand')
    if (redHand != "None"):
        if (redHand >= threshold):
            return True
    return False

def isDontWalk():
    dontWalk = hm.get('dont walk')
    if (dontWalk != "None"):
        if (dontWalk >= threshold):
            return True
    return False

if __name__ == "__main__":
    app.run()
