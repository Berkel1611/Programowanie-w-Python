##################################### Zadanie 0   na rozgrzewkę ##################
## Utwórz funkcję o nazwie "Rozprawka.py", która będzie wyświetlała,
## na ekranie napis "to poprostu jest wspaniałe i niesamowite, musisz to zobaczyć",
## następnie używając w/w funkcji napisz tekst reklamujący, opisujący jeden z 7 Cudów świata gdzie
## wywołasz tą funkcję w tekście minimum 3 krotnie
#
# def Rozprawka():
#     print('To poprostu jest wspaniałe i niesamowite, musisz to zobaczyć.')
#
# Rozprawka()
# print('Największa z trzech piramid została wybudowania przez Cheopsa. Jej wysokość to 146 metrów, a długość boku podstawy liczy sobie ponad 230 metrów.')
# Rozprawka()
# print('Największa różnica pomiędzy długościami boków wynosi tylko 4,4 cm, a podstawa odbiega od poziomu o nie więcej niż 2,1 cm - to nadzwyczajne osiągnięcie inżynierskie.')
# Rozprawka()

## Zadanie 1
## Utwórz 1 funkcje wielu-zmiennych wejściowych, która obliczy wartość wyrażenia
## dla dowolnego jednego argumentu wejściowego, x^x
## dla dowolnych dwóch argumentów wejściowych  x^x,
## dla pozostałych przypadków wyświetli komunikat, że jest błąd.
#
# def power(*args):
#     if len(args) == 1:
#         return pow(args[0], args[0])
#     elif len(args) == 2:
#         return pow(args[0], args[1])
#     else:
#         return ('Jest błąd.')

######### Zadanie 2
## Wczytaj poniższy fragment tekstu opisujący komputer
## Napisz funkcję która ustali liczbę występujących w tym tekście wyrazów wskazanych przez użytkownika
## ciąg nazw i liczba wyszukiwanych wyrazów podanych przez użytkownika jest dowolna,
## niemniej w tekście są wyrazy o nazwach kluczowych i potencjalnie zawsze ważnych
## dla innych użytkowników np. komputera, skaner, uwzględnij je w wyszukiwaniu.
#
# text = 'Wczytywanie do komputera tekstów, ilustracji, fotografii, itp. jest '   \
#        'możliwe dzięki urządzeniom zewnętrznym zwanym skanerami. Skaner to ' \
#        'urządzenie umożliwiające wprowadzenie do komputera grafiki i tekstu. ' \
#        'Dzięki zamianie skanowanej płaszczyzny na postać cyfrową może ona zostać ' \
#        'wyświetlona na ekranie monitora i zapisana na dysku w odpowiednim formacie ' \
#        'oraz może zostać poddana komputerowej obróbce. Skanery dzielimy na dwie podstawowe ' \
#        'grupy: ręczne (np. czytniki kodów paskowych) oraz stacjonarne. Najpopularniejszym ' \
#        'typem skanerów są skanery stacjonarne płaskie, które umożliwiają skanowanie ' \
#        'dokumentów o formacie A3 lub A4 i ich pochodnych. Są one podłączane do ' \
#        'komputerów przez port równoległy, uniwersalną magistralę szeregową lub sterownik SCSI.'
# print(text)
#
#
# def countWords(*args):
#     print('komputer: {}'.format(text.count('komputer')))
#     print('skaner: {}'.format(text.count('skaner')))
#     for i in args:
#         if i in text:
#             print('{}: {}'.format(i, text.count(i)))
#         else:
#             print('Brak takich wyrazów.')
#
#
# countWords('port', 'dzięki')

############ Zadanie 3 #################
## Utwórz funkcję o nazwie "SredniaLiczb.py", która wczyta N dowolnych liczb
## i obliczy średnią z w/w liczb, podane przez użytkownika liczby przypisz do listy
#
# def SredniaLiczb(*args):
#     if not args:
#         return 'Brak argumentów!'
#     return sum(args)/len(args)
#
# lista = []
# while True:
#     inp = input()
#     if inp == 'stop':
#         break
#     if inp.isdigit():
#         lista.append(int(inp))
# print(SredniaLiczb(*lista))

