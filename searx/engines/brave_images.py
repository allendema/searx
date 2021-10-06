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

categories = ['images']
paging = False


base_url = 'https://search.brave.com'
search_string = '/api/images?q={query}'


def request(query, params):

    params['url'] = base_url + search_string

# Set safesearch mode based on user settings.
# Safesearch is set with cookies and not with URL params.

#    if params['safesearch'] == 1:
#        params['cookies'] = {"cookie": "safesearch:moderate"}

#    elif params['safesearch'] == 2:
#        params['cookies'] = {"cookie": "safesearch:strict"}

    return params


def response(resp):
    results = []

    json_data = loads(resp.text)
    for result in json_data['results']:

        results.append({
            'template': 'images.html',
            'url': result['url'],
            'title': result['title'],
            'img_src': result['properties']['url'],
            'thumbnail_src': result['thumbnail']['src']
        })

    return results
