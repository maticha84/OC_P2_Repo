# OC_P2_Project
####Repo projet 2 - Formation OC Developpeur application - Python
## Introduction

Ce projet a pour objectif de récupérer tous les éléments des livres, par catégorie, se 
trouvant sur le site http://books.toscrape.com/. \
Les éléments récupérés par livre sont :

_product_page_url_ : l'url de la page du livre\
_universal_product_code_ : le code produit UPC\
_title_ : le titre du livre\
_price_including_tax_ : le prix du livre incluant la taxe \
_price_excluding_tax_ : le prix hors taxe \
_number_available_ : le nombre d'exemplaires disponibles \
_product_description_ : la description du livre (le résumé) \
_category_ : la catégorie du livre \
_review_rating_ : la version du livre \
_image_url_ : l'url de l'image du livre \

A l'exécution du fichier _**main.py**_, plusieurs fichiers seront créés :
- un dossier nommé **Lists of Categories** est créé là où sera exécuté le fichier _main.py_.
- dans ce dossier, un fichier csv par catégorie est créé.
- dans ce dossier, un dossier par catégorie est créé (de la forme _'category_pictures'_),
  il contient pour chaque catégorie les images des livres de la catégorie.

## Format du dossier Modules

Dans le dossier **_Modules_** se trouvent 3 fichiers nécessaires à l'éxecution du projet : 

###Fichier _OneBook.py_
Dans ce fichier se trouve la fonction **search_info_page** permettant de scrapper un seul livre.
Le but est de récupérer les informations de ce livre dans un fichier csv.
On en profite pour récupérer l'image du livre par la même occasion.\
Si ce fichier est exécuté directement, il génère un csv du livre pour lequel le fichier 
à été lancé. (l'url exemple pris dans ce fichier est la suivante : 
http://books.toscrape.com/catalogue/eragon-the-inheritance-cycle-1_153/index.html)
###Fichier _OneCategorie.py_
Ce fichier a pour but de scroller tous les livres d'une catégorie définie
afin de permettre de récupérer tous les éléments pour chaque livre de la
catégorie dans un fichier csv. \
Si ce fichier est lancé directement, il permet de générer le csv de la catégorie Mystery
Exemple de la catégory Mystery : 
http://books.toscrape.com/catalogue/category/books/mystery_3/index.html\
Pour fonctionner, il nécessite l'import du fichier _OneBook.py_. \
Dans ce fichier, on trouve 3 fonctions disctinctes : 
- **search_info_category(soupCat)** : permet de récupérer le nom de la catégorie que
    l'on est en train de scroller. \
  soupCat : paramètre obligatoire de la fonction, contenant le résultat de la commande BeautifulSoup sur la réponse à la
  requète sur l'url de la catégorie.
- **search_tab_category(soupCat,urlCat)** : Cette fonction permet de rechercher tous les livres en fonction du nombre de
  pages dans la catégorie. 
  Elle retourne un tableau contenant la liste des URL des livres de la catégorie srollée. 
  Elle prend en compte le fait que la catégorie s'affiche sur une ou plusieurs pages.
  soupCat : paramètre obligatoire de la fonction, contenant le résultat de la commande BeautifulSoup sur la réponse à la 
  requète sur l'url de la catégorie.\
  urlCat : paramètre obligatoire de la fonction, c'est l'url de la catégorie.
- **crea_csv_by_category(category,listBooks,urlsite)** : Cette fonction permet de récupérer dans un fichier csv du nom 
  de la catégorie la liste des éléments de chaque livre de la catégorie.\
    Pour fonctionner, elle s'appuie sur la fonction **search_info_page** du module _OneBook.py_
    Le fichier csv se créera dans un dossier 'List of Categories'. \
  category : paramètre obligatoire, retour de la fonction **search_info_category(soupCat)** \
  listBooks : paramètre obligatoire, retour de la fonction **search_tab_category(soupCat,urlCat)** \
  urlsite : paramètre obligatoire, url du site (ici http://books.toscrape.com/)
###Fichier _AllBooksByCategory.py_

Dans ce fichier se trouve une unique fonction **research_all_category(urlsite,soupUrlSite)**.\
Cette fonction permet de rechercher toutes les pages de catégorie. elle retourne un tableau avec les urls des pages de 
chaque catégorie.\
urlsite : paramètre obligatoire, l'url du site (ici http://books.toscrape.com/) \
soupUrlSite : paramètre obligatoire de la fonction, contenant le résultat de la commande BeautifulSoup sur la réponse à la
  requète sur l'url du site


## Lancement du scrapping

Pour pouvoir utiliser le projet, il vous faudra au préalable récupérer l'intégralité du dossier 
**OC_P2_Projet**. Dans ce dossier, vous trouverez : 
- le dossier Modules
- le fichier __init__.py (qui est vierge)
- le fichier main.py
- le fichier requirements.txt 

Dans un premier temps, vous devrez avoir installé si ce n'est pas encore le cas, les modules présents dans le fichier
requirements.txt. \
Ensuite, executez avec python le fichier main.py. A l'exécution du fichier _**main.py**_, plusieurs fichiers seront créés :
- un dossier nommé **Lists of Categories** est créé là où sera exécuté le fichier _main.py_.
- dans ce dossier, un fichier csv par catégorie est créé.
- dans ce dossier, un dossier par catégorie est créé (de la forme _'category_pictures'_),
  il contient pour chaque catégorie les images des livres de la catégorie.
  
Le temps d'exécution est d'environ 17 min. Le détail s'affiche dans la console d'exécution du script. En fin de 
programme, le temps d'exécution s'affiche.