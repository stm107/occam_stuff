import occam_es

cur_es = occam_es.Occam_es()
cur_es.bulk_add("tester7.json")

found = cur_es.occam_search(input("Word? (only searching title currently) "))
print(found)
cur_es.clear_index('occam_index')