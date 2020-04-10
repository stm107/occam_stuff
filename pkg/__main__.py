import occam_es

cur_es = occam_es.Occam_es()
cur_es.bulk_add("tester7.json")
cur_es.clear_index('occam_index')