from elasticsearch import Elasticsearch
from elasticsearch import helpers
import elasticsearch_dsl
import json

actions =[]
with open("occam_objects.json") as json_file:
    data = json.load(json_file)
    for line in data:
        entry = {
        ###########TODO acutally fomat for occam
            '_index': 'occam_index',
            # '_type': 'occam_obj',
            'href': line,
            'name': data[line].get('name'),
            'type': data[line].get('type'),
            'architecture': data[line].get('architecture'), 
            'environment': data[line].get('enviorment'),
            'summary': data[line].get('summary'),
        }
        print(entry)
        break
        actions.append(entry)