# -*- coding: utf-8 -*-
from books import Book, Library

lib = Library(1, '51 Some str., NY')
try:
    lib += Book('Leo Tolstoi', 'War and Peace')
    lib += Book('Charles Dickens', 'David Copperfield')
    lib += Book('Arthur Conan Doyle', 'The Lost World')
    lib += Book('', 'Test empty book')
except ValueError as err:
    print(err)

for book in lib:
    print(book)
    print(book.tag())
    print('')