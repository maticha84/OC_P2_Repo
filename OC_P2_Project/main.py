# -*- coding: utf-8 -*-
"""
Ceci est le script qui lancer l'application générale.

Il s'appuie sur 3 modules, présent dans le dossier Modules :
AllBookByCategory.py
OneCategory.py
OneBook.py

Sans ces 3 fichiers, le script actuel ne fonctionnera pas.

Il permet de récupérer tous les livres, par catégorie, ainsi que l'image de chacun d'eux, dans un dossier
'List of Categories'. Dans ce dossier seront alors générés tous les fichiers csv (1 par catégorie),
ainsi qu'un dossier par catégorie contenant toutes les images de la catégorie.

Les fichiers csv sont encodés en UTF-8, ils doivent donc être ouvert avec cet encodage pour une meilleure lecture.

Le module 'requests' est nécessaire pour récupérer les éléments du site.
Le module 'bs4' est nécessaire pour le parsing du résultat.
une pause de 2s entre chaque scroll de catégorie est mise en place pour éviter les blocages.
"""

import requests
from bs4 import BeautifulSoup
from Modules import AllBooksByCatergory as abc
from Modules import OneCategory as oc
import time


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



