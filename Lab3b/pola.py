import globals
import pole_trojkata
import pole_prostokata


def oblicz_pola(prostokat=True, kwadrat=True, trojkat=True, **kwargs):
    if prostokat:
        a = globals.prostokat_bok_a
        b = globals.prostokat_bok_b
        if 'prostokat_bok_a' in kwargs.keys():
            a = kwargs['prostokat_bok_a']
        if 'prostokat_bok_b' in kwargs.keys():
            b = kwargs['prostokat_bok_b']
        print('Pole prostokąta to {}'.format(pole_prostokata.pole(a, b)))
    if kwadrat:
        a = globals.kwadrat_bok
        if 'kwadrat_bok' in kwargs.keys():
            a = kwargs['kwadrat_bok']
        print('Pole kwadratu to {}'.format(pole_prostokata.pole(a, a)))
    if trojkat:
        a = globals.trojkat_podstawa
        h = globals.trojkat_wysokosc
        if 'trojkat_podstawa' in kwargs.keys():
            a = kwargs['trojkat_podstawa']
        if 'trojkat_wysokosc' in kwargs.keys():
            h = kwargs['trojkat_wysokosc']
        print('Pole trójkąta to {}'.format(pole_trojkata.pole(a, h)))