############ Zadanie ##################
## Utwórz funkcję o nazwie "ZdanieRozdziel.py", która wczyta od użytkownika pewien dowolny tekst,'
## a następnie podzieli go na zdania (zakładamy, że jednoznacznie kropka rozdziela zdania)'
## funkcja w zależności od ustawionych kolejnych parametrów wejściowych funkcji
## (ustaw domyślnie argumenty wejściowe: True),
## może ale nie musi wyświetlić następujące informacje:
## ile w każdym zdaniu jest fragmentów rozdzielonych przez określony znak np. ',', ';'
## (domyślnie argument wejściowy to przecinek: ',')
## ile w każdym zdaniu jest wyrazów (zakładamy, że spacja oddziela wyrazy w zdaniu)
## użyj odpowiednich metod dla zmiennych typu string np. split do rozdzielenia elementów: x = ‘blue,red,green’,   x.split(“,”)
#
# def ZdanieRozdziel(tekst, separator=',', pokaz_ilosc_fragmentow=True, pokaz_ilosc_wyrazow=True):
#     zdania = tekst.split('.')
#
#     for zdanie in zdania:
#         if zdanie.strip() == '':
#             continue
#
#         print('\"{}\"'.format(zdanie))
#         if pokaz_ilosc_fragmentow:
#             print('Ilość fragmentów w zdaniu: {}'.format(len(zdanie.split(separator))))
#         if pokaz_ilosc_wyrazow:
#             wyrazy = zdanie.split(" ")
#             print('Ilość wyrazów w zdaniu: {}'.format(len(zdanie.split(" "))))
#
# ZdanieRozdziel(input(), ',')

########### Zadanie 6  ########################
## Zdefiniuj funkcję "CiagGometryczny.py", która dla podanych trzech parametrów:
## n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie: 1),
## q=wartość iloczynu ciągu geometrycznego (domyślnie: 2)
## zwróci w zależności od ustawianych parametrów funkcji
## a) wartość n-tego elementu ciągu geometrycznego
## b) sumę elementów ciągu geometrycznego
#
# def CiagGeometryczny(n, a1=1, q=2):
#     if n == 1:
#         return a1
#     else:
#         nth_element = a1 * pow(q, n-1)
#         sum_of_n_elements = a1 * ((1 - pow(q, n))/(1-q))
#         return nth_element, sum_of_n_elements

# ########################## Zadanie 7
## Zaprojektuj program służący do obsługi prostej bazy danych dla sklepu z
## dowolnej branży o różnej liczbie pracowników. Program zapisuje do kolejnych list
## liczby produktów dostarczonych w danym dniu (nazwa listy odpowiada nazwie towaru)
## liczba towarów powinna być zapamiętana

# Przetestuj swój program dla różnych przypadków dostawy towaru
# Pamiętaj że asortyment sprzedawanego towaru ulega zmianie
# Użyj kwargs


#baza_danych = {}

#
# def dodaj_dostawe(**kwargs):
#     for nazwa_towaru, ilosc in kwargs.items():
#         if nazwa_towaru in baza_danych:
#             baza_danych[nazwa_towaru] += int(ilosc)
#         else:
#             baza_danych.update({nazwa_towaru: ilosc})
#
#
# def usun_towary(**kwargs):
#     for nazwa_towaru, ilosc in kwargs.items():
#         if nazwa_towaru in baza_danych:
#             if baza_danych[nazwa_towaru] >= ilosc:
#                 baza_danych[nazwa_towaru] -= int(ilosc)
#             if baza_danych[nazwa_towaru] == 0:
#                 baza_danych.pop(nazwa_towaru)
#         else:
#             return 'Za mała ilość towaru!'
#     else:
#         return 'Brak towaru w bazie danych!'
#
#
# dodaj_dostawe(jablka=100, ziemniaki=150, pieczywo=20)
# print(baza_danych)
# usun_towary(jablka=50, ziemniaki=100)
# print(baza_danych)

