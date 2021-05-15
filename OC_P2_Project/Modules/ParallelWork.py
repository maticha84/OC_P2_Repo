# -*- coding: utf-8 -*-

from threading import Thread
from queue import Queue
from Modules import AllBooksByCatergory as abc
from Modules import OneCategory as oc


class ParallelWorkGlobal(Thread):


    def __init__(self, queue,urlsite):
        Thread.__init__(self)
        self.queue = queue
        self.urlsite = urlsite


    def run(self):
        while True:
            urlCat = self.queue.get()
            abc.result_main(self.urlsite,urlCat)
            self.queue.task_done()


class ParrallelImageByCategory(Thread):
    def __init__ (self, queue, urlsite,dico):
        Thread.__init__(self)
        self.queue = queue
        self.urlsite = urlsite
        self.dico = dico

    def run(self):
        book = self.queue.get()
        oc.dico_for_csv(book, self.urlsite, self.dico)
        self.queue.task_done()