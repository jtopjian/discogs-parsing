How to Find the "Best Of" a style on Discogs
============================================

* Convert the masters XML file into JSON
* Create a dictionary of master_id: release_id values of the style(s) you want:

<pre><code>
    import json
    f = open('data.json')
    data = json.load(f)
    search = ['electro', 'synth-pop']
    id = {}
    for k in data:
        found = 1
        curr_data = data[k]
        style = curr_data.get('style',['none'])
        if style[0] == 'none':
            continue
        for s in search:
            if s not in [x.lower() for x in style]:
                found = 0
        if found:
            id[k] = curr_data.get('main_release')
    w = open('subdata.json')
    json.dump(id, w)
</code></pre>

* Use `scrape.py` (edit the `IN_FILE` and `OUT_FILE` variables) to scrape discogs.com and get the rating and number of votes for each release.

* Parse the resulting data:

<pre><code>
    import json
    import copy
    f = open(OUT_FILE)
    data = json.load(f)
    f2 = open('data.json')
    full_data = json.load(f)
    # Limit results to releases with 10 or more votes
    data2 = copy.deepcopy(data)
    for k in data:
        if int(data[k]['count']) &lt; 10:
            del(data2[k])
    x = sorted(data2.iteritems(), key=lambda (k,v): (v['rating'], k))
    x.reverse()
    out = ""
    for i in x:
        master_id = i[0]
        curr_data = full_data[master_id]
        out = out + "%s: %s = > %s\n" % (curr_data['name'][0], curr_data['title'][0], i[1]['rating'])
    f3 = open('out.txt','w')
    f3.write(out.encode('ascii','ignore'))
    f3.close()
</code></pre>

* `out.txt` will now have a sorted list of the best voted albums of a particular style.
