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


os.makedirs(os.path.join(os.getcwd(), 'Dokument'))
change_actual_path(os.path.join(os.getcwd(), 'Dokument'))
f1 = open('Lab1.doc', 'w')
f2 = open('Lab2.doc', 'w')
f3 = open('Lab3.doc', 'w')
f1.close()
f2.close()
f3.close()
print(filter(fnmatch.fnmatch(), os.listdir('.')))
print(os.listdir())
