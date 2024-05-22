'''
NAME
    bookService

DESCRIPTION
    This module allows the administrator to manage book database.

    This tool accepts files (.csv, .txt) that includes books' data.

    This script requires 'csv', 'datetime' , 'os' be installed within the Python
    environment you are running this script in.

FUNCTIONS
    This module contains the following functions:
    * addBook(AUTHOR, TITLE, PAGES) - adds a book to the database
    AUTHOR, TITLE, PAGES - provided by user
    CREATED, UPDATED - provided by datatime

    * deleteBook(ID) - deletes a book from the database
    value - ID or TITLE of the book to delete
    option - user has to choose if book should be deleted by ID or by TITLE
    Returns messages about the result.

    * bookRental(ID, *args) - deletes rented books from database and updates file of the customer who rents the books
    ID - ID of the customer who rents books
    args - books which customer is renting
    Returns messages about the result.

    * returnBook(ID, TITLE) - adds returned book to database and updates customer's file
    ID - ID of the customer who returns the book
    TITLE - title of the returned book
    Returns messages about the result.

EXAMPLES
    addBook("Stephen King", "The Shining", 447)
    deleteBook("Stephen King", "TITLE")
    bookRental(201, "The Shining", "The Witcher")
    returnBook(201, "The Shining")
'''

import csv
import os
import additionalFun
from datetime import date
from tkinter.messagebox import showinfo, showerror


def returnBooks(fun):
    def wrapper(ID, *args):
        for book in args:
            fun(ID, book)

    return wrapper


def addBook(AUTHOR, TITLE, PAGES):
    """
    Adds a book to the database

    Args:
        AUTHOR (str): author of the book
        TITLE (str): title of the book
        PAGES (int): pages of the book
    Returns:
        showinfo: (addedMessage) if book was successfully added
        showerror: if AUTHOR, TITLE or PAGES are empty
        showerror: if PAGES is not digit
    """
    if len(AUTHOR) == 0 or len(TITLE) == 0 or len(str(PAGES)) == 0:
        return showerror('noRequiredData', 'Nie podano kluczowych parametrów.')
    if not str(PAGES).isdigit():
        return showerror('intRequired', 'Liczba stron musi być dodatnią liczbą całkowitą.')
    # loading IDs from database, to find unique one
    getColumn = additionalFun.getColumnFromData(additionalFun.loadData('book.csv'))
    ids = getColumn('ID')
    ID = additionalFun.linearIdGenerator(ids)

    # adding a new book
    fieldnames = additionalFun.getFieldnames('book.csv')
    with open('book.csv', mode='a', newline='\n') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(dict(zip(fieldnames, [ID, AUTHOR, TITLE, PAGES, date.today(), date.today()])))
    return showinfo('addedMessage', 'Książka została pomyślnie dodana.')


def deleteBook(value, option):
    """
    Deletes book from the database

    Args:
        value: ID or TITLE of the book to delete
        option (str): information about value ("ID" or "TITLE")
    Returns:
        showerror: (notFoundMessage) if book was not found in the database
        showinfo: (deletedMessage) if book was successfully deleted
    Raises:
        ValueError: if option is 'ID' and value is not a digit
    """
    # loading data from database
    books = additionalFun.loadData('book.csv')
    # searching for book to delete
    flag = len(books)
    if option == 'ID':
        try:
            value = int(value)
        except ValueError:
            return showerror('ValueError', 'Niepoprawne ID.')
        books = [row for row in books if row['ID'] != str(value)]
    elif option == 'TITLE':
        if len(value) == 0:
            return showerror('noData', 'Brak wymaganych danych.')
        books = [row for row in books if row['TITLE'] != value]
    if flag == len(books):
        return showerror('notFoundMessage', 'Nie znaleziono podanej książki.')
    # saving updated data to database
    additionalFun.updateData('book.csv', books)
    return showinfo('deletedMessage', 'Książka została pomyślnie usunięta.')


def bookRental(ID, *args):
    """
    Manages book lending. Searches for books to rent,
    deletes them from database and updates customer's file in 'DATABASE' directory.

    Args:
        ID (int): ID of the customer who rents the books
        args: books to rent
    Returns:
        showinfo: (rentedMessage) message with rented books
        showerror: (notFoundMessage) message if there were books which were not found in database
    Raises:
        TypeError: none of the books is available
        FileNotFoundError: if customer's file doesn't exist
    """
    try:
        ID = int(ID)
    except ValueError:
        return showerror('ValueError', 'Niepoprawne ID.')
    # loading data of books to rent
    data = additionalFun.loadData('book.csv')
    # searching for rented books in database
    books = []
    notFound = []
    titles = additionalFun.getColumnFromData(data)('TITLE')
    for title in args:
        if title in titles:
            books.append(data[titles.index(title)])
            # deleting books from database
            deleteBook(title, 'TITLE')
        else:
            notFound.append(title)
    # saving to folder 'DATABASE'
    if not os.path.exists(os.path.join(os.getcwd(), 'DATABASE', str(ID))):
        return showerror('FileNotFound', 'Klient z podanym ID nie istnieje w bazie danych.')
    try:
        file = open(os.path.join(os.getcwd(), 'DATABASE', str(ID)), 'a')
        for book in books:
            file.write('{},{},{},{},{},{},{}\n'
                       .format(book['ID'], book['AUTHOR'], book['TITLE'], book['PAGES'],
                               book['CREATED'], book['UPDATED'], date.today()))
            file.close()
    except TypeError:
        return showerror('notFoundMessage', 'Żadna z podanych książek nie jest dostępna.')
    books = [row['TITLE'] for row in books]
    # notFound = [row['TITLE'] for row in notFound]
    if len(notFound) != 0:
        return showinfo('info', 'Wypożyczone: ' + str(*books) + '\n' + 'Niedostępne: ' + str(*notFound))
    return showinfo('rentedMessage', 'Wypożyczone: ' + str(*books))


@returnBooks
def returnBook(ID, TITLE):
    """
    Returns the book. Makes changes to customer's file and book database.

    Args:
        ID (int): ID of the customer who returns the book
        TITLE (str): title of the returned book
    Returns:
        showerror: (notFoundMessage) if customer's file or book from parameters is not found
        showinfo: (returnedMessage) if book was successfully returned
    Raises:
        FileNotFoundError: if there's no file with given ID
    """
    try:
        ID = int(ID)
    except ValueError:
        return showerror('ValueError', 'Niepoprawne ID.')
    if len(TITLE) == 0:
        return showerror('noData', 'Brak wymaganych danych.')
    # loading data from customer's file
    try:
        file = open(os.path.join(os.getcwd(), 'DATABASE', str(ID)), 'r')
        data = file.readlines()
        file.close()
    except FileNotFoundError:
        return showerror('notFoundMessage', 'Nie znaleziono pliku z podanym ID.')
    # searching for book to return
    book = ""
    for row in data:
        if TITLE == row.split(',')[2] and len(row.split(',')) == 7:
            book = row
            break
    # when the specified book is not in the file
    if len(book) == 0:
        return showerror('notFoundMessage', 'Brak książki na liście wypożyczonych.')
    # adding returned book to the database
    with open('book.csv', mode='a', newline='\n') as csv_file:
        fieldnames = additionalFun.getFieldnames('book.csv')
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(dict(zip(fieldnames, (book[0:len(book) - 23] + ',' + str(date.today())).split(','))))
    # saving changes to the customer's file
    data = [row for row in data if book not in row]
    book = book[0: len(book) - 1].split(',')
    book.append(str(date.today()) + '\n')
    data.append(','.join(book))
    file = open(os.path.join(os.getcwd(), 'DATABASE', str(ID)), 'w')
    file.writelines(data)
    file.close()
    return showinfo('returnedMessage', 'Książka została pomyślnie zwrócona.')
