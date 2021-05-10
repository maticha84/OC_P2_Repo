"""
Le but est ici de scroller tous les livres d'une catégorie définie
afin de permettre de récupérer tous les éléments pour chaque livre de la
catégorie dans un fichier csv
Exemple de la catégory Mystery
http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
"""

import requests
import urllib.request
from bs4 import BeautifulSoup
import re

def rech_info_category(soup):


    #Recherche du nom de la catégorie
    ul = soup.find('ul',attrs='breadcrumb',)
    li = ul.find('li',attrs='active')
    category = li.text
    return category
    pass

def rech_tab_category(soup,category):

    list_books=[]

    # choix : il n'y a qu'une page ou il y en a plusieurs


    # si plusieurs pages, alors
    if soup.find('ul',attrs = "pager") :
        # récupérer le nombre x de pages à scroller,
        pager = soup.find('ul',attrs = "pager").text
        pager = pager.strip()
        pager = pager.split()
        x = int(pager[3])
        print(x)
        # pour url_page1  à url_pagex
        for i in range(1,x+1,1):
            print(i)
            url_page = url_cat.split('/index.html')
            urlpage = url_page[0]+'/page-'+str(i)+'.html'
            print(urlpage)
            # recherche des liens dans les pages et les ajouter dans le tableau des liens
            rech_liens = requests.get(urlpage)
            if rech_liens.ok:
                soup_liens = BeautifulSoup(rech_liens.text, "html.parser")
                h3 = soup_liens.findAll('h3')
                print(h3)

            pass


    # si une seule page, alors
    else:
        print('KO')
    # recherche des liens dans la pageet les ajouter dans le tableau des liens
    list_books.append('test2')





    #retourne la liste des url des livres de la catégorie
    return list_books


if __name__ == '__main__':
    url_cat = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    #url_cat = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    response = requests.get(url_cat)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")

        category = rech_info_category(soup)
        list_books = rech_tab_category(soup,category)
        print(list_books)

    #print(rech_info_category(url_cat))



"""
Pour le csv - utilisation de pandas : 
from pandas import DataFrame
C = {'Nom': ['Depond','Alicat', 'Muller','Massont'],
'Prénom': ['Marcel', 'Patricia', 'Antoni','Rudolf'],
'E-mail': ['Marcel@gmail.com', 'Alicatpa@gmail.com',
'Antoni.muller@gmail.com','Massont.rudolf@gmail.com'],
'Télephone': ['1020304050', '.1224455660', '1669988445','1669988444'],
}
données = DataFrame(C, columns= ['Nom', 'Prénom', 'E-mail', 'Télephone'])
export_csv = df.to_csv ('resultat.csv', index = None, header=True, encoding='utf-8', sep=';')
print(données)
"""