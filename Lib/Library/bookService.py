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

import pandas as pd
from datetime import date

def addBook(AUTHOR, TITTLE, PAGES):
    