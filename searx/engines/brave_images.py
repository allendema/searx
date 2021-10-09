# SPDX-License-Identifier: AGPL-3.0-or-later
"""
Brave Search (Images) : Images from Brave
"""

from json import loads
from urllib.parse import urlencode
from searx import settings

about = {
    "website": 'https://search.brave.com',
    "wikidata_id": 'Q22906900',
    "use_official_api": True,
    "require_api_key": False,
    "results": 'JSON',
}

safesearch_table = {
    0: 'safesearch=off',
    1: 'safesearch=moderate',
    2: 'safesearch=strict'
}

categories = ['images']
paging = False


base_url = 'https://search.brave.com'
search_string = '/api/images?q={query}'

# Do a request
def request(query, params):
    params['url'] = base_url +\
        search_string.format(query=urlencode(
                             {'q': query}))

    # Set the header "cookie", a str
    # based on safesearch_table
    # Lang could be something like this:
    # "Cookie": country=ar; safesearch=strict
    params['headers'].update({
       "Cookie": safesearch_table[params['safesearch']],
})

    return params



def response(resp):
    results = []

    json_data = loads(resp.text)
    # Look for JSON key-values and append to results
    for result in json_data['results']:

        results.append({
            'template': 'images.html',
            'url': result['url'],
            'source': result['source'],
            'title': result['title'],
            'img_src': result['properties']['url'],
            'thumbnail_src': result['properties']['resized'],
            'img_format': result['properties']['format']
        })

    return results
