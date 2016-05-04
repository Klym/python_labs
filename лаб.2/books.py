# -*- coding: utf-8 -*-
import abc

class Taggable(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def tag(self):
        """ абстрактный парсинг """

class Book(Taggable):
    
    def __init__(self, name, author):
        if name == '':
            raise NameError('Empty Name!')
        self.__name = name
        self.__author = author
    
    def tag(self):
        return [w for w in self.__name.split(' ') if w[0].isupper()]
        
    @property
    def name(self):
        return self.__name
    
    @property
    def author(self):
        return self.__author
        
class Library(object):
    
    def __init__(self, number, address):
        self.__number = number
        self.__address = address
        self.__books = []
        
    def __iadd__(self, book):
        self.__books.append(book)