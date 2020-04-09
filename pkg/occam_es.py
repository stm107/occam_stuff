from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json


class Occam_es:
    def __init__(self, host='http://localhost', port=9200):
        self.es = Elasticsearch(HOST=host, PORT=port)
        return

    #  very basic attampt at providing elastic search functionality for Occam

    def bulk_add(self, occam_data):
        # adds a bunch'o items to the search index
        # this is for starting a new occam server and adding an existing database of objects
        actions =[]
        with open(occam_data) as json_file:
            data = json.load(json_file)
            i = 1
            for line in data:
                entry = {
                ########### x's are place holders!! TODO
                    '_index': 'occam_index',
                    '_type': 'occam_obj',
                    '_id': i,
                    'title': x,
                    '_source': line,
                }
                actions.append(entry)
                # es.index(index="games", doc_type="game_info", id=index_val, body=data[line])
                i += 1
            helpers.bulk(self.es, actions)

    def add_new_obj(self, parameter_list):
        # adds a single new object to an existing index
        pass

    def occam_search(self, parameter_list):
        pass
    
    def clear_index(self, index_name):
        self.es.indices.delete(index=index_name)
        return self.es.idices.exists(index=index_name)
        # return true if index is empty 