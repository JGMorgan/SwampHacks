from clarifai import rest
#from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp
from flask import Flask
from flask import request
import json
import base64
# parser

#link = 'http://www.parking.uci.edu/services/traffic/images/traffic-signals-signage/Pedestrian-Timing/walk.jpg'
app = Flask(__name__)

threshold = .85
hm = {}

@app.route("/", methods = ['POST'])
def recv_base64():
    print request.data
    print json.loads(request.data)['Image']
    with open('../env/api_keys.txt') as f:
        content = f.readlines()

    with open("./img.jpg", "wb") as fh:
        fh.write(base64.decodestring(json.loads(request.data)['Image']))


    content = [x.strip() for x in content]
    clarifai = ClarifaiApp(content[0], content[1])
    # get the general model
    model = clarifai.models.get("general-v1.3")
    image = ClImage(file_obj=open('./img.jpg', 'rb'))
    # predict with the model
    prediction = model.predict([image])
    print prediction
    data = json.loads(json.dumps(prediction['outputs']))['data']['concepts']
    for element in data:
        hm[element['name']] = element['value']

    if (canCross(hm)):
        return 'True'
    return 'False'


def canCross(hm):
    if (isCrosswalk(hm) and isWhiteMan(hm) and not(isRedHand(hm) or isDontWalk(hm))):
        return True
    else:
        return False

def isCrosswalk(hm):
    crosswalk = hm.get('cross walk')
    if (crosswalk != "None"):
        if (crosswalk >= threshold):
            return True
    return False

def isWhiteMan(hm):
    whiteMan = hm.get('walk signal')
    if (whiteMan != "None"):
        if (whiteMan >= threshold):
            return True
    return False

def isRedHand(hm):
    redHand = hm.get('red hand')
    if (redHand != "None"):
        if (redHand >= threshold):
            return True
    return False

def isDontWalk(hm):
    dontWalk = hm.get('dont walk')
    if (dontWalk != "None"):
        if (dontWalk >= threshold):
            return True
    return False

if __name__ == "__main__":
    app.run(host='0.0.0.0')
