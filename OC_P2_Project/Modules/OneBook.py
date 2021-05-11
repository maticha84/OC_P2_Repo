# -*- coding: utf-8 -*-

"""
Ici, on va créer les fonctions permettant de scrapper un seul livre
le but étant de récupérer les informations de ce livre dans
un fichier csv.
"""

import requests
import urllib.request
from bs4 import BeautifulSoup
import re
import csv

def search_info_page(url,soup,urlsite):
    """
    Title
    """
    titles = soup.find('title')
    title = titles.text.split('|')[0]
    title = title.strip()
    # print(title)

    """
    Product description
    """
    articles = soup.findAll('article')
    for article in articles:
        p = article.find('p', attrs=None)
        if p != None:
            product_description = p.text

    # print(product_description)
    """
    Product Information
    - UPC
    - Price excluding tax
    - Price Including tax
    - number available
    - review rating
    """
    trs = soup.findAll('tr')
    for tr in trs:
        th = tr.find('th')
        # print(th.text)
        td = tr.find('td')
        # print(td.text)
        if th.text == "UPC":
            universal_product_code = td.text
            # break
        elif th.text == "Price (excl. tax)":
            price_excluding_tax = td.text.split('Â')[1]
            # break
        elif th.text == "Price (incl. tax)":
            price_including_tax = td.text.split('Â')[1]
            # break
        elif th.text == "Availability":
            number_available = td.text
            # break
        elif th.text == "Number of reviews":
            review_rating = td.text
            # break

    """
    Category
    <a href="../category/books/fantasy_19/index.html">Fantasy</a>
    """
    aaa = soup.findAll('a')
    for a in aaa:
        ref = a['href']
        rech = re.search('../category/books/', ref)
        if not rech == None:
            category = a.text
    """
    Image_url
    <img src="../../media/cache/8e/5a/8e5a6639c7e2f9b59ff15f04a3b055e1.jpg" alt="Eragon (The Inheritance Cycle #1)">
    """
    imgs = soup.findAll('img')
    for img in imgs:
        alt = img['alt']
        src = img['src']
        if alt == title:
            image_url = src.replace('../..', urlsite)
            """pour le nom de l'image  
            specialchars = ":/()#$%^*"
            for specialchar in specialchars:
                title = title.replace(specialchar,'-')
            urllib.request.urlretrieve(image_url ,title +'.jpg') """

            """
            Product_page_url
            """
    product_page_url = url
    return title, product_description, universal_product_code, price_excluding_tax, price_including_tax, \
           number_available, review_rating, category,image_url


if __name__ == '__main__':
    url = "http://books.toscrape.com/catalogue/eragon-the-inheritance-cycle-1_153/index.html"
    urlsite = "http://books.toscrape.com"
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        title, product_description, universal_product_code, price_excluding_tax, price_including_tax, number_available,\
        review_rating, category, image_url = rech_info_page(url,soup,urlsite)

        """Pour création d'un fichier csv pour un livre
        Crée un csv avec les éléments du livre là où est executé le fichier
        OneBook.py"""

        specialchars = ":/()#$%^*"
        for specialchar in specialchars:
            title = title.replace(specialchar, '-')
        with open(title+'.csv', 'w', newline='') as fichiercsv:
            writer = csv.writer(fichiercsv,delimiter=';',quotechar='"')
            writer.writerow(['product_url_page','universal_product_code','title','price_including_tax',\
                             'price_excluding_tax', 'number_available','category',\
                            'review_rating','image_url','product_description'])
            writer.writerow([url,universal_product_code,title,price_including_tax,\
                             price_excluding_tax, number_available,category,\
                             review_rating, image_url,product_description])





