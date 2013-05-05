#!/usr/bin/env python2

import dumptruck
import json
from urllib2 import urlopen, quote

dt = dumptruck.DumpTruck(dbname = 'tcamp13.db')

def search(queries = [], results_per_page = '100', language = 'en', num_pages = 15 ):
    '''
    Get results from the Twitter API! Change QUERY to your search term of choice.
    Example queries: 'newsnight', '#newsnight', 'from:bbcnewsnight', 'to:bbcnewsnight'
    '''
    for query in queries:
        for page in range(1, num_pages + 1):
            base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
                 % (quote(query), results_per_page, language, page)
            try:
                results_json = json.load(urlopen(base_url))
                for result in results_json['results']:
                    data = {}
                    data['id'] = result['id']
                    data['text'] = result['text']
                    data['from_user'] = result['from_user']
                    print data['from_user'], data['text']
                    dt.insert(data, 'tweet')
            except:
                print 'Oh dear, failed to scrape %s' % base_url
                raise

if __name__ == '__main__':
    search(['#tcamp2013', 'from:TCampDC', '@TCampDC', '#tcamp13'])
