lista1 = []
lista2 = []
while True:
    login = input('Podaj login: ')
    if login == 'STOP':
        break
    haslo = input('Podaj hasło: ')
    lista1.append(login)
    lista2.append(haslo)
slownik = {}
for indeks, login in enumerate(lista1):
    slownik[login] = lista2[indeks]
print(slownik)