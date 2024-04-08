# # ################################ Task 0
# '''
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line. Don't forget about function documentation
#
# '''
# ##### do testów możesz użyć:
# x = 1000
# # y = 2101
# # my_list = list(range(x,y,1))
# # print(my_list)
#
# def func(x, y):
#     '''
#     Funkcja szuka liczb podzielnych przez 7 i niepodzielnych przez 5
#     z przedziału od x do y włącznie.
#     :param x: (int) dolna granica
#     :param y: (int) górna granica
#     :return: listę liczb podzielnych przez 7 i niepodzielnych przez 5 z przedziału [x, y]
#     '''
#     lista = list(filter(lambda a: a % 7 == 0 and a % 5 != 0, range(x, y+1)))
#     return lista
#
#
# x = 1000
# y = 2101
# print(func(x, y))
import fnmatch
import string


# # ################################ Task 1
## A website requires the users to input username and password to register.
## Create function to check the validity of password input by users.
## Using continue() or break().
## Following are the criteria for checking the password:
## 1. At least 1 letter between [a-z]
## 2. At least 1 number between [0-9]
## 3. At least 1 letter between [A-Z]
## 4. Minimum length of transaction password: 4
## 5. Maximum length of transaction password: 8
## You should to document your code by using python docstrings (google)
## Save result to *.txt file
#
# def is_valid_password(password):
#     '''
#     Funkcja sprawdza poprawność hasła według 5 kryteriów.
#     :param password: hasło podawane przez użytkownika
#     :return: True lub False zależnie od poprawności hasła
#     '''
#     if len(password) < 4:
#         print('Hasło jest za krótkie!')
#         return False
#     elif len(password) > 8:
#         print('Hasło jest za długie!')
#         return False
#     flag = False
#     for char in list(password):
#         if char in string.ascii_lowercase:
#             flag = True
#             break
#     if not flag:
#         print('Hasło musi zawierać przynajmniej jedną małą literę [a-z]!')
#         return False
#     for char in list(password):
#         if char in string.ascii_uppercase:
#             break
#     if not flag:
#         print('Hasło musi zawierać przynajmniej jedną dużą literę [A-Z]!')
#         return False
#     for char in list(password):
#         if char in range(10):
#             flag = True
#             break
#     if not flag:
#         print('Hasło musi zawierać przynajmniej jedną cyfrę [0-9]!')
#         return False
#     return True
#
#
# def get_username_password():
#     '''
#     Funkcja pobiera dane do rejestracji.
#     :return: krotka zawierająca login i hasło
#     '''
#     print('** Rejestracja **')
#     username = input('Podaj login: ')
#     password = input('Podaj hasło: ')
#     return username, password
#
#
# while True:
#     data = get_username_password()
#     if is_valid_password(data[1]):
#         break
# f = open('data.txt', 'a')
# f.write(data[0] + ' ' + data[1] + '\n)
# f.close()

################ Task 2
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line.
## You should to document your code by using python docstrings
## (dokumentacja kodu styl google)
## Don't forget to handle exceptions (obsłudze wyjątków)
## Save result to *.pkl file use picle package
# '''
# ##### do testów możesz użyć:
# x = 1000
# # y = 2101
# # my_list = list(range(x,y,1))
# # print(my_list)
# import pickle
#
# def func(x, y):
#     '''
#     Funkcja szuka liczb podzielnych przez 7 i niepodzielnych przez 5
#     z przedziału od x do y włącznie.
#     :param x: (int) dolna granica
#     :param y: (int) górna granica
#     :return: listę liczb podzielnych przez 7 i niepodzielnych przez 5 z przedziału [x, y]
#     '''
#     try:
#         x = int(x)
#         y = int(y)
#     except ValueError:
#         print('Niepoprawny format argumentów funkcji \'func\'.')
#         return []
#     lista = list(filter(lambda a: a % 7 == 0 and a % 5 != 0, range(x, y+1)))
#     return lista
#
#
# b = 1000
# c = 2101
# f = open('file.pkl', 'ab')
# pickle.dump(str(b) + ' ' + str(c) + ' ' + str(func(b, c)) + '\n', f)
# f.close()

################ Task 3
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Name of input parameters:
## You should to document your code by using python docstrings (google)
###############

################ Task 4
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Use: dynamic variable name (exec() or globals() or locals())
## Name of input parameters: x1, x2, ..., xn
## You should to document your code by using python docstrings (google)
## Don't forget to handle exceptions (obsłudze wyjątków)
###############
#
# def func(*args):
#     '''
#     Funkcja dla każdego argumentu oblicza x^x
#     :param args: lista n argumentów
#     :return: listę wyników x^x
#     '''
#     if len(args) > 99:
#         raise ValueError("Liczba argumentów jest za duża!")
#     lis = []
#     for i, num in enumerate(args, start=1):
#         exec(f'x{i} = {num}')
#         exec(f'lis.append(x{i}**x{i})')
#     return lis
#
#
# inp = input('Podaj liczby: ').split(', ')
# try:
#     result = func(*map(int, inp))
#     print(result)
# except ValueError as ev:
#     print('Error: {}'.format(ev))
# except Exception as e:
#     print('Error: {}'.format(e))

########################## Task 5 ########################
## The first step,
## generate test data: create folder. Create 5 text files to this folder,
## each file contains more than 5 sentences.
## Filenames: Text1ID_ABC, Text2ID_405.txt, Text3ID_607.txt, Text4ID_ABC5.txt, Text5ID_DEF.txt
##
## Create function with multiple arguments that:
## a) print all file from folder
## b) if the file name contains 'ABC', count how many words in the text of file
## contain words with more than 3 letters
## Next step: decorate this function, add the following functionality:
## a) the function will check how many files have 0 in the filename
## b) if the file has 0 in the filename then the function counts words in the text of the file
## c) if the filename contains 'EF.txt', then the function copy this file to
## 'DocumentLab5copy' directory
#
# import os
#
#
# def copy_file(src_file, dst_file):
#     src = open(src_file, 'r')
#     dst = open(dst_file, 'w')
#     dst.write(src.read())
#     src.close()
#     dst.close()
#
#
# def decor(fun):
#     def wrapper(*args):
#         fun(*args)
#         for folder in args:
#             os.chdir(folder)
#             j = 0
#             for file in os.listdir():
#                 if not os.path.isfile(file):
#                     continue
#                 f = open(file, 'r')
#                 if '0' in file:
#                     j += 1  # liczy pliki z '0' w nazwie
#                     # wypisuje liczbę słów w plikach z '0' w nazwie
#                     print('Plik \'{}\' posiada {} słów.'.format(file, len(f.read().split(' '))))
#                 if fnmatch.fnmatch(file, '*EF.txt'):
#                     # sprawdza czy folder istnieje; jeśli nie, tworzy go
#                     if not os.path.exists(os.path.join(folder, 'DocumentLab5copy')):
#                         os.makedirs('DocumentLab5copy')
#                     copy_file(os.path.join(folder, file), os.path.join(folder, 'DocumentLab5copy', file))
#                 f.close()
#             print('Pliki, które mają \'0\' w nazwie: {}'.format(j))
#     return wrapper
#
#
# @decor
# def func(*args):
#     # Wypisuje pliki z folderów i zapisuje je do listy
#     for folder in args:
#         os.chdir(folder)
#         print(os.listdir())
#         for file in list(filter(lambda x: fnmatch.fnmatch(x, '*ABC*'), os.listdir())):
#             f = open(os.path.join(folder, file), 'r')
#             # Liczy ilość słów w plikach, które mają ponad 3 litery
#             i = 0
#             words = f.read().split(' ')
#             for word in words:
#                 if len(word) > 2:
#                     i += 1
#             print('Ilość co najmniej 3 literowych słów w pliku \'{}\': {}'.format(file, i))
#
#
# path = os.getcwd()
# # os.makedirs(os.path.join(path, 'Folder'))
# # os.chdir(os.path.join(path, 'Folder'))
# #
# # f1 = open('Text1ID_ABC', 'w')
# # f2 = open('Text2ID_405.txt', 'w')
# # f3 = open('Text3ID_607.txt', 'w')
# # f4 = open('Text4ID_ABC5.txt', 'w')
# # f5 = open('Text5ID_DEF.txt', 'w')
# # f1.write('''Woda jest źródłem życia, a jej jakość bezpośrednio wpływa na zdrowie ekosystemów, dobrostan ludzi i trwałość środowiska naturalnego.
# # W obliczu globalnych wyzwań, takich jak zanieczyszczenie wód, zmiany klimatyczne i rosnące zapotrzebowanie na czystą wodę, nowoczesne technologie uzdatniania wody nabierają kluczowego znaczenia.
# # Dzięki nim możliwe jest nie tylko zapewnienie dostępu do bezpiecznej wody pitnej dla coraz większej liczby ludzi, ale także ochrona środowiska i zasobów naturalnych dla przyszłych pokoleń.
# # Woda jest niezbędna dla życia - nie tylko utrzymuje nas przy życiu, ale także odgrywa centralną rolę w rolnictwie, przemyśle i gospodarce.
# # Jednak zanieczyszczenie wody jest jednym z najpoważniejszych problemów ekologicznych naszych czasów.''')
# # f2.write('''Substancje chemiczne, odpady przemysłowe i rolnicze, mikroplastik - wszystko to znajduje drogę do naszych rzek, jezior i oceanów, zagrażając życiu wodnemu i zdrowiu ludzi.
# # Nowoczesne technologie uzdatniania wody otwierają nowe możliwości w walce z tymi wyzwaniami.
# # Innowacje takie jak zaawansowana filtracja, odwrócona osmoza, dezynfekcja UV i procesy biologiczne pozwalają na skuteczne usuwanie zanieczyszczeń i patogenów z wody, zapewniając jej wysoką jakość.
# # Dzięki temu możliwe jest nie tylko poprawienie zdrowia i dobrostanu ludzi, ale także ochrona środowiska wodnego i jego mieszkańców.
# # Ekologiczne metody uzdatniania wody, wykorzystujące mniej energii i chemikaliów, przynoszą szereg korzyści dla środowiska.''')
# # f3.write('''Pomimo postępów technologicznych, wciąż istnieją wyzwania, takie jak dostosowanie infrastruktury, zmniejszenie kosztów technologii oraz edukacja i podnoszenie świadomości społecznej na temat znaczenia ochrony zasobów wodnych.
# # Przyszłość uzdatniania wody będzie zależała od naszej zdolności do inwestowania w zrównoważone technologie, wspierania badań naukowych i promowania międzynarodowej współpracy w ochronie najcenniejszego zasobu naszej planety - wody.
# # Nowoczesne technologie uzdatniania wody mają kluczowe znaczenie dla zrównoważonego rozwoju, zdrowia publicznego i ochrony środowiska.
# # Dzięki nim możemy stawić czoła wyzwaniom związanym z zanieczyszczeniem wody i zapewnić dostęp do czystej wody dla wszystkich.
# # Inwestycje w innowacyjne metody uzdatniania, edukacja ekologiczna i międzynarodowa współpraca są niezbędne, aby chronić zasoby wodne.''')
# # f4.write('''W ramach projektu BIOMAC utworzona zostanie otwarta platforma testowa poświęcona zwiększaniu skali nowych koncepcji materiałów pochodzenia biologicznego przy konkurencyjnych kosztach i jednoczesnym dostępie do kompleksowych usług.
# # BIOMAC to partnerstwo badawczo-przemysłowe 34 podmiotów, które służy zintegrowanej strategii zwiększania skali produktów i materiałów pochodzących z biomasy.
# # Jego celem jest stworzenie otwartego ekosystemu innowacji (OITB-Open Innovation Test Bed), który zapewni holistyczne usługi w zakresie projektowania, rozwoju i testowania nowych biokompozytów polimerowych opartych na nanotechnologii.
# # Jednocześnie będzie oferować usługi obejmujące ocenę ram regulacyjnych, zrównoważonego rozwoju, obiegu zamkniętego i potencjału rynkowego, dostępne na uczciwych warunkach i kosztach dla zainteresowanych stron.
# # Biokompozyty na bazie nanocząstek są odpowiedzią na wiele wyzwań stojących przed naszym społeczeństwem w zakresie nowych, przyjaznych dla środowiska materiałów, ale brak inwestycji, finansowania i ich ograniczona produkcja na dużą skalę sprawiają, że na rynku dostępna jest tylko niewielka liczba takich materiałów.''')
# # f5.write('''BIOMAC wypełnia tę lukę, zapewniając kompleksowe usługi zainteresowanym stronom i przyspieszając wejście na rynek innowacyjnych materiałów pochodzenia biologicznego.
# # Aby to osiągnąć, połączono innowacyjne technologie i odpowiednie metodologie, które zostały już opracowane na wysokim poziomie przez partnerów i zostały ulepszone w kontekście tworzenia ekosystemu BIOMAC.
# # Open Innovation Test Beds (OITB) to podmioty z siedzibą w co najmniej 3 krajach UE, które oferują dostęp do fizycznych obiektów, możliwości i usług potrzebnych do opracowywania, testowania i skalowania nanotechnologii i zaawansowanych materiałów.
# # Ich celem jest uczynienie rozwoju innowacyjnych produktów bardziej dostępnym dla firm i użytkowników, aby przejść od walidacji w laboratorium (TRL 4) do prototypów w środowisku przemysłowym (TRL 7).
# # Tworzenie OITB jest finansowane przez UE w ramach działań programu Horyzont, w kontekście promowania biogospodarki.''')
# #
# # f1.close()
# # f2.close()
# # f3.close()
# # f4.close()
# # f5.close()
#
# func(os.path.join(os.getcwd(), 'Folder'))
