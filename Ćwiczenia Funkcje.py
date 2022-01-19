# def inny_len(x):
#     y = 0
#     for element in x:
#         y += 1
#     return y
# print(inny_len("jakisstring"))
# Ćwiczenie
# Napisz funkcję w Pythonie, która zsumuje wszystkie elementy na liście.
#
# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers
#
#
# print(sum_list([1, 2, -8]))
# Funkcja w Pythonie, który mnoży wszystkie elementy na liście



# Ćwiczenie
# Napisz funkcję w Pythonie, który mnoży wszystkie elementy na liście.
# def mnlist(elementy):
#     iloraz_elementy = elementy[0]
#     for i in elementy[1:]:
#         iloraz_elementy *=i
#     return iloraz_elementy
# print(mnlist([2,4,6]))

# Ćwiczenie
# Napisz funkcję w Pythonie, aby uzyskać największą liczbę z listy.

# def maxlist(list):
#     a = list[0]
#     for i in list[1:]:
#         if i > a:
#             a = i
#     return a
# print(maxlist([222,3,4,5, 101,6,7,8,9]))
# print(maxlist([-1,-2,-22,-90,-9,5]))

# Ćwiczenie
# Napisz funkcję w Pythonie, który zlicza liczbę znaków (częstotliwość znaków) w ciągu tekstowym.
# Przykładowy ciąg tekstowy: google.com
# Oczekiwany wynik: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
# def znaki(x):
#     znak = {}
#     for i in x:
#         klucze = znak.keys()
#         if i in klucze:
#             znak[i] += 1
#         else:
#             znak[i]=1
#     return znak
# print(znaki("google.com"))

# Ćwiczenie
# Napisz funkcję w Pythonie, który zlicza ciągi znaków, w których długość ciągu wynosi 2 lub więcej, a pierwszy i ostatni znak są takie same z podanej listy ciągów.
# Przykładowa lista : ['abc', 'xyz', 'aba', '1221']
# Oczekiwany wynik: 2

# def ciag(x):
#     licznik = 0
#     for i in x:
#         if len(i) >= 2 and i[-1] == i[0]:
#             licznik +=1
#     return licznik
# print(ciag(['abc', 'xyz', 'aba', '1221']))

# Ćwiczenie
# Napisz funkcję w Pythonie, aby uzyskać listę posortowaną w porządku
# rosnącym według ostatniego elementu w każdej krotce z podanej listy niepustych krotek.
# Przykładowa lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Oczekiwany wynik : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def pierwsza(krotka):
    return krotka[1]
def krotki(x):
    sorted(x, keys = pierwsza())
    return x

print(krotki([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))