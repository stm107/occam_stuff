import occam_es
import json

cur_es = occam_es.Occam_es()
cur_es.bulk_add("occam_objects.json")

found = cur_es.occam_search(input("Word? "))


print(found)

cur_es.clear_index('occam_index')