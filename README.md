Some Discogs Code
=================

This is just some code I was playing with to work with the [Discogs](http://discogs.com) freely available [XML database dumps](http://www.discogs.com/data/) -- specifically the "masters" file.

`discogs_parse.py` file will convert the XML file to a JSON file. Edit this file with the path to your downloaded XML file.

`find.py` takes one or more command line arguments. It searches the JSON file for albums with styles matching your arguments:

    $ find.py "modern classical" breakcore
    
    Venetian Snares: Rossz Csillag Alatt Szletett:
        Electronic
        Modern Classical, Breakcore

    Igorrr: Nostril:
        Classical, Electronic
        Modern Classical, Baroque, Breakcore
    
    DJ Scotch Egg: Scotch Hausen:
        Electronic
        Modern Classical, Chiptune, Breakcore
    
    Venetian Snares: My Downfall (Original Soundtrack):
        Classical, Electronic
        Modern Classical, Breakcore
