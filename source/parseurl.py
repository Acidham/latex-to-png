#!/usr/bin/python

import sys
import urllib
from urlparse import urlparse

encoded_url = sys.argv[1]
#encoded_url = "https://latex.codecogs.com/png.latex?%5Cfn_jvn%20Dev%20%5C%2C%20Per%20%5C%2C%20Roadmap%20%5Ccdot%20%7BDiff%20%5C%2C%20HC%20%5Cover%20Total%20%5C%2C%20HC%20%5C%2C%20Planned%20%5C%2C%20Work%7D%20%3D%20HC%20%5C%2C%20per%20%5C%2C%20Roadmap"
if encoded_url.startswith("http"):

    decoded_url = urllib.unquote(encoded_url)

    url_items = urlparse(decoded_url)
    url_query = url_items.query
    result = url_query.replace("fn_jvn ", "")
    sys.stdout.write(result[1:])
else:
    sys.stdout.write("ERROR")
