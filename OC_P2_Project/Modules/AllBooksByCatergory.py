# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from Modules import OneCategory as oc


def research_all_category(urlsite,soupUrlSite):

    """
    Cette fonction permet de rechercher toutes les pages de catégorie.
    elle retourne un tableau avec les urls des pages de chaque catégorie.
    """

    urlCat=[]
    divClassSideCat = soupUrlSite.find('div',attrs='side_categories')
    ul = divClassSideCat.find('ul',attrs=None)
    allRefCat = ul.findAll('a')
    for a in allRefCat:
        category = a['href']
        urlCat.append(urlsite + '/'+category)
    return urlCat


def result_main(urlsite,urlCat):

    responseCat = requests.get(urlCat)
    if responseCat.ok:
        soup = BeautifulSoup(responseCat.text, "html.parser")

        category = oc.search_info_category(soup)
        print('Category '+category+' in progress...')
        listBooks = oc.search_tab_category(soup,urlCat)
        # creadico
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

        dico = oc.dico_for_csv(urlCat, urlsite, dictForCsv)
        oc.crea_csv_by_category(category, listBooks, urlsite,dico)
        print('Category '+category+' ok !')



if __name__ == '__main__':
    urlsite = "http://books.toscrape.com"
    response = requests.get(urlsite)

    if response.ok:
        soupUrlSite = BeautifulSoup(response.text,'html.parser')
        print(research_all_category(urlsite,soupUrlSite))