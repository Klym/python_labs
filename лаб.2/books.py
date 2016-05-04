# -*- coding: utf-8 -*-
import abc

class Taggable(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def tag(self):
        pass

class Book(Taggable):
    
    staticNum = 0
    
    def __init__(self, author, name):
        if name == '' or author == '':
            raise ValueError('Empty value! Error rised at book number ' + str(self.__class__.staticNum + 1) + '\n')
        self.__name = name
        self.__author = author
    
    def __str__(self):
        spaceIndex = self.__author.find(' ') + 1
        return '[' + str(self.__num) + '] ' + self.__author[0] + '.' + self.__author[spaceIndex:] + ' \'' + self.__name + '\''
    
    def tag(self):
        return [w for w in self.__name.split(' ') if w[0].isupper()]
    
    def generateCode(self):
        self.__num = self.__class__.staticNum + 1
        self.__class__.staticNum += 1
        return self
        
class Library(object):
    
    def __init__(self, number, address):
        self.__number = number
        self.__address = address
        self.__books = []
    
    def __iter__(self):
        for book in self.__books:
            yield book
    
    def __iadd__(self, book):
        self.__books.append(book.generateCode())
        return self