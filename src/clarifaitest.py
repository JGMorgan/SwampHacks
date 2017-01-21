from clarifai import rest
#from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp

with open('../env/api_keys.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]
app = ClarifaiApp(content[0], content[1])


# create the model walking signal
links = ["https://driversed.com/images/v2008coursecontent/walking.jpg","http://il3.picdn.net/shutterstock/videos/2273915/thumb/1.jpg","http://www.parking.uci.edu/services/traffic/images/traffic-signals-signage/Pedestrian-Timing/walk.jpg"]
for link in links:
    app.inputs.create_image_from_url(url=link, concepts=['walk signal'])
    train = app.models.create('crossing', concepts=['walk signal'])
    print train
    train = app.models.get('{model_id}')
    train.train()

# get the general model
#model = app.models.get("{model_id}")

# predict with the model
model = app.models.get('{model_id}')


import json
links = ['http://nacto.org/wp-content/themes/sink_nacto/views/design-guides/retrofit/urban-street-design-guide/images/conventional-crosswalks/carousel//crystalcity_nn.jpg','http://quincyquarry.com/wp-content/uploads/2015/06/traffic-pedestrian-crosswalk-light-replaced.jpg','http://www.driverknowledgetests.com/resources/wp-content/uploads/2014/05/pedestrian-crossing.jpg','http://grahamprojects.com/wp-content/uploads/2013/12/1312-Hopscotch-Crosswalk-Colossus-shoeprints-action.jpg','http://www.parking.uci.edu/services/traffic/images/traffic-signals-signage/Pedestrian-Timing/walk.jpg','https://driversed.com/images/v2008coursecontent/walking.jpg']

for link in links:
    print links[links.index(link)]
    image = ClImage(url=link)
    print model.predict([image])
    #data = json.dumps(model.predict_by_url(url=link)['outputs'])
    #outputs = json.loads(data)[0]['data']['concepts']
    #for element in outputs:
    #    print element
