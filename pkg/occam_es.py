from elasticsearch import Elasticsearch
from elasticsearch import helpers
import elasticsearch_dsl
import json


class Occam_es:
    def __init__(self, host='http://localhost', port=9200):
        self.es = Elasticsearch(HOST=host, PORT=port)
        # print(type(self.es))
        
    #  very basic attampt at providing elastic search functionality for Occam

    def bulk_add(self, occam_data):
        # adds a bunch'o items to the search index
        # this is for starting a new occam server and adding an existing database of objects
        # cleaning/prepping the data really should be a helper finction
            # thought, maybe use requests to hit all of the existing occam objects??
            # 
        actions =[]
        with open(occam_data) as json_file:
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
                actions.append(entry)
                # es.index(index="games", doc_type="game_info", id=index_val, body=data[line])
            helpers.bulk(self.es, actions)

    def add_new_obj(self, new_obj, index_name='occam_index'):
        # adds a single new object
        ##### update for occam objs
        self.es.index(index=index_name, body=new_obj)
       

    def occam_search(self, search_input, index_name='occam_index'):
        # not done just matches orgional test functionality (probably)
        # res = self.es.search(index=index_name, body={"from":0,"size":10,"query":{"match":{"description":search_input}}})
        res = elasticsearch_dsl.Search(using=self.es, index=index_name)
        print('<for debug/dev> number of objects in index ' + str(res.count()))
        q = elasticsearch_dsl.Q('multi_match', query=search_input, fields=['name', 'summary', 'environment'])
        ans = res.query(q)
        answer = ans.execute()
        # print(answer)
        return answer

    def clear_index(self, index_name='occam_index'):
        self.es.indices.delete(index=index_name)
        ##returns true to confirm index is deleted
        return not self.es.indices.exists(index=index_name)