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
import os
import time
from bs4 import BeautifulSoup
from threading import Thread
from queue import Queue
from Modules import ParallelWork as pw
from Modules import AllBooksByCatergory as abc
from Modules import OneCategory as oc


if not os.path.exists('./Lists of Categories'):
    os.mkdir('./Lists of Categories')

urlsite = "http://books.toscrape.com"
responseSite = requests.get(urlsite)

if responseSite.ok:
    print('Start scrapping...')
    tps1 = time.time()
    soupUrlSite = BeautifulSoup(responseSite.text,'html.parser')

    listUrlCat=abc.research_all_category(urlsite,soupUrlSite)

    thread_count = 8

    queue = Queue()

    for i in range(thread_count):
        parallelWork = pw.ParallelWorkGlobal(queue,urlsite)
        parallelWork.daemon = True
        parallelWork.start()

    for urlCat in listUrlCat:
        queue.put(urlCat)

    queue.join()

    tps2 = int(time.time() - tps1)
    tpsFinal = time.strftime('%H:%M:%S', time.gmtime(tps2))
    print('End scrapping, during : '+str(tpsFinal)+' seconds')

