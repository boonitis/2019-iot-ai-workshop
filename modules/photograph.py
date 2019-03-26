import requests
from modules import helpers

def all():
    return requests.get(helpers.api('photograph'))


def find(id):
    return requests.get(helpers.api('photograph/'+id))


def store(data):
    return requests.post(helpers.api('photograph'), files = {
        'image': open(data['image'], 'rb')
    },
    headers= {
        'scarecrow-id': '1',
        'scarecrow-secret': 'Pizza112'
    },
    data = {
        'location': data['location'],
        'latitude': data['latitude'],
        'longitude': data['longitude'],
    })
