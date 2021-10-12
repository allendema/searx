# SPDX-License-Identifier: AGPL-3.0-or-later
"""
Weather (DuckDuckGo)


There are less complicated providers but giving ddg spices a go
"""

import json
from urllib.parse import urlencode

# about
about = {
    "website": 'https://duckduckgo.com/',
    "wikidata_id": 'Q12805',
    "official_api_documentation": '',
    "use_official_api": True,
    "require_api_key": False,
    "results": 'JSONP',
}

search_url = 'https://duckduckgo.com/js/spice/forecast/{query}'
weight = 100

https_support = True


def request(query, params):
    params['url'] = search_url.format(
        query=urlencode({'q': query}))
 #   print(params)
    return params


def response(resp):
    """remove first and last lines to get only json"""
    json_resp = resp.text[resp.text.find('\n') + 1:resp.text.rfind('\n') - 2]

    results = []

    now = json.loads(json_resp)['currently']

    # TODO: Dynamically add icon to infobox
    if now['summary'].rfind('Clear') == -1:
        url = 'http://openweathermap.org/img/wn/01d@2x.png'
    elif now['summary'].rfind('rain') == -1:
        url = 'http://openweathermap.org/img/wn/10d@2x.png'
    elif now['summary'].rfind('snow') == -1:
        url = 'http://openweathermap.org/img/wn/13d@2x.png'
    else:
        url = 'http://openweathermap.org/img/wn/01d@2x.png'

    # convert Weather temperature in celsius
    weather_temp = (now['temperature'] - 32) / 1.8

    # round the temp, i.e 12.227777777777776 to 12
    weather_temp = round(weather_temp)

    #print(now)
    summary = 'The weather summary: {0}'.format(
        now['summary'])

    weather_string = 'Temperature: {0} Celsius'.format(
        weather_temp)

    # URL to click
#    print(url)

    # For infobox
    new_list = ({"infobox": weather_string, "id": url, "content": summary, "img_src": url, "content": summary, "urls": [{"title": summary, 'url':url}]})
    results.append(new_list)

    # For link results
#    results.append({'answer': now['summary'], 'content': weather_string, 'url': url, 'infobox': summary, 'title': summary, 'img_src': url, 'content': 'title', 'attributes["image"]': url, 'attributes["src"]': url, 'alt': url})

    # For link results
#    results.append({"url": url, "id": url, "title": weather_string})

    return results
