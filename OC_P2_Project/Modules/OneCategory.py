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

def rech_info_category(url_cat):
    response = requests.get(url_cat)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")

        ' Recherche du nom de la catégorie'
        ul = soup.find('ul',attrs='breadcrumb',)
        li = ul.find('li',attrs='active')
        category = li.text
    return category
    pass

def rech_tab_category(url_cat,category):

    list_books=[]

    list_books.append('test')
    list_books.append('test2')





    return list_books


if __name__ == '__main__':
    url_cat = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    category = rech_info_category(url_cat)

    list_books = rech_tab_category(url_cat,category)
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