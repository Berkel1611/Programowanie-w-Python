from tkinter import *
import UI


def main():
    window = Tk()
    window.title("Biblioteka")
    window.geometry("700x950")
    window.config(bg='#414141')

    # main label
    title = Label(window, text="SYSTEM BIBLIOTECZNY", fg='#1f1f1f',
                  font=('Arial Black', 35), relief='ridge', bd=10, bg='#b5b5b5')
    title.pack(side=TOP, fill=X)

    # book service menu
    bookFrame = Frame(window, bd=10, relief='ridge', bg='#b5b5b5')
    bookFrame.pack(side=TOP, fill=X, pady=15, padx=15)
    bookMan = Label(bookFrame, text='ZARZĄDZANIE KSIĄŻKAMI', fg='#1f1f1f',
                    font=('Arial Black', 20), bg='Silver', bd=3, relief=SOLID)
    bookMan.pack(side=TOP)
    # add book button
    (Button(bookFrame, text='Dodaj książkę', font=('Arial Black', 15),
            relief='raised', bd=7, bg='#afafaf', fg='#323232', command=lambda: UI.addBookMenu(window))
     .pack(side=TOP, pady=5, padx=15, fill=X))
    # delete book button
    Button(bookFrame, text='Usuń książkę', font=('Arial Black', 15), relief='raised', bd=7, bg='#afafaf', fg='#323232',
           command=lambda: UI.delBookMenu(window)).pack(side=TOP, pady=5, padx=15, fill=X)
    # rent book button
    (Button(bookFrame, text='Wypożycz książkę', font=('Arial Black', 15),
            relief='raised', bd=7, bg='#afafaf', fg='#323232', command=lambda: UI.rentBookMenu(window))
     .pack(side=TOP, pady=5, padx=15, fill=X))
    # return book button
    (Button(bookFrame, text='Zwróć książkę', font=('Arial Black', 15),
            relief='raised', bd=7, bg='#afafaf', fg='#323232', command=lambda: UI.returnBookMenu(window))
     .pack(side=TOP, pady=5, padx=15, fill=X))

    # customer service menu
    customerFrame = Frame(window, bd=10, relief='ridge', bg='#b5b5b5')
    customerFrame.pack(side=TOP, fill=X, padx=15)
    custMan = Label(customerFrame, text='ZARZĄDZANIE KLIENTAMI', fg='#1f1f1f',
                    font=('Arial Black', 20), relief=SOLID, bg='Silver', bd=3)
    custMan.pack(side=TOP)
    # add customer button
    (Button(customerFrame, text='Dodaj klienta', font=('Arial Black', 15),
            relief='raised', bd=7, bg='#afafaf', fg='#323232', command=lambda: UI.addCustomerMenu(window))
     .pack(side=TOP, pady=5, padx=15, fill=X))
    # delete customer button
    (Button(customerFrame, text='Usuń klienta', font=('Arial Black', 15),
            relief='raised', bd=7, bg='#afafaf', fg='#323232', command=lambda: UI.delCustomerMenu(window))
     .pack(side=TOP, pady=5, padx=15, fill=X))

    # displaying the contents of csv files
    displayFrame = Frame(window, bd=10, relief='ridge', bg='#b5b5b5')
    displayFrame.pack(side=TOP, fill=X, padx=15, pady=15)
    # display books button
    (Button(displayFrame, text='Wyświetl książki', font=('Arial Black', 15),
            relief='raised', bd=7, bg='#afafaf', fg='#323232', command=lambda: UI.displayData(window, 'book.csv'))
     .pack(side=TOP, pady=5, padx=15, fill=X))
    # display customers button
    (Button(displayFrame, text='Wyświetl klientów', font=('Arial Black', 15),
            relief='raised', bd=7, bg='#afafaf', fg='#323232', command=lambda: UI.displayData(window, 'customer.csv'))
     .pack(side=TOP, pady=5, padx=15, fill=X))
    # display addresses button
    (Button(displayFrame, text='Wyświetl adresy', font=('Arial Black', 15),
            relief='raised', bd=7, bg='#afafaf', fg='#323232', command=lambda: UI.displayData(window, 'address.csv'))
     .pack(side=TOP, pady=5, padx=15, fill=X))

    window.mainloop()


if __name__ == "__main__":
    main()

# C:\Users\Radek\OneDrive\Pulpit\Studia UWB\Programowanie w języku Python\Zadania\Library
