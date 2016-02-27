# -*- coding: utf-8 -*-
string = raw_input("Введите строку слов:\n")
wordlen = {w: len(w) / 2 for w in string.split(" ")}
print "> 7:"
for word in filter(lambda key: wordlen[key] > 7, wordlen):
    print word
print "\n[4...7]:"
for word in filter(lambda key: wordlen[key] in range(4, 8), wordlen):
    print word
print "\n< 4:"
for word in filter(lambda key: wordlen[key] < 4, wordlen):
    print word