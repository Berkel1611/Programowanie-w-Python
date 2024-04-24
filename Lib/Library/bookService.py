'''
NAME
book_service.py

DESCRIPTION
This module allows the administrator to manage book database.

This tool accepts file (.csv) that includes books' data.

This script requires 'pandas', 'datetime' be installed within the Python
environment you are running this script in.

FUNCTIONS

'''

import csv
import additionalFun
from datetime import date


def addBook(AUTHOR, TITLE, PAGES):
    with open('test.csv', mode='a+') as books:
        csv_writer = csv.DictWriter(books, 'csv.DictReader(books).fieldnames')
        csv_reader = csv.DictReader(books)
        ids = []
        for row in csv_reader:
            ids.append(row[0])
        csv_writer.writerow(
            {'ID': additionalFun.generateId(ids),
             'AUTHOR': AUTHOR,
             'TITLE': TITLE,
             'PAGES': PAGES,
             'CREATED': date.today(),
             'UPDATED': date.today()})


addBook('Adam Mickiewicz', 'Pan Tadeusz', 256)
