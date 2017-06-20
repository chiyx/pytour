#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import datetime
import random
import re

base_url = 'https://en.wikipedia.org'

random.seed(datetime.datetime.now())


def getLinks(article_url):
    resp = requests.get(base_url + article_url)
    resp.raise_for_status()
    bsObj = BeautifulSoup(resp.text, "html.parser")
    return (
        bsObj.find('div', {"id": "bodyContent"})
        .findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    )

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    new_article = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(new_article)
    links = getLinks(new_article)
