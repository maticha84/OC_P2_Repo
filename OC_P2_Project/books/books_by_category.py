# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from books import category as cat


def research_all_category(url_site, soup_url_site):
    """
    Cette fonction permet de rechercher toutes les pages de catégorie.
    elle retourne un tableau avec les urls des pages de chaque catégorie.
    """

    url_category = []
    div_side_categories = soup_url_site.find('div', attrs='side_categories')
    ul = div_side_categories.find('ul', attrs=None)
    all_reference_category = ul.findAll('a')
    for a in all_reference_category:
        category = a['href']
        url_category.append(url_site + '/' + category)
    return url_category


def result_main(url_site, url_category):
    response_category = requests.get(url_category)
    if response_category.ok:
        soup = BeautifulSoup(response_category.content, "html.parser")

        category = cat.search_info_category(soup)
        print('Category ' + category + ' in progress...')
        list_books = cat.search_tab_category(soup, url_category)
        # creation du dico
        dico_for_csv = {'product_page_url': [], 'title': [], 'product_description': [], 'universal_product_code': [],
                        'price_excluding_tax': [], 'price_including_tax': [], 'number_available': [],
                        'review_rating': [], 'category': [], 'image_url': []}

        cat.crea_csv_by_category(category, list_books, url_site, dico_for_csv)
        print('Category ' + category + ' ok !')

