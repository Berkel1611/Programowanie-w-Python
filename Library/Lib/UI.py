from tkinter import *
import bookService
import customerService
import additionalFun
from tkinter.scrolledtext import ScrolledText


def addBookMenu(window):
    newWindow = Toplevel(window)
    newWindow.title('Dodaj książkę')
    newWindow.geometry('300x300')

    Label(newWindow, text='Autor', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    AUTHOR = Entry(newWindow, font=15)
    AUTHOR.pack(side=TOP, pady=15, padx=15)

    Label(newWindow, text='Tytuł', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    TITLE = Entry(newWindow, font=15)
    TITLE.pack(side=TOP, pady=15, padx=15)

    Label(newWindow, text='Liczba stron', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    PAGES = Entry(newWindow, font=15)
    PAGES.pack(side=TOP, pady=15, padx=15)

    Button(newWindow, text='Zatwierdź', font=('Arial', 13), relief='raised', bd=4,
           command=lambda: bookService.addBook(AUTHOR.get(), TITLE.get(), PAGES.get())).pack(side=TOP, padx=5)


def delBookMenu(window):
    newWindow = Toplevel(window)
    newWindow.title('Usuń książkę')
    newWindow.geometry('250x170')

    Label(newWindow, text='ID/Tytuł', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    value = Entry(newWindow, font=15)
    value.pack(side=TOP, pady=15, padx=15)

    optionFrame = Frame(newWindow)
    optionFrame.pack(side=TOP)
    option = IntVar()
    Radiobutton(optionFrame, text='ID', variable=option, value=1, font=('Arial', 10)).pack(side=LEFT)
    Radiobutton(optionFrame, text="Tytuł", variable=option, value=2, font=('Arial', 10)).pack(side=RIGHT)

    (Button(newWindow, text='Zatwierdź', font=('Arial', 13), relief='raised', bd=4,
            command=lambda: bookService.deleteBook(value.get(), 'ID' if option.get() == 1 else 'TITLE'))
     .pack(side=TOP, padx=5, pady=10))


def rentBookMenu(window):
    newWindow = Toplevel(window)
    newWindow.title('Wypożycz')
    newWindow.geometry('400x250')

    Label(newWindow, text='ID', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    ID = Entry(newWindow, font=15)
    ID.pack(side=TOP, pady=15, padx=15)

    Label(newWindow, text='Książki (po przecinku bez spacji)', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    books = Entry(newWindow, font=15)
    books.pack(side=TOP, pady=15, padx=15)

    Button(newWindow, text='Zatwierdź', font=('Arial', 13), relief='raised', bd=4,
           command=lambda: bookService.bookRental(ID.get(), *(books.get().split(',')))).pack(side=TOP, padx=5)


def returnBookMenu(window):
    newWindow = Toplevel(window)
    newWindow.title('Zwróć')
    newWindow.geometry('400x250')

    Label(newWindow, text='ID', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    ID = Entry(newWindow, font=15)
    ID.pack(side=TOP, pady=15, padx=15)

    Label(newWindow, text='Książki (po przecinku bez spacji)', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    books = Entry(newWindow, font=15)
    books.pack(side=TOP, pady=15, padx=15)

    Button(newWindow, text='Zatwierdź', font=('Arial', 13), relief='raised', bd=4,
           command=lambda: bookService.returnBook(ID.get(), *(books.get().split(',')))).pack(side=TOP, padx=5)


def addCustomerMenu(window):
    newWindow = Toplevel(window)
    newWindow.title('Dodaj klienta')
    newWindow.geometry('300x600')

    Label(newWindow, text='Imię Nazwisko', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    NAME = Entry(newWindow, font=15)
    NAME.pack(side=TOP, pady=15, padx=15)

    Label(newWindow, text='E-mail', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    EMAIL = Entry(newWindow, font=15)
    EMAIL.pack(side=TOP, pady=15, padx=15)

    Label(newWindow, text='Telefon', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    PHONE = Entry(newWindow, font=15)
    PHONE.pack(side=TOP, pady=15, padx=15)

    Label(newWindow, text='Ulica', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    STREET = Entry(newWindow, font=15)
    STREET.pack(side=TOP, pady=15, padx=15)

    Label(newWindow, text='Miasto', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    CITY = Entry(newWindow, font=15)
    CITY.pack(side=TOP, pady=15, padx=15)

    Label(newWindow, text='Kraj', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    COUNTRY = Entry(newWindow, font=15)
    COUNTRY.pack(side=TOP, pady=15, padx=15)

    Button(newWindow, text='Zatwierdź', font=('Arial', 13), relief='raised', bd=4,
           command=lambda: customerService.addCustomer(NAME.get(), EMAIL.get(), PHONE.get(),
                                                       STREET.get(), CITY.get(), COUNTRY.get())).pack(side=TOP, padx=5)


def delCustomerMenu(window):
    newWindow = Toplevel(window)
    newWindow.title('Usuń klienta')
    newWindow.geometry('250x170')

    Label(newWindow, text='ID/Imię_Nazwisko', font=('Arial Black', 15),
          relief='solid', bd=3, bg='#afafaf', fg='#323232').pack(side=TOP, fill=X)
    value = Entry(newWindow, font=15)
    value.pack(side=TOP, pady=15, padx=15)

    optionFrame = Frame(newWindow)
    optionFrame.pack(side=TOP)
    option = IntVar(value=1)
    Radiobutton(optionFrame, text='ID', variable=option, value=1, font=('Arial', 10)).pack(side=LEFT)
    Radiobutton(optionFrame, text="Imię_Nazwisko", variable=option, value=2, font=('Arial', 10)).pack(side=RIGHT)

    (Button(newWindow, text='Zatwierdź', font=('Arial', 13), relief='raised', bd=4,
            command=lambda: customerService.deleteCustomer(value.get(), 'ID' if option.get() == 1 else 'NAME'))
     .pack(side=TOP, padx=5, pady=10))


def displayData(window, csv_file):
    newWindow = Toplevel(window)
    newWindow.title(csv_file)
    newWindow.geometry('900x350')

    data = additionalFun.loadData(csv_file)
    data2 = [', '.join(additionalFun.getFieldnames(csv_file))]
    for row in data:
        data2.append(', '.join(row.values()))
    text_widget = ScrolledText(newWindow, wrap=WORD, width=100, height=20)
    text_widget.insert(END, '\n'.join(data2))
    text_widget.pack(padx=10, pady=10)
    newWindow.mainloop()
