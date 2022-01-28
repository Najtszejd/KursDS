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
# def pierwsza(krotka):
#     return krotka[1]
# def krotki(x):
#     sorted(x, keys = pierwsza())
#     return x

# print(krotki([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# Ćwiczenie
# Napisz funkcję w Pythonie, aby uzyskać łańcuch składający się z pierwszych 2 i ostatnich 2 znaków z danego łańcucha.
# Jeśli długość ciągu jest mniejsza niż 2, zwróć zamiast tego pusty ciąg.
# Przykładowy ciąg : Python
# Oczekiwany wynik: Pyon
# Przykładowy ciąg : Py
# Oczekiwany wynik: PyPy
# Przykładowy ciąg : P
# Oczekiwany wynik: pusty ciąg
# def str_leng(x):
#     if len(x)<2:
#         return "pusty ciąg"
#     else:
#         return x[:2] + x[-2:]
# print(str_leng("Python"))
# print(str_leng("Py"))
# print(str_leng("P"))

# Ćwiczenie
# Napisz program, policzy silnię dla liczby n tj.
# n! = 1*2*3*4...*(n-2)*(n-1) * n
# Zrób to przez napisanie funkcji, która rekurencyjne będzie się odwoływała do samej
# siebie do momentu gdy będzie liczyła silnie dla 1, która wynosi 1.
# def silnia(n):
#      if n == 1:
#         return 1
#     return silnia(n-1)*n
# print(silnia(4))


# Rekurencyjny ciąg Fibonacciego w Pythonie.
# def ciag_F(n):
#     if n <=1:
#         return 1
#     return ciag_F(n-1)+ciag_F(n-2)
# print(ciag_F(5))

# Ćwiczenie
#
# Napisz funkcję w Pythonie, aby uzyskać łańcuch składający się z pierwszych 2 i ostatnich 2 znaków z danego łańcucha.
# Jeśli długość ciągu jest mniejsza niż 2, zwróć zamiast tego pusty ciąg.
# Przykładowy ciąg : CodeBrainers
# Oczekiwany wynik: Cors
# Przykładowy ciąg : CB
# Oczekiwany wynik: CBCB
# Przykładowy ciąg : C
# Oczekiwany wynik: pusty ciąg

# def ciag(x):
#     if len(x) < 2:
#         return ("ciąg pusty")
#     return x[:2] + x[-2:]
# print(ciag("CodeBrainers"))
# print(ciag("CB"))
# print(ciag("C"))