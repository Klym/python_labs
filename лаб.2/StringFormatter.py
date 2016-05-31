# -*- coding: utf-8 -*-

class StringFormatter(object):
    """ Класс для форматирования строк """
    def __init__(self, s):
        self.__s = s
        self.__words = self.__s.split(' ')
        
    def delSmallWords(self, N):
        self.__words = [w for w in self.__words if len(w) >= N]
        self.__joinWords(' ', self.__words)
    
    def replaceDigits(self):
        chars = map(lambda ch: '*' if ch.isdigit() else ch, self.__s)
        self.__joinWords('', chars)
    
    def insertSpaces(self):
        chars = map(lambda ch: ch + ' ', self.__s)
        self.__joinWords('', chars)
    
    def sortWordsBySize(self):
        self.__words = sorted(self.__words, key = lambda w: len(w))
        self.__joinWords(' ', self.__words)
        
    def sortWordsLexicographically(self):
        self.__words = sorted(self.__words, key = lambda w: w)
        self.__joinWords(' ', self.__words)
        
    def __joinWords(self, sep, words):
        self.__s  = sep
        self.__s = self.__s.join(words)
    
    def getString(self):
        return self.__s
    
if __name__ == "__main__":
    sf = StringFormatter("your777 password is so small1234")
    sf.delSmallWords(4)
    sf.sortWordsLexicographically()
    sf.replaceDigits()
    sf.insertSpaces()
    
    print sf.getString()