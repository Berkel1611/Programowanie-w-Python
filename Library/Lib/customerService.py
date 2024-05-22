'''
NAME
    customerService

DESCRIPTION
    This module allows the administrator to manage customer and address database.

    This tool accepts file (.csv) that includes customers' data.

    This script requires 'csv', 'datetime', 'os' be installed within the Python
    environment you are running this script in.

FUNCTIONS
    This module contains the following functions:
    * addAddress(ID, STREET, CITY, COUNTRY) - adds new customer's address to database
    ID - ID of the customer
    STREET, CITY, COUNTRY - address of the customer

    * deleteAddress(ID) - deletes customer's address
    ID - ID of the customer

    * addCustomer(NAME, **kwargs) - adds new customer to database
    NAME - name of the customer
    kwargs - optional arguments (EMAIL, PHONE, STREET, CITY, COUNTRY), NULL as default

    * deleteCustomer(value, option) - deletes customer from database
    value - ID or NAME of the customer to delete
    option - user has to choose if customer should be deleted by ID or by NAME
'''

import csv
import additionalFun
from datetime import date
import os
from tkinter.messagebox import showinfo, showerror


def addAddress(ID, STREET, CITY, COUNTRY):
    """
    Adds an address to the database

    Args:
        ID: ID of the customer whose address is to be added
        STREET (str): residential street
        CITY (str): city of residence
        COUNTRY (str): home country
    """
    if STREET == '': STREET = 'NULL'
    if CITY == '': CITY = 'NULL'
    if COUNTRY == '': COUNTRY = 'NULL'
    with open('address.csv', mode='a', newline='\n') as csv_file:
        fieldnames = additionalFun.getFieldnames('address.csv')
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(dict(zip(fieldnames, [ID, STREET, CITY, COUNTRY])))


def deleteAddress(ID):
    """
    Deletes address from the database.

    Args:
        ID: ID of the deleted customer.
    """
    # loading data from database
    addresses = additionalFun.loadData('address.csv')
    # searching for book to delete
    addresses = [row for row in addresses if row['ID'] != str(ID)]
    # saving updated data to database
    additionalFun.updateData('address.csv', addresses)


def addCustomer(NAME, EMAIL, PHONE, STREET, CITY, COUNTRY):
    """
    Adds a customer to the database. Creates customer's file in directory 'DATABASE'.

    Args:
        NAME (str): name of the customer
        **kwargs (dict):
            EMAIL (str): e-mail of the customer,
            PHONE (str): phone number of the customer,
            STREET (str): residential street,
            CITY (str): city of residence,
            COUNTRY (str): home country,
    Returns:
        showinfo: (addedMessage) info about result
        showerror: (validData) if incorrect format of data
        showerror: (noData) if 'NAME' not provided
    """
    # checking what parameters have been provided
    if NAME == '':
        return showerror('noData', 'Musisz wpisać imię.')
    if EMAIL == '': EMAIL = 'NULL'
    elif not additionalFun.isEmailValid(EMAIL):
        return showerror('validData', 'Niepoprawny format e-maila')
    if PHONE == '': PHONE = 'NULL'
    elif not additionalFun.isPhoneValid(PHONE):
        return showerror('validData', 'Niepoprawny format numeru telefonu')
    # searching for the unique ID
    getColumn = additionalFun.getColumnFromData(additionalFun.loadData('customer.csv'))
    ids = getColumn('ID')
    ID = additionalFun.randomIdGenerator(ids)
    # adding a new customer's data
    with open('customer.csv', mode='a', newline='\n') as csv_file:
        fieldnames = additionalFun.getFieldnames('customer.csv')
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(dict(zip(fieldnames, [ID, NAME, EMAIL, PHONE, date.today(), date.today()])))
    # adding a new customer's address
    addAddress(ID, STREET, CITY, COUNTRY)
    # creating customer's file in DATABASE
    if not os.path.exists('DATABASE'):
        os.makedirs('DATABASE')
    path = os.path.join(os.getcwd(), 'DATABASE', ID)
    file = open(path, 'w')
    file.close()
    return showinfo('addedMessage', "Użytkownik został pomyślnie dodany.")


def deleteCustomer(value, option):
    """
    Deletes customer's data from the database

    Args:
        value: ID or NAME of the customer to delete
        option (str): information about value ("ID" or "NAME")
    Returns:
        showerror: (notFoundMessage) if file with data was not found or the customer does not exist in database
        showinfp: (deletedMessage) if customer was successfully deleted
    Raises:
        IndexError: if customer is not in database
        FileNotFoundError: if file 'customer.csv' doesn't exist
        PermissionError: if program doesn't have access do 'DATABASE' directory
    """
    # loading data from database
    try:
        data = additionalFun.loadData('customer.csv')
    except FileNotFoundError:
        return showerror('notFoundMessage', 'Plik nie istnieje!')
    # searching for book to delete
    ID = ""
    if option == 'ID':
        try:
            value = int(value)
            ID = [row['ID'] for row in data if row['ID'] == str(value)][0]
        except ValueError:
            return showerror('ValueError', 'Niepoprawne ID.')
        except IndexError:
            return showerror('notFoundMessage', 'Użytkownik o podanym ID nie istnieje.')
        # if customer exists in database
        data = [row for row in data if row['ID'] != str(value)]
        deleteAddress(str(value))
    elif option == 'NAME':
        if len(value) == 0:
            return showerror('noData', 'Brak wymaganych danych.')
        try:
            ID = [row['ID'] for row in data if row['NAME'] == value][0]
        except IndexError:
            return showerror('notFoundMessage', 'Użytkownik o podanej nazwie nie istnieje.')
        data = [row for row in data if row['NAME'] != value]
        deleteAddress(ID)
    # saving updated data to database
    additionalFun.updateData('customer.csv', data)
    # deleting customer's file
    try:
        os.remove(os.path.join(os.getcwd(), 'DATABASE', ID))
    except PermissionError as e:
        return showerror('Permission denied', 'Brak dostępu do pliku \'DATABASE\'')
    return showinfo('deletedMessage', 'Użytkownik został pomyślnie usunięty.')
