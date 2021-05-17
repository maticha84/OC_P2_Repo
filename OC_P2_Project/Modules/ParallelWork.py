# -*- coding: utf-8 -*-

from threading import Thread
from queue import Queue
from Modules import AllBooksByCatergory as abc
from Modules import OneCategory as oc


class ParallelWorkGlobal(Thread):
    """
    Classe permettant la mise en place de parallèlisation entre les exécutions des différentes catégories.
    queue : les urls à scapper, qui sont mises en file d'attente
    urlsite : l'adresse url du site : "http://books.toscrape.com"
    """

    def __init__(self, queue,urlsite):
        Thread.__init__(self)
        self.queue = queue
        self.urlsite = urlsite


    def run(self):
        while True:
            urlCat = self.queue.get()
            abc.result_main(self.urlsite,urlCat)
            self.queue.task_done()

