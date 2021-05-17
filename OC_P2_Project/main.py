# -*- coding: utf-8 -*-
"""
Ceci est le script qui lancer l'application générale.

Il s'appuie sur 4 modules, présent dans le dossier books :
books_by_category.py
category.py
book.py
parrallel_work.py

Sans ces 4 fichiers, le script actuel ne fonctionnera pas.

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
from books import parallel_work as pw
from books import books_by_category as bbc
from books import category as oc


if not os.path.exists('./Lists of Categories'):
    os.mkdir('./Lists of Categories')

url_site = "http://books.toscrape.com"
response_site = requests.get(url_site)

if response_site.ok:
    print('Start scrapping...')
    tps1 = time.time()
    soup_url_site = BeautifulSoup(response_site.content,'html.parser')

    list_url_category=bbc.research_all_category(url_site,soup_url_site)

    thread_count = 10

    queue = Queue()

    for i in range(thread_count):
        parallel_work = pw.ParallelWorkGlobal(queue,url_site)
        parallel_work.daemon = True
        parallel_work.start()

    for url_category in list_url_category:
        queue.put(url_category)

    queue.join()

    tps2 = int(time.time() - tps1)
    tps_final = time.strftime('%H:%M:%S', time.gmtime(tps2))
    print('End scrapping, during : '+str(tps_final)+' seconds')

