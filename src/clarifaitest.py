from clarifai import rest
#from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp
from flask import Flask
from flask import request

# parser


link = 'http://www.parking.uci.edu/services/traffic/images/traffic-signals-signage/Pedestrian-Timing/walk.jpg'
app = Flask(__name__)

@app.route("/")
def recv_base64():
    print request.data
    with open('../env/api_keys.txt') as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    app = ClarifaiApp(content[0], content[1])
    # get the general model
    model = app.models.get("general-v1.3")

    # predict with the model
    import json
    data = json.loads(json.dumps(model.predict_by_url(url=link)['outputs']))[0]['data']['concepts']
    hm = {}
    for element in data:
        hm[element['name']] = element['value']



def canCross():
    if (isCrosswalk() and isWhiteMan() and not(isRedHand() or isDontWalk())):
        return True
    else:
        return False

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
