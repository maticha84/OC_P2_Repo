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
from OneBook import rech_info_page

def rech_info_category(soup):


    #Recherche du nom de la catégorie
    ul = soup.find('ul',attrs='breadcrumb')
    li = ul.find('li',attrs='active')
    category = li.text
    return category
    pass

def rech_tab_category(soup,category):

    list_books=[]
    url_catalogue = 'http://books.toscrape.com/catalogue/'
    # choix : il n'y a qu'une page ou il y en a plusieurs


    # si plusieurs pages, alors
    if soup.find('ul',attrs = "pager") :
        # récupérer le nombre x de pages à scroller,
        pager = soup.find('ul',attrs = "pager").text
        pager = pager.strip()
        pager = pager.split()
        x = int(pager[3])
        # pour url_page1  à url_pagex
        for i in range(1,x+1,1):
            url_page = url_cat.split('/index.html')
            urlpage = url_page[0]+'/page-'+str(i)+'.html'
            # recherche des liens dans les pages et les ajouter dans le tableau des liens
            rech_liens = requests.get(urlpage)
            if rech_liens.ok:
                soup_liens = BeautifulSoup(rech_liens.text, "html.parser")
                h3s = soup_liens.findAll('h3')
                for h3 in h3s:
                    a = h3.find('a')
                    ref_book = a['href'].split('../../../')[1]

                    url_add = url_catalogue + ref_book
                    list_books.append(url_add)


            pass


    # si une seule page, alors
    else:
        print('KO')
    # recherche des liens dans la pageet les ajouter dans le tableau des liens


    #retourne la liste des url des livres de la catégorie
    return list_books


if __name__ == '__main__':
    url_cat = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    urlsite = "http://books.toscrape.com"
    #url_cat = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    response = requests.get(url_cat)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")

        category = rech_info_category(soup)
        list_books = rech_tab_category(soup,category)
        #print(list_books)
        Dict_for_CSV = {}
        Dict_for_CSV['product_page_url'] = []
        Dict_for_CSV['title'] = []
        Dict_for_CSV['product_description'] = []
        Dict_for_CSV['universal_product_code'] = []
        Dict_for_CSV['price_excluding_tax'] = []
        Dict_for_CSV['price_including_tax'] = []
        Dict_for_CSV['number_available'] = []
        Dict_for_CSV['review_rating'] = []
        Dict_for_CSV['category'] = []
        Dict_for_CSV['image_url'] = []
        for book in list_books:
            responseBook = requests.get(book)
            if response.ok:
                title, product_description, universal_product_code, price_excluding_tax, price_including_tax,\
                number_available, review_rating, category, image_url = rech_info_page(book\
                ,BeautifulSoup(responseBook.text,"html.parser"),urlsite)
                Dict_for_CSV['product_page_url'].append(book)
                Dict_for_CSV['title'].append(title)
                Dict_for_CSV['product_description'].append(product_description)
                Dict_for_CSV['universal_product_code'].append(universal_product_code)
                Dict_for_CSV['price_excluding_tax'].append(price_excluding_tax)

                Dict_for_CSV['price_including_tax'].append(price_including_tax)
                Dict_for_CSV['number_available'].append(number_available)
                Dict_for_CSV['review_rating'].append(review_rating)
                Dict_for_CSV['category'].append(category)
                Dict_for_CSV['image_url'].append(image_url)

        #Mise en forme dans un csv de résultat, du nom de la catégorie - Unicode utf-8

        data = DataFrame(Dict_for_CSV, columns=Dict_for_CSV.keys())
        export_csv = data.to_csv(category+'.csv',mode='w',index=False,sep=';',quotechar='"',encoding='utf-8')