# ########################## Zadanie 8
## W module pole_prostokata.py
## Zdefiniuj funkcję która obliczy pole powierzchni prostokąta
## W module pole_trojkata.py
## Zdefiniuj funkcję która obliczy pole powierzchni trójkąta
# W module pola.py
## Korzystając z modułów pole_prostokata i pole_trojkata
## napisz funkcję która ma możliwość obliczenia pola prostokąta, trójkąta i kwadratu
## Użyj zmiennych globals, utwórz moduł globals.py w którym będą przechowywane
## domyślne wartości dla boków prostokąta, trójkąta, kwadratu (równe 1)
#
# import pola
#
# pola.oblicz_pola(prostokat=False, kwadrat_bok=4, trojkat_podstawa=4, trojkat_wysokosc=3)

# ########################## Zadanie 9
## Zdefiniuj funkcję wyższego rzędu która ma możliwość obliczenia
## pole powierzchni prostokąta i pola powierzchni trójkąta
## Nie modyfikując zawartości w/w funkcji, użyj dekoratora i dodaj możliwość
## obliczenia pola kwadratu
#
#
# def pole_prostokata(a, b):
#     return a*b
#
#
# def pole_trojkata(a, h):
#     return a*h/2
#
#
# def dodaj_pole_kwadratu(func):
#     def wrapper(a, b):
#         func(a, b)
#         print('Pole kwadratu: {}'.format(a*a))
#     return wrapper
#
#
# @dodaj_pole_kwadratu
# def oblicz_pola(a, b):
#     print('Pole prostokąta: {}'.format(pole_prostokata(a, b)))
#     print('Pole trójkąta: {}'.format(pole_trojkata(a, b)))
#
#
# oblicz_pola(2, 3)

# ########################## Zadanie 10
## Utwórz funkcję która umożliwia logowanie na serwer
## Ma dwa argumenty wejściowe:
## user i password (domyślne wartości odpowiednio: 'edek2003', 'Wsx123')
## a) nie modyfikując zawartości w/w funkcji, użyj dekoratora i dodaj dodatkowe
## pola tj. host, port
## b) nie modyfikując zawartości w/w funkcji, użyj dekoratora i  daj możliwość
## wprowadzania dodatkowych innch pól użytkownikowi (wprowadzane jako słownik
##  np. {'data_base': 'https://pl.wikipedia.org'})
# slownik = {}
#
#
# def dodaj_wiecej_argumentow(func):
#     def wrapper(user, password, **kwargs):
#         func(user, password)
#         slownik.update(kwargs)
#     return wrapper
#
#
# def dodaj_argumenty(func):
#     def wrapper(user, password, host='Brak', port='Brak'):
#         func(user, password)
#         slownik['host'] = host
#         slownik['port'] = port
#     return wrapper
#
#
# @dodaj_wiecej_argumentow
# @dodaj_argumenty
# def logowanie(user='edek2003', password='Wsx123'):
#     slownik['user'] = user
#     slownik['password'] = password
#
#
# logowanie(user='Berkel1611', password='Logika106', host='cośtam', dane='Wikipedia')
# print(slownik)

# ########################## Zadanie 11
## Zdefiniuj funkcję ciag_gometryczny, która dla podanych trzech parametrów:
## n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie: 1),
## q=wartość iloczynu ciągu geometrycznego (domyślnie: 2)
## zwróci w zależności od ustawianych parametrów funkcji
## a) wartość n-tego elementu ciągu geometrycznego

## Następnie korzystając z dekoratora udoskonal swoją funkcję,
## dodaj możliwość obliczenia sumy elementów ciągu geometrycznego
#
# def dodaj_sume_ciagu(func):
#     def wrapper(n, a1=1, q=2):
#         n_ty = func(n, a1, q)
#         sum_of_n_elements = a1 * ((1 - pow(q, n)) / (1 - q))
#         return n_ty, sum_of_n_elements
#     return wrapper
#
#
# @dodaj_sume_ciagu
# def CiagGeometryczny(n, a1=1, q=2):
#     if n == 1:
#         return a1
#     else:
#         nth_element = a1 * pow(q, n-1)
#         return nth_element
#
#
# print(CiagGeometryczny(9))
