import sys
import json
import utils
search = []

if len(sys.argv) < 2:
    print "Need an argument"
    print "find.py classical idm"
    print "  - will find all albums with styles of both classical and idm music"
    sys.exit(1)
else:
    for x in sys.argv[1:]:
        search.append(x.lower())

f = open('data.json')
data = json.load(f)

results = utils.style_search(data, search)

for r in results:
    curr_data = data[r]
    name = curr_data.get('name', ['none'])[0]
    title = curr_data.get('title',['none'])[0]
    genre = curr_data.get('genre',['none'])
    style = curr_data.get('style',['none'])

    output = "%s: %s:\n" % (name.encode('ascii','ignore'), title.encode('ascii','ignore'))
    output += "    %s\n" % ', '.join(genre).encode('ascii','ignore')
    output += "    %s\n" % ', '.join(style).encode('ascii','ignore')
    print output
