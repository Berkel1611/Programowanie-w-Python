import csv
import random
from fnmatch import fnmatch


def linearIdGenerator(ids):
    i = 101
    while str(i) in ids:
        i += 1
    return str(i)


def randomIdGenerator(ids):
    while True:
        ID = random.randint(1, 10000)
        if str(ID) not in ids:
            break
    return str(ID).zfill(4)


def loadData(csv_file):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)


def updateData(csv_file, data):
    # loading fieldnames
    fieldnames = getFieldnames(csv_file)
    # saving updated data in the file
    with open(csv_file, mode='w', newline='\n') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def getColumnFromData(data):
    def getColumn(header):
        column = []
        for row in data:
            column.append(row[header])
        return column
    return getColumn


def getFieldnames(csv_file):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        return csv_reader.fieldnames


def isEmailValid(EMAIL):
    return fnmatch(EMAIL, '*@*.*')


def isPhoneValid(PHONE):
    return len(PHONE) == 9 and str(PHONE).isdigit()
