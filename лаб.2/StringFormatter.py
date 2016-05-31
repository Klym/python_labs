# -*- coding: utf-8 -*-
import re

class StringFormatter(object):
    """ Класс для форматирования строк """
    def __init__(self, s):
        self.__s = s
        self.__words = self.__s.split(' ')
        
    def delSmallWords(self, N):
        self.__words = [w for w in self.__words if len(w) > N]
        self.__s = " "
        self.__s = self.__s.join(self.__words)
    
    def replaceDigits(self):
        self.__s = re.sub('\d', '*', self.__s)
    
    def getString(self):
        return self.__s
    
if __name__ == "__main__":
    sf = StringFormatter("your777 password is so small1234")
    sf.delSmallWords(4)
    sf.replaceDigits()
    print sf.getString()