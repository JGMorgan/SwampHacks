from clarifai import rest
from clarifai.rest import ClarifaiApp

with open('../env/api_keys.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]
app = ClarifaiApp(content[0], content[1])

# get the general model
model = app.models.get("general-v1.3")

# predict with the model
print model.predict_by_url(url='http://www.aronfelddev.com/wp-fla/files/2013/06/women-crossing-the-street.jpg')
