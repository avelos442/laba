import asyncio
import os
import sys

from django.contrib.auth import get_user_model
from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django
django.setup()

from scraping.parsers import *
from scraping.models import Declaration, Url

User = get_user_model()

parsers = (
    (cian, 'cian'),
    (m_2, 'm_2')
)
apart, errors = [], []


def get_settings():
    qs = User.objects.filter(send_email=True).values()
    settings_lst = set((q['city_id'], q['metro_id']) for q in qs)
    return settings_lst


def get_urls(_settings):
    qs = Url.objects.all().values()
    url_dct = {(q['city_id'], q['metro_id']): q['url_data'] for q in qs}
    urls = []
    for pair in _settings:
        tmp = {'city': pair[0], 'metro': pair[1], 'url_data': url_dct[pair]}
        urls.append(tmp)

    return urls


async def main(value):
    func, url, city, metro = value
    _kv, err = await loop.run_in_executor(None, func, url, city, metro)
    errors.extend(err)
    apart.extend(_kv)


settings = get_settings()
url_list = get_urls(settings)

loop = asyncio.get_event_loop()
tmp_tasks = [(func, data['url_data'][key], data['city'], data['metro'])
             for data in url_list
             for func, key in parsers]
tasks = asyncio.wait([loop.create_task(main(f)) for f in tmp_tasks])

'''
for data in url_list:

  for func, key in parsers:
      url = data['url_data'][key]
        a, e = func(url, city=data['city'], metro=data['metro'])
        apart += a
        errors += e
'''

loop.run_until_complete(tasks)
loop.close()

for kv in apart:
    d = Declaration(**kv)
    try:
        d.save()
    except DatabaseError:
        pass

'''
h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(apart))
h.close()
'''
