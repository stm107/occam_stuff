import occam_es
import json

cur_es = occam_es.Occam_es()
cur_es.bulk_add("occam_objects.json")
word=input("Word? ")
found = cur_es.occam_search(word)
print(found)
# for line in found:
#     print(line)
print(cur_es.clear_index('occam_index'))
