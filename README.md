# OC_P2_Repo
 ##Repo projet 2 - Formation OC Developpeur application - Python
### Introduction

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

### Format du dossier Modules

Dans le dossier **_Modules_** se trouvent 3 fichiers nécessaires à l'éxecution du projet : 

####Fichier _OneBook.py_
Dans ce fichier se trouve la fonction permettant de scrapper un seul livre
le but étant de récupérer les informations de ce livre dans un fichier csv.
On en profite pour récupérer l'image du livre par la même occasion.\
Si ce fichier est exécuté directement, il génère un csv du livre pour lequel le fichier 
à été lancé. (l'url exemple pris dans ce fichier est la suivante : 
http://books.toscrape.com/catalogue/eragon-the-inheritance-cycle-1_153/index.html)
####Fichier _OneCategorie.py_
Ce fichier a pour but de scroller tous les livres d'une catégorie définie
afin de permettre de récupérer tous les éléments pour chaque livre de la
catégorie dans un fichier csv.\
Exemple de la catégory Mystery : 
http://books.toscrape.com/catalogue/category/books/mystery_3/index.html\
Pour fonctionner, il nécessite l'import du fichier _OneBook.py_. \
Dans ce fichier, on trouve 3 fonctions disctinctes : 
- **search_info_category(soupCat)** : permet de récupérer le nom de la catégorie que
    l'on est en train de scroller. \
  soupCat : paramètre obligatoire de la fonction, contenant le résultat de la commande BeautifulSoup sur la réponse à la requète sur l'url de la catégorie.
- **search_tab_category(soupCat,urlCat)** : 



### Lancement du script
- Un module OneBook.py qui permet la recherche une fois l'url d'un livre sélectionnée.