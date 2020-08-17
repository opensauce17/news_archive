#! /usr/bin/env python

import requests
import json

wayback_url = 'https://pragma.archivelab.org'

news_url = "https://www.nintendolife.com/news/2020/03/here_are_the_full_patch_notes_for_animal_crossing_new_horizons_version_1_1_0"

data = {"url": ""+news_url+"", "annotation": {"id": "lst-ib", "message": "world news archive"}}


x = requests.post(wayback_url, data = data)

x_json = json.loads(x.text)

try:
    archive_url = x_json['wayback_id']
    print('https://web.archive.org/' + archive_url)
except KeyError:
    print('No URL yet')


