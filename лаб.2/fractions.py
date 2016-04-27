# -*- coding: utf-8 -*-

class Fraction(object):
    """ Класс для представления обыкновенных дробей """
    def __init__(self, n, d):
        self.__num = n
        self.__den = d
        self.reduce()
        
    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)
    
    def __neg__(self):
        return '-' + self.__str__(self)
    
    def __invert__(self):
        return "%d/%d" % (self.__den, self.__num)
    
    def __pow__(self, power):
        return "%d/%d" % (self.__num**power, self.__den**power)
    
    def __float__(self):
        return self.__num / self.__den
        
    def __int__(self):
        return int(self.__float__(self))
    
    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g
    
    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)