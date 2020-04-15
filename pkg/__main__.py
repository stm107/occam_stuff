import occam_es

cur_es = occam_es.Occam_es()
cur_es.bulk_add("occam_objects.json")

found = cur_es.occam_search(input("Word? "))
# i = 1
for line in found:
    print(line['summary'])
# print(found)
cur_es.clear_index('occam_index')