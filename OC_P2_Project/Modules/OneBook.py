"""
Ici, on va créer les fonctions permettant de scrapper une seule page
"""

import requests
from bs4 import BeautifulSoup
import re


def rech_info_page(soup):
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
    """
    Image_url
    <img src="../../media/cache/8e/5a/8e5a6639c7e2f9b59ff15f04a3b055e1.jpg" alt="Eragon (The Inheritance Cycle #1)">
    """
    """
    Product_page_url
    """
    product_page_url = url
    return title, product_description, universal_product_code, price_excluding_tax, price_including_tax, \
           number_available, review_rating
    # print(product_page_url)


if __name__ == '__main__':
    url = "http://books.toscrape.com/catalogue/eragon-the-inheritance-cycle-1_153/index.html"

    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        title, product_description, universal_product_code, price_excluding_tax, price_including_tax, number_available,\
        review_rating = rech_info_page(soup)
        print(title)
        print(product_description)
        print(universal_product_code)
        print(price_excluding_tax)
        print(price_including_tax)
        print(number_available)
        print(review_rating)
