from clarifai import rest
#from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp

with open('../env/api_keys.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]
app = ClarifaiApp(content[0], content[1])

# get the general model
#model = app.models.get("{model_id}")

# predict with the model
model = app.models.get('general-v1.3')

import json
link = 'http://nacto.org/wp-content/themes/sink_nacto/views/design-guides/retrofit/urban-street-design-guide/images/conventional-crosswalks/carousel//crystalcity_nn.jpg'

print link
data = json.dumps(model.predict_by_url(url=link)['outputs'])
outputs = json.loads(data)[0]['data']['concepts']
for element in outputs:
    print element
