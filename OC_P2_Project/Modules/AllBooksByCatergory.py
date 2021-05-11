# -*- coding: utf-8 -*-

"""
Ici ce trouveront les fonction permettant de rechercher les différentes url de chaque
catégory, pour faire la recherce par catégorie après.
"""

import requests
import csv
import urllib.request
from bs4 import BeautifulSoup
import re
from pandas import DataFrame



def research_all_category(soupUrlSite):
    print(soupUrlSite)
    pass


if __name__ == '__main__':
    urlsite = "http://books.toscrape.com"
    response = requests.get(urlsite)

    if response.ok:
        soupUrlSite = BeautifulSoup(response.text,'html.parser')
        research_all_category(soupUrlSite)