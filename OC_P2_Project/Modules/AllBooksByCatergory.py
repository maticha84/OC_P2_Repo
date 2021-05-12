# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def research_all_category(urlsite,soupUrlSite):

    """
    Cette fonction permet de rechercher toutes les pages de catégorie.
    elle retourne un tableau avec les urls des pages de chaque catégorie.
    """

    urlCat=[]
    divClassSideCat = soupUrlSite.find('div',attrs='side_categories')
    ul = divClassSideCat.find('ul',attrs=None)
    #print(ul)
    allRefCat = ul.findAll('a')
    for a in allRefCat:
        category = a['href']
        urlCat.append(urlsite + '/'+category)
    return urlCat


if __name__ == '__main__':
    urlsite = "http://books.toscrape.com"
    response = requests.get(urlsite)

    if response.ok:
        soupUrlSite = BeautifulSoup(response.text,'html.parser')
        print(research_all_category(urlsite,soupUrlSite))