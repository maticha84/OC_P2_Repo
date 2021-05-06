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

else:
    print('error')