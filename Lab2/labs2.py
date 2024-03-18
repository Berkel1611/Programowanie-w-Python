#### Zadanie 1
## Poniżej masz 3 zbiory genów, 3 różnych pacjentów chorych na różne choroby
## Odpowiedz na poniższe pytania:
## a) Które elementy/geny są wspólne dla wszystkich pacjentów?
## b) Jakie elementy/geny są wspólne dla 2 pacjentów?
## c) Jakie elementy/geny występują wyłącznie w przypadku 1 choroby?
#
# set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                 'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
#                 'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
#                 'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])
# print('Wspólne dla wszystkich:')
# print(set_gene1 & set_gene2 & set_gene3)
#
# print('Wspólne dla 1 i 2:')
# print(set_gene1 & set_gene2)
# print('Wspólne dla 2 i 3:')
# print(set_gene2 & set_gene3)
# print('Wspólne dla 1 i 3:')
# print(set_gene1 & set_gene3)
#
# print('Tylko dla 1:')
# print(set_gene1 - set_gene2 - set_gene3)
import math

# ##########Zadanie 2
# ### Sprawdź czy w poniższym zbiorze występuje gen 'FGFR4' oraz 'FGERA4', jeśli tak to wskaż index
# ### genu na liście
#
# lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                 'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']
# flag = 0
# print('Indeksy genu \'FGFR4\':')
# for i in range(0, len(lista_gene1)):
#     if lista_gene1[i] == 'FGFR4':
#         flag = 1
#         print(i)
# if flag == 0:
#     print('Brak!')
# flag = 0
# print('Indeksy genu \'FGERA4\':')
# for i in range(len(lista_gene1)):
#     if lista_gene1[i] == 'FGERA4':
#         flag = 1
#         print(i)
# if flag == 0:
#     print('Brak!')

#####Zadanie 3
## Przekopiuj dowolny ale długi fragment tekstu ze strony:
## http://www.national-geographic.pl/ludzie/dziennikarka-kontra-komputer-kto-napisze-lepszy-tekst
## sprawdź:
## a) ile razy w tekście występuje słowo Emma
## b) zamień całość tekstu na duże litery
## c) wstaw poszczególne wyrazy jako elementy listy
## d) ile zdań jest w analizowanym tekście?
#
# str = 'Emma i ja dostałyśmy instrukcje, by o 9:30 napisać o oficjalnych danych dotyczących zatrudnienia w Wielkiej Brytanii i wysłać nasze wersje do redaktora. Byłam przekonana, że Emma będzie ode mnie szybsza, ale miałam też szczerą nadzieję, że to ja będę lepsza. Twórca Emmy, start-up o nazwie Stealth, nazywa ją „niezależną sztuczną inteligencją” zaprojektowaną, by świadczyć profesjonalne usługi, takie jak badania i analiza. Odkąd w modzie są prognozy, że sztuczna inteligencja (ang. artificial intelligence, AI) zastąpi pracowników biurowych, w tym również dziennikarzy, chciałam to sprawdzić na własnej skórze. Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki).'
# print('Słowo \'Emma\' występuje {} razy.'.format(str.count('Emma')))
# str = str.upper()
# print(str)
# lista = str.split('. ')
# print('Zdań w tekscie jest {}.'.format(len(lista)))

########Zadanie 4
## Sprawdź czy dowolnie podana przez użytkownika liczba jest parzysta czy nieparzysta
#
# a = int(input('Podaj liczbę: '))
# if a % 2 == 0:
#     print('Liczba {} jest parzysta.'.format(a))
# else:
#     print('Liczba {} jest nieparzysta.'.format(a))

########Zadanie 5
## W zależności od procentu uzyskanych punktów z kolokwium z Python'a
## student uzyskuje określoną ocenę końcową z laboratorium
## np 50%-60% to 3.0, 61%-70% to 3.5, ...., 91%-100% to 5.0 - if
## np 50% to 3.0, 61% to 3.5, ...., 91% to 5.0 - match
## Korzystając z instrukcji match, napisz program który będzie wyznaczał ocenę studenta na podstawie uzyskanych punktów (max 15pkt)
#
# pts = int(input('Podaj uzyskane punkty: '))
# per = (pts/15.0)*100
# print('Twoja ocena to:')
# if 50 <= per < 61:
#     print(3.0)
# elif 61 <= per < 71:
#     print(3.5)
# elif 71 <= per < 81:
#     print(4.0)
# elif 81 <= per < 91:
#     print(4.5)
# elif 91 <= per <= 100:
#     print(5.0)
# else:
#     print('Nie zdałeś!')

# # #Zadanie 6
### Napisz skrypt, ktory obliczy sume ciagu: 1+1/2+1/3+...+1/n korzystając z pętli for
### Zmienna wejsciowa m jest dowolnia, m-parametr wprowadzany jako dane wejsciowe przez uzytkownika (użyj input)
### Write a program that calculates the sum of the sequence: 1+1/2+1/3+...+1/m using the for loop.
### The input variable m is arbitrary. The m-parameter is provided as input by the user (use input).
#
# m, suma = int(input('Podaj liczbę całkowitą: ')), 0
# for i in range(1, m+1):
#     suma += (1/i)
# print('Suma: {}'.format(suma))

###### Zadanie 7
###### Calculate the root of the numbers from 1 to 10 using the while loop
###### Oblicz pierwiastek liczb od 1 do 10 korzystając z pętli while
#
# import math
# i = 1
# while i < 11:
#     print('Pierwiastek z {} to {}.'.format(i, math.sqrt(i)))
#     i += 1

###### Task 8
###### Write a program which takes 3 digits: a, b, c as input and
###### calculate the roots of a quadratic equation ax^2 + bx + c = 0
#
# print('Podaj 3 cyfry: ')
# a, b, c = int(input()), int(input()), int(input())
# delta = (b**2) - 4*a*c
# if delta == 0:
#     print('Jest jeden pierwiastek: {}'.format(-b / (2*a)))
# elif delta > 0:
#     print('Są dwa pierwiastki: {} i {}'.format((-b - math.sqrt(delta))/(2*a), (-b + math.sqrt(delta))/(2*a)))
# else:
#     print('Brak pierwiastków.')

###### Task 9
##### Write a program, which will find all such numbers between 1 and 1000 (both included) such
##### that each digit of the number is an even number the numbers obtained should be printed
### in a comma-separated sequence on a single line

# for i in range(1, 1000):
#     if i % 2 == 0:
#         print('{}, '.format(i), end='')
# print(1000)
