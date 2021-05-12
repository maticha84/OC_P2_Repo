# -*- coding: utf-8 -*-

"""
Le but est ici de scroller tous les livres d'une catégorie définie
afin de permettre de récupérer tous les éléments pour chaque livre de la
catégorie dans un fichier csv
Exemple de la catégory Mystery
http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
"""

import requests
import csv
import urllib.request
from bs4 import BeautifulSoup
import re
from pandas import DataFrame
from Modules.OneBook import search_info_page
import os
def search_info_category(soupCat):


    #Recherche du nom de la catégorie
    ul = soupCat.find('ul',attrs='breadcrumb')
    li = ul.find('li',attrs='active')
    category = li.text
    return category
 

def search_tab_category(soupCat,urlCat):

    listBooks=[]
    urlCatalogue = 'http://books.toscrape.com/catalogue/'
    # choix : il n'y a qu'une page ou il y en a plusieurs


    # si plusieurs pages, alors
    if soupCat.find('ul',attrs = "pager") :
        # récupérer le nombre x de pages à scroller,
        pager = soupCat.find('ul',attrs = "pager").text
        pager = pager.strip()
        pager = pager.split()
        x = int(pager[3])
        # pour url_page1  à url_pagex
        for i in range(1,x+1,1):
            url = urlCat.split('/index.html')
            urlPage = url[0]+'/page-'+str(i)+'.html'
            # recherche des liens dans les pages et les ajouter dans le tableau des liens
            researchLinks = requests.get(urlPage)
            if researchLinks.ok:
                soupLinks = BeautifulSoup(researchLinks.text, "html.parser")
                h3s = soupLinks.findAll('h3')
                for h3 in h3s:
                    a = h3.find('a')
                    refBook = a['href'].split('../../../')[1]

                    urlAdd = urlCatalogue + refBook
                    listBooks.append(urlAdd)


    # si une seule page, alors
    else:
        researchLinks = requests.get(urlCat)
        if researchLinks.ok:
            soupLinks = BeautifulSoup(researchLinks.text, "html.parser")
            h3s = soupLinks.findAll('h3')
            for h3 in h3s:
                a = h3.find('a')
                refBook = a['href'].split('../../../')[1]

                urlAdd = urlCatalogue + refBook
                listBooks.append(urlAdd)
    # recherche des liens dans la pageet les ajouter dans le tableau des liens


    #retourne la liste des url des livres de la catégorie
    return listBooks


def crea_csv_by_category(category,list_books,urlsite):
    # Création dico pour le csv
    dictForCsv = {}
    dictForCsv['product_page_url'] = []
    dictForCsv['title'] = []
    dictForCsv['product_description'] = []
    dictForCsv['universal_product_code'] = []
    dictForCsv['price_excluding_tax'] = []
    dictForCsv['price_including_tax'] = []
    dictForCsv['number_available'] = []
    dictForCsv['review_rating'] = []
    dictForCsv['category'] = []
    dictForCsv['image_url'] = []

    # Récupération des éléments pour chaque book de la liste récupérée et création des dossiers de sauvegarde
    for book in list_books:
        responseBook = requests.get(book)
        if responseBook.ok:
            title, product_description, universal_product_code, price_excluding_tax, price_including_tax, \
            number_available, review_rating, category, image_url = \
                search_info_page(BeautifulSoup(responseBook.text,"html.parser"),urlsite)
            dictForCsv['product_page_url'].append(book)
            dictForCsv['title'].append(title)
            dictForCsv['product_description'].append(product_description)
            dictForCsv['universal_product_code'].append(universal_product_code)
            dictForCsv['price_excluding_tax'].append(price_excluding_tax)
            dictForCsv['price_including_tax'].append(price_including_tax)
            dictForCsv['number_available'].append(number_available)
            dictForCsv['review_rating'].append(review_rating)
            dictForCsv['category'].append(category)
            dictForCsv['image_url'].append(image_url)

    # Pour la sauvegarde des fichiers csv
    if not os.path.exists('./Lists of Category'):
        os.mkdir('./Lists of Category')


    # Mise en forme dans un csv de résultat, du nom de la catégorie - Unicode utf-8
    data = DataFrame(dictForCsv, columns=dictForCsv.keys())
    export_csv = data.to_csv('./Lists of Category/'+category + '.csv', mode='w', index=False, sep=';', quotechar='"'\
                             ,encoding='utf-8')


    return export_csv

if __name__ == '__main__':
    #url_cat = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    urlsite = "http://books.toscrape.com"
    urlCat = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    response = requests.get(urlCat)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")

        category = search_info_category(soup)
        listBooks = search_tab_category(soup,urlCat)
        crea_csv_by_category(category,listBooks,urlsite)



