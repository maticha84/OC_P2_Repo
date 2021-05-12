"""
Ceci sera le script qui lancera l'application générale.

A coder :
- le scrapper pour une page
- le scrapper pour une catégorie complète
- le main qui récupèrera toutes les informations du site
"""

import requests
from bs4 import BeautifulSoup
from Modules import AllBooksByCatergory as abc
from Modules import OneCategory as oc
import time
#from Modules import OneBook as ob

urlsite = "http://books.toscrape.com"
responseSite = requests.get(urlsite)

if responseSite.ok:
    soupUrlSite = BeautifulSoup(responseSite.text,'html.parser')

    listUrlCat=abc.research_all_category(urlsite,soupUrlSite)

    for urlCat in listUrlCat:
        print(urlCat)
        responseCat = requests.get(urlCat)
        print(responseCat)
        if responseCat.ok:
            soup = BeautifulSoup(responseCat.text, "html.parser")

            category = oc.search_info_category(soup)
            print('Category '+category+' in progress...')
            listBooks = oc.search_tab_category(soup,urlCat)
            oc.crea_csv_by_category(category, listBooks, urlsite)
            time.sleep(2)
            print('Category '+category+' ok !')



