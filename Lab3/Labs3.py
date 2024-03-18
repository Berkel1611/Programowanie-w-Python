# # ################################ Task 1
## Write a program using if statement, for loop, break(), continue() which takes 2 digits: x, y as input and
###### calculate multiplication x*y. The program stops working if x or y is equal to 0.
## Korzystając z instrukcji sterujących napisz program który będzie wczytywał kolejno z klawiatury 2 liczby,
## a następnie obliczał i wyświetlał na ekranie iloczyn wprowadzonych przez użytkownika liczb,
## program kończy działanie jeżeli uzytkownik wprowadzi cyfrę 0. Użytkownik może wykonać obliczenia tylko na
## liczbach całkowitych (wstaw odpowiedni warunek).
#
# while True:
#     x = input('Podaj 1. liczbę: ')
#     if x == '0':
#         break
#     y = input('Podaj 2. liczbę: ')
#     if y == '0':
#         break
#     if x.isdigit() and y.isdigit():
#         print('Iloczyn: {}'.format(int(x)*int(y)))
#     else:
#         print('Zły typ!')

## # ################################ Task 2
## Napisz program, który wyświetli twoje imię i nazwisko jeżeli użytkownik poda
## właściwe hasło, jedno z 2 do wyboru, (hasła są przechowywane w krotce)
#
# hasla = ('1234', '4321')
# while True:
#     inp = input('Podaj hasło: ')
#     if inp == '1234' or inp == '4321':
#         print('Bartłomiej Koźluk')
#         break
#     else:
#         print('Niepoprawne hasło.')

################################## Task 3
## Generate list with 100 random numbers (integer type)
## Ascending sort these odd numbers and print only odd numbers from list.

## Wygeneruj listę złożoną z 100 liczb całkowitych parzystych i nieparzystych
## wypisz wszystkie liczby parzyste z tablicy liczby, od najmniejszej do największej.
## Do losowania liczb wykorzystaj moduł random patrz przykład poniżej
#
# import random
# lista = random.sample(range(1000), 100)
# lista = sorted(lista)
# for el in lista:
#     if el % 2 == 0:
#         print('{} '.format(el), end='')

############### Task 4
## Uprość kod z Zadania 2 korzystając w w/w struktur
## Simplify the code from Task 2 using a one line if/else statement
#
# hasla = ('1234', '4321')
# inp = input('Podaj hasło: ')
# print('Bartłomiej Koźluk') if inp == '1234' or inp == '4321' else print('Niepoprawne hasło.')

#################### Task 5
## Write a function that calculates the quotient of 3 even numbers
## Utwórz funkcje która obliczy iloraz 3 parzystych liczb, użyj "one line statement"
#
# def div_numbers(x, y, z):
#     return (x % 2 == 0 and y % 2 == 0 and z % 2 == 0) and x/y/z or 0

# ########################## Task 6
# Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
# z funkcji lambda połącz kolejne litery w jeden wyraz (swoje imie)
#
# lista = list('Bartłomiej')
# imie = lambda lista: ''.join(lista)
# print(imie(lista))

# ########################## Task  7
# Przypisz do zmiennej wartość która będzie twoim imieniem i nazwiskiem następnie korzystając
# z funkcji lambda rozdziel wyraz na poszczegolne wyrazy, a potem wyrazy na litery
# użyj funkcji list i metody split - dla zmiennych typu string
#
# dane = 'Bartłomiej Koźluk'
# podziel_spacjami = lambda str: str.split(" ")
# podziel_na_litery = lambda str: list(str)
# imie_nazwisko = podziel_spacjami(dane)
# imie = podziel_na_litery(imie_nazwisko[0])
# nazwisko = podziel_na_litery(imie_nazwisko[1])
# print(imie_nazwisko)
# print(imie)
# print(nazwisko)

# ########################## Task 8
# # Utwórz funkcję która w dowolnym wyrazie (1 argument funkcji)
# # znajdzie dowolną literę (2 argument funkcji)
## użyj lammbda()
#
# ile_wystapien = lambda str, a: list(str).count(a)
# print(ile_wystapien('Python', 'y'))

# ########################## Task 9
## Utwórz dwie listy, do każdej z nich niezależnie zapisuj odpowiednio
## podawane przez użytkowników login (pierwsza lista) i hasło (druga lista),
## operacja zapisu jest powtarzana aż do momentu wpisania przez użytkownika "STOP"
## użyj break, continue, enumerate().
## Następnie login-y i hasła zapisz do słownika (login to klucz słownika).
#
# lista1 = []
# lista2 = []
# while True:
#     login = input('Podaj login: ')
#     if login == 'STOP':
#         break
#     haslo = input('Podaj hasło: ')
#     lista1.append(login)
#     lista2.append(haslo)
# slownik = {}
# for indeks, login in enumerate(lista1):
#     slownik[login] = lista2[indeks]
# print(slownik)

# ########################## Task 10  - Module in Python
# # # Zmodyfikuj poprzednie zadanie, tworząc a następnie importując moduł
# # #Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # #Utwórz funkcje Pion: która rysuje gwiazdeki pionowo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # obie funkcje są z modułu o nazwie stars
# # Korzystając z modułu stars i funkcji Pion Poziom wypisz litery: E, L

# import Task9
# import stars
# # E
# stars.Poziom(8)
# stars.Pion(1)
# stars.Poziom(8)
# stars.Pion(1)
# stars.Poziom(8)
# print()
# # L
# stars.Pion(4)
# stars.Poziom(8)

# ########################## Task 11
# # utwórz moduł o nazwie sil, w którym znajdzie się funkcja silnia (użyj lammbda), a następnie korzystając z
# modułu sil, oblicz symbol Newtona dla dowolnych 2 liczb wskazanych przez
# użytkownika(http://www.fizykon.org/wzory/wzory_matem_kombinatoryka.htm)
#
# import sil
# symbol_Newtona = sil.silnia(7)/(sil.silnia(5)*sil.silnia(7-5))
# print(symbol_Newtona)

# ########################## Task 12
# # Write a script to filter out only the even items from a list (i.e. made from range(1, 100))
# # using filter() and lambda functions.
# #  The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# print(list(filter(lambda x: x % 2 == 0, range(1, 100))))

# ########################## Task 13
#### Write a script, using reduce(), which will multiply elements in range (1, 100)
#
# from functools import reduce
# print(reduce(lambda x, y: x * y, range(1, 100)))

# ########################## Task 14
### Write a program which will find all such numbers which are
### divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included)
#
# print(list(filter(lambda x: x % 7 == 0 and x % 5 != 0, range(2000, 3201))))