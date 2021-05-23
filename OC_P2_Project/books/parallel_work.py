# -*- coding: utf-8 -*-

from threading import Thread
from queue import Queue
from books import books_by_category as bbc


class ParallelWorkGlobal(Thread):
    """
    Classe permettant la mise en place de parallèlisation entre les exécutions des différentes catégories.
    queue : les urls à scrapper, qui sont mises en file d'attente
    urlsite : l'adresse url du site : "http://books.toscrape.com"
    """

    def __init__(self, queue,url_site):
        Thread.__init__(self)
        self.queue = queue
        self.url_site = url_site


    def run(self):
        while True:
            url_category = self.queue.get()
            bbc.result_main(self.url_site, url_category)
            self.queue.task_done()

