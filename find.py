import sys
import json
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

for k in data:
    to_print = 1
    curr_data = data[k]
    name = curr_data.get('name', ['none'])[0]
    title = curr_data.get('title',['none'])[0]
    genre = curr_data.get('genre',['none'])
    style = curr_data.get('style',['none'])

    if style[0] == 'none':
        continue

    output = "%s: %s:\n" % (name.encode('ascii','ignore'), title.encode('ascii','ignore'))
    output += "    %s\n" % ', '.join(genre).encode('ascii','ignore')
    for s in search:
        if s not in [x.lower() for x in style]:
            to_print = 0
    output += "    %s\n" % ', '.join(style).encode('ascii','ignore')

    if to_print:
        print output
