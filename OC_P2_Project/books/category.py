# -*- coding: utf-8 -*-

"""
Le but est ici de scroller tous les livres d'une catégorie définie
afin de permettre de récupérer tous les éléments pour chaque livre de la
catégorie dans un fichier csv
Exemple de la catégory Mystery
http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
"""

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
from books.book import search_info_page
import os
import re


def search_info_category(soup_category):
    """
    Cette fonction permet de récupérer le nom de la catégorie que l'on est en train de scroller

    soup_category : paramètre contenant le résultat de la commande BeautifulSoup sur la réponse à la requète sur l'url
    de la catégorie.
    """

    # Recherche du nom de la catégorie
    ul = soup_category.find('ul', attrs='breadcrumb')
    li = ul.find('li', attrs='active')
    category = li.text
    if not os.path.exists('./Lists of Categories/' + category + '_pictures'):
        os.mkdir('./Lists of Categories/' + category + '_pictures')
    return category


def search_tab_category(soup_category, url_category):
    """
    Cette fonction permet de rechercher tous les livres en fonction du nombre de pages dans la
    catégorie.
    Cette fonction permet de retourner un tableau contenant la liste des URL des livres de la
    catégorie srollée.
    """
    list_books = []
    url_catalogue = 'http://books.toscrape.com/catalogue/'

    # si plusieurs pages, alors
    if soup_category.find('ul', attrs="pager"):
        # récupérer le nombre x de pages à scroller,
        pager = soup_category.find('ul', attrs="pager").text
        pager = pager.strip()
        pager = pager.split()
        x = int(pager[3])
        # pour url_page1  à url_pagex
        for i in range(1, x + 1, 1):
            url = url_category.split('/index.html')
            url_page = url[0] + '/page-' + str(i) + '.html'
            # recherche des liens dans les pages et les ajouter dans le tableau des liens
            research_links = requests.get(url_page)
            if research_links.ok:
                soup_links = BeautifulSoup(research_links.content, "html.parser")
                h3s = soup_links.findAll('h3')
                for h3 in h3s:
                    a = h3.find('a')
                    ref_book = a['href'].split('../../../')[1]
                    url_add = url_catalogue + ref_book
                    list_books.append(url_add)


    # si une seule page, alors
    else:
        research_links = requests.get(url_category)
        if research_links.ok:
            soup_links = BeautifulSoup(research_links.content, "html.parser")
            h3s = soup_links.findAll('h3')
            for h3 in h3s:
                a = h3.find('a')
                ref_book = a['href'].split('../../../')[1]
                url_add = url_catalogue + ref_book
                list_books.append(url_add)

    # retourne la liste des url des livres de la catégorie
    return list_books


def crea_csv_by_category(category, list_books, url_site, dico_for_csv):
    """
    Cette fonction permet de récupérer dans un fichier csv du nom de la catégorie la liste des
    éléments de chaque livre de la catégorie.
    Pour fonctionner, elle s'appuie sur la fonction search_info_page du module book.py
    Le fichier csv se créera dans un dossier 'List of Categories', là où la fonction sera lancée.
    """

    # Récupération des éléments pour chaque book de la liste récupérée et création des dossiers de sauvegarde

    for book in list_books:
        response_book = requests.get(book)
        if response_book.ok:
            title, product_description, universal_product_code, price_excluding_tax, price_including_tax, \
            number_available, review_rating, category, image_url = \
                search_info_page(BeautifulSoup(response_book.content, "html.parser"), url_site)
            dico_for_csv['product_page_url'].append(book)
            dico_for_csv['title'].append(title)
            dico_for_csv['product_description'].append(product_description)
            dico_for_csv['universal_product_code'].append(universal_product_code)
            dico_for_csv['price_excluding_tax'].append(price_excluding_tax)
            dico_for_csv['price_including_tax'].append(price_including_tax)
            dico_for_csv['number_available'].append(number_available)
            dico_for_csv['review_rating'].append(review_rating)
            dico_for_csv['category'].append(category)
            dico_for_csv['image_url'].append(image_url)

    # Mise en forme dans un csv de résultat, du nom de la catégorie - Unicode utf-8
    data = DataFrame(dico_for_csv, columns=dico_for_csv.keys())
    export_csv = data.to_csv('./Lists of Categories/' + category + '.csv', mode='w', index=False, sep=';',
                             quotechar='"', encoding='utf-8-sig')

    return export_csv
