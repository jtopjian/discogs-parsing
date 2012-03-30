#!/usr/bin/env python

import utils
import json
from collections import defaultdict
import time

IN_FILE = 'electro.json'
OUT_FILE = 'new_electro.json'

f = open(IN_FILE)
data = json.load(f)

new_data = defaultdict(dict)

for k in data:
    release_id = data[k][0]
    try:
        (rating, count) = utils.get_rating(release_id)
        new_data[k] = defaultdict(dict)
        new_data[k]['release_id'] = release_id
        new_data[k]['rating'] = rating
        new_data[k]['count'] = count
        print "%s: %s/%s" % (release_id, rating,count)
        time.sleep(1)
    except Exception:
        continue


w = open(OUT_FILE,'w')
json.dump(new_data, w)
