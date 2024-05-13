from tkinter import *  # standard Python interface to the Tcl/Tk GUI toolkit
import requests  # package allows you to send HTTP requests
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo, showerror, showwarning

# ############Zadanie 1 ######################
# Kalkulator: utwórz 2 kontrolki typu edit tekst, 1 przycisk "ok" i radiobutton
# po wcisnieciu przycisku program powinien wykonywać 4 dowolne operacje matematyczne na liczbach wpisanych przez użytkownika
# w kontrolkach edit
# Obsłuż potencjalne błędy wpisując własny komentarz: np. TypeError
# Do wyswietlania komunikatów użyj okienek komunikacyjnych

# def calc():
#     result = 0
#     try:
#         if var.get() == 1:
#             result = float(entry1.get()) + float(entry2.get())
#         elif var.get() == 2:
#             result = float(entry1.get()) - float(entry2.get())
#         elif var.get() == 3:
#             result = float(entry1.get()) * float(entry2.get())
#         elif var.get() == 4:
#             result = float(entry1.get()) / float(entry2.get())
#     except ValueError as e:
#         showerror("ValueError:", e)
#     except ZeroDivisionError as z:
#         showerror("ZeroDivisionError:", z)
#     text3.config(text="Wynik: "+str(result))
#
#
# window = Tk()
# window.title("Kalkulator")
# window.geometry("300x200")
#
# Label(window, text='Podaj 1. liczbę: ').grid(row=1, column=1)
# Label(window, text='Podaj 2. liczbę: ').grid(row=2, column=1)
#
# entry1 = Entry(window)
# entry1.grid(row=1, column=2)
# entry2 = Entry(window)
# entry2.grid(row=2, column=2)
#
# var = IntVar()
# Radiobutton(window, text='+', variable=var, value=1).grid(row=1, column=3)
# Radiobutton(window, text='-', variable=var, value=2).grid(row=2, column=3)
# Radiobutton(window, text='*', variable=var, value=3).grid(row=1, column=4)
# Radiobutton(window, text='/', variable=var, value=4).grid(row=2, column=4)
#
# text3 = Label(window, text="Wynik: 0")
# text3.grid(row=3, column=2)
#
# Button(window, text="Enter", command=calc).grid(row=4, column=2)
# window.mainloop()

# # ########## Zadanie 2
# # Okres świąt to również zwiększony czas brania kredytów przez konsumentów
# # Zaprojektuj prosty interfejs który obliczy ratę kredytu 1000-10000zł zgodnie ze wzorem:
# # rata =(K*q^n*(1-q))/(1-q^n) gdzie: q = 1+p/100
# # K - kwota udzielonego kredytu
# # n - liczba okresów  (n=1,2,3) np. mc
# # p - stopa procentowa (p=const, wpisz jako ułamek)
# # Uwaga jak wiadomo emocje można wyrazić za pomocą kolorów
# # A zatem postaraj się uzależnić kolor wyświetlanej kwoty raty do spłaty od potencjalnych emocji klienta banku na
# # widok ile musi oddać bankowi.
#
# def obliczRate():
#     wynik = 0
#     try:
#         k, n, p = float(kwota.get()), float(okresy.get()), float(stopa.get())
#         q = 1+p/100
#         wynik = (k*pow(q, n)*(1-q))/(1-pow(q, n))
#     except ZeroDivisionError as z:
#         showerror("ZeroDivisionError", str(z))
#     except ValueError as e:
#         showerror("ValueError", str(e))
#     rata = Label(window, text=round(wynik, 2), fg=kolorRaty(wynik))
#     rata.grid(row=6, column=2)
#
#
# def kolorRaty(r):
#     if r < 600:
#         return "green"
#     elif 600 <= r < 900:
#         return "yellow"
#     elif 900 <= r < 1200:
#         return "orange"
#     return "red"
#
#
# window = Tk()
# window.title("Jaka rata?")
# window.geometry("250x150")
#
# Label(window, text='Kwota kredytu: ').grid(row=1, column=1)
# Label(window, text='Liczba okresów: ').grid(row=2, column=1)
# Label(window, text='Stopa procentowa: ').grid(row=3, column=1)
#
# kwota = Entry(window)
# kwota.grid(row=1, column=2)
# okresy= Entry(window)
# okresy.grid(row=2, column=2)
# stopa= Entry(window)
# stopa.grid(row=3, column=2)
#
# Button(window, text="Oblicz", command=obliczRate).grid(row=4, column=2)
#
# window.mainloop()

# # #########Zadanie 3
# # Pewna firma zleciła Ci wykonie badania ankietowego dotyczącego kupowanych przez konsumentów produktów na święta:
# # Do każdego pytania utwórz 2-3 kontrolki wielokrotnego wyboru z następującymi opcjami do wyboru.
# # np. Co najczęściej kupujesz dla rodziny w prezencie?
# # opcja 1: agd
# # opcja 2: kosmetyki
# # opcja 3: odzież

# def display():
#     a, k, o = "", "", ""
#     if var1.get() == 1:
#         a = "agd"
#     if var2.get() == 1:
#         k = " kosmetyki"
#     if var3.get() == 1:
#         o = " odzież"
#     text.config(text="{}{}{}".format(a, k, o))
#
#
# def confirm():
#     showinfo("Sukces!", "Dziękujemy za udział w ankiecie. :)")
#     window.quit()
#
#
# window = Tk()
# window.title("Ankieta")
# window.geometry("270x150")
#
# Label(window, text="Co najczęściej kupujesz dla rodziny w prezencie?", bg="yellow", fg="black").grid(row=0, column=0)
#
# var1 = IntVar()
# Checkbutton(window,
#             text="1. AGD",
#             bg="magenta",
#             fg="black",
#             variable=var1,
#             command=display).grid(row=1, sticky=W)
# var2 = IntVar()
# Checkbutton(window,
#             text="1. Kosmetyki",
#             bg="magenta",
#             fg="black",
#             variable=var2,
#             command=display).grid(row=2, sticky=W)
# var3 = IntVar()
# Checkbutton(window,
#             text="1. Odzież",
#             bg="magenta",
#             fg="black",
#             variable=var3,
#             command=display).grid(row=3, sticky=W)
#
# text = Label(window)
# text.grid(row=4, column=0)
#
# Button(window, text="Zatwierdź", command=confirm).grid(row=6, column=0)
# window.mainloop()
