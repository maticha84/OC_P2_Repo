"""
Ici, on va créer les fonctions permettant de scrapper une seule page
"""

import requests
from bs4 import BeautifulSoup
import re

url = "http://books.toscrape.com/catalogue/eragon-the-inheritance-cycle-1_153/index.html"

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    """
    Title
    """
    titles = soup.find('title')
    title = titles.text.split('|')[0]
    title = title.strip()
    #print(title)

    """
    Product description
    """
    articles = soup.findAll('article')
    tests = []
    for article in articles:
        p=article.find('p',attrs = None)
        if p != None:
            #print(p.text)
            product_description = p.text

    #print(product_description)
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
        #print(th.text)
        td = tr.find('td')
        #print(td.text)
        if th.text == "UPC":
            universal_product_code = td.text
            #break
        elif th.text == "Price (excl. tax)":
            price_excluding_tax = td.text.split('Â')[1]
            #break
        elif th.text == "Price (incl. tax)":
            price_including_tax = td.text.split('Â')[1]
            #break
        elif th.text == "Availability":
            number_available = td.text
            #break
        elif th.text == "Number of reviews":
            review_rating = td.text
            #break

    """print(universal_product_code+'\n'+price_excluding_tax + '\n'+price_including_tax +
          '\n' + number_available + '\n'+ review_rating)
    """
    """
    Category
    <a href="../category/books/fantasy_19/index.html">Fantasy</a>
    """
    """
    Image_url
    <img src="../../media/cache/8e/5a/8e5a6639c7e2f9b59ff15f04a3b055e1.jpg" alt="Eragon (The Inheritance Cycle #1)">
    """
    """
    Product_page_url
    """
    product_page_url = url
    #print(product_page_url)
else:
    print('error')