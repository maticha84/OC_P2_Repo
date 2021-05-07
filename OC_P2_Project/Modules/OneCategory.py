"""
Le but est ici de scroller tous les livres d'une catégorie définie
afin de permettre de récupérer tous les éléments pour chaque livre de la
catégorie dans un fichier csv
"""

import requests
import urllib.request
from bs4 import BeautifulSoup
import re