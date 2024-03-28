import fnmatch
import os

########################## Zadanie 1 #########################
## Utwórz funkcję która będzie zmieniała bieżący katalog dyskowy na inny wskazany przez
## użytkownika (nazwa ścieżki do katalogu to argument wejściowy funkcji)
## oraz będzie wyświetlała zawartość wskazanego przez użytkownika katalogu.


def change_actual_path(path):
    print(os.getcwd())
    os.chdir(path)
    print(os.listdir('.'))

########################## Zadanie 2 #########################
## Korzystając z utworzonej funkcji napisz funkcję która będzie zmieniała bieżący katalog
## dyskowy na inny wskazany przez użytkownika oraz będzie wyświetlała zawartość wskazanego przez
## użytkownika katalogu.
## Przetestuj działanie programu dla natepującego przypadku:
## program działa tylko wówczas gdy użytkownik odpowie "yes" na pytanie:
## "Czy mam zmienić katalog?", zastosuj pętle while True(zmuś użytkownika :) do wpisania "yes")
#
#
# while True:
#     print('Czy mam zmienić katalog?')
#     answer = input()
#     if answer == 'yes':
#         change_actual_path(input('Podaj ścieżkę: '))
#         break

########################## Zadanie 3 #######################
## W swoim folderze roboczym (w którym masz plik programu) utworz folder o nazwie Dokument,
## do w/w folderu przekopiuj lub utwórz 3 dowolne pliki z rozszerzeniem *.doc np. (Lab1.doc, Lab2.doc, Lab3.doc)
## następnie wykonaj następujące zadania:
## a) korzystając z instrukcji Pythona wyświetl wszystkie pliki znajdujące się folderze roboczym
## b) korzystając z metod Pythona i (pętli lub funkcji filter) wyświetl tylko pliki z rozszerzeniem *.doc znajdujące się folderze roboczym
#
#
# # os.makedirs(os.path.join(os.getcwd(), 'Dokument'))
# os.chdir(os.path.join(os.getcwd(), 'Dokument'))
# # f1 = open('Lab1.doc', 'w')
# # f2 = open('Lab2.doc', 'w')
# # f3 = open('Lab3.txt', 'w')
# # f1.close()
# # f2.close()
# # f3.close()
# print(list(filter(lambda x: fnmatch.fnmatch(x, '*.doc'), os.listdir())))

########################## Zadanie 4 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze 2 katalogi:
## StudentDoc, StudentObrazy, do w/w folderów zapisz w każdym z nich 2 dowolne
## pliki odpowiednio tekstowe i graficzne, a następnie wyświetl zawartość poszczególnych
## folderów podaj rozmiar każdego pliku
#
#
# # os.makedirs('StudentDoc')
# # os.makedirs('StudentObrazy')
#
# path = os.getcwd()
# os.chdir(os.path.join(path, 'StudentObrazy'))
# f = open('zdj.jpg', 'a')
# f.close()
# os.chdir(os.path.join(path, 'StudentDoc'))
# f1 = open('plik.txt', 'a')
# f1.close()
#
# print(os.listdir())
# print('Rozmiar pliku: {}'.format(os.path.getsize(os.path.join(os.getcwd(), 'plik.txt'))))
#
# os.chdir(os.path.join(path, 'StudentObrazy'))
# print(os.listdir())
# print('Rozmiar pliku: {}'.format(os.path.getsize(os.path.join(os.getcwd(), 'zdj.jpg'))))

########################## Zadanie 5 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze katalog,
## a następnie zmień nazwę katalogu na inną, dowolną.
#
#
# # os.makedirs('Folder')
# os.rename(os.path.join(os.getcwd(), 'Folder'), os.path.join(os.getcwd(), 'Folderek'))

########################## Zadanie 6 ########################
# # Utwórz trzy listy, zapisz, usuń a następnie odczytaj z pliku listy, użyj pickle


import pickle

# lista1 = [1, 2, 3, 4]
# lista2 = [3, 4, 5, 6]
# lista3 = [5, 6, 7, 8]
# f = open('Listy.txt', 'wb')
# pickle.dump(lista1, f)
# pickle.dump(lista2, f)
# pickle.dump(lista3, f)
# f.close()
# del lista1, lista2, lista3
#
# f2 = open('Listy.txt', 'rb')
# lista4 = list(pickle.load(f2))
# lista5 = list(pickle.load(f2))
# lista6 = list(pickle.load(f2))
# f2.close()
# print(lista4)
# print(lista5)
# print(lista6)

########################## Zadanie 7 ########################
## Zapisz do pliku liczbę 123456789, spakuj, rozpakuj dane
## Sprawdź w dokumentacji pakietu struct typ danej
## https://docs.python.org/3/library/struct.html


from struct import *

# f = open('Binarno.txt', 'wb')
# dane = pack('i', 123456789)
# f.write(dane)
# f.close()
#
# f2 = open('Binarno.txt', 'rb')
# dane2 = unpack('i', f2.read())
# f2.close()
# print(dane2)

########################## Zadanie 9 #########################
## Utwórz i zapisz do folderu 5 dowolnych plików tekstowych z dowolnym tekstem
##(więcej niż 5 zdań), możesz tez skopiować dowolny tekst.
## Nazwy plików: Tekst1ID_ABC, Tekst2ID_405.txt, Tekst3ID_607.txt, Tekst4ID_ABC.txt, Tekst5ID_DEF.txt
## Uwaga: pisząc program przyjmij założenie, że masz takich nazw plików w folderze tysiące,
## program ma działać niezależnie od liczby plików w folderze
## Utwórz funkcję która:
## a) odczyta z folderu nazwy wszystkich plików
## b) dla plików zakończonych ciągiem znaków 'ABC' wyznacz liczbę wyrazów złożonych z conajmnie 3 liter.
## Utwórz dodatkowową funkcję która wykorzystując poprzednią funkcję sprawdzi:
## a) ile plików zawiera w identyfikatorze ID liczbę 0
## b) dla wszystkich plików które w nazwie nie mają liczby 0
##    wyznaczy liczbę słów
## c) dla plików zakończonych ciągiem znaków 'ABC' wyznacz liczbę wyrazów złożonych z conajmnie 3 liter.
#
#
# def f2(func):
#     def wrapper(path):
#         files_id_with_0 = list(filter(lambda x: fnmatch.fnmatch(x, '*ID_*0*'), os.listdir()))
#         print('Plików, które zawierają \'0\' w ID jest: {}'.format(len(files_id_with_0)))
#         for file in os.listdir():
#             if file not in files_id_with_0:
#                 f = open(file, 'r', encoding='utf-8')
#                 print('Plik \'{}\' zawiera {} słów.'.format(file, len(f.read().split(" "))))
#                 f.close()
#         func(path)
#     return wrapper
#
#
# @f2
# def f1(path):
#     os.chdir(path)
#     print(os.listdir('.'))
#     for file in filter(lambda x: fnmatch.fnmatch(x, '*ABC'), os.listdir()):
#         f = open(file, 'r', encoding='utf-8')
#         num_of_3_and_more_words = len(list(filter(lambda x: len(x) >= 3, f.read().split(' '))))
#         print('Plik \'{}\' posiada {} wyrazów składających się z co najmniej 3 liter.'
#               .format(file, num_of_3_and_more_words))
#         f.close()
#
#
# os.chdir(os.path.join(os.getcwd(), 'Folder'))
# f1(os.getcwd())
