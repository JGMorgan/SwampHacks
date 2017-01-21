from clarifai import rest
from clarifai.rest import ClarifaiApp

with open('../env/api_keys.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]
app = ClarifaiApp(content[0], content[1])

# get the general model
model = app.models.get("general-v1.3")

# predict with the model
import json
data = json.dumps(model.predict_by_url(url='http://www.parking.uci.edu/services/traffic/images/traffic-signals-signage/Pedestrian-Timing/walk.jpg')['outputs'])
outputs = json.loads(data)[0]['data']['concepts']
for element in outputs:
    print element
