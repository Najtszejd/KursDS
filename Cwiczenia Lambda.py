# Utwórz funkcję lambda, która przyjmuje jeden parametr (a) i zwraca go

# to_samo = lambda a : a
# print(to_samo(3))

# Kolejne ćwiczenie na rozgrzewkę
# Napisz program w Pythonie, aby utworzyć funkcję lambda,
# która dodaje 15 do podanej liczby przekazanej jako argument i zwraca to wynik.

# sum_15 = lambda a: a+15
# print(sum_15(10))

# Utwórz funkcję lambda, która mnoży argument x przez argument y i zwraca to wynik. Następnie wydrukuj wynik.
# iloraz_dwa = lambda a,b: a*b
# print(iloraz_dwa(10,5))

# Napisz program w Pythonie wsparcia sortowania listy krotek za pomocą lambda po drugim elemencie
# subject_marks = [('Język angielski', 88),
#                  ('Nauka',           90),
#                  ('Matematyka',      97),
#                  ('Nauki społeczne', 82)]
# print(sorted(subject_marks, key= lambda krotka: krotka[1]))

# Ćwiczenie
# Napisz program w Pythonie, aby posortować za pomocą lambda listę słowników po kluczu model lub kolor.
# 8:06
# models = [{'marka': 'Nokia',   'model': '3310',   'kolor': 'Czarny'},
#           {'marka': 'Apple',   'model': '11',     'kolor': 'Złoty'},
#           {'marka': 'Samsung', 'model': 'Galaxy', 'kolor': 'Srebrny'}]
# print(sorted(models, key= lambda modele: ["model"]))

# Ćwiczenie
# Napisz program w Pythonie, aby sprawdzić, czy dany ciąg (str) zaczyna się od znaku ‘P’, używając lambda
# Podpowiedź: skorzystaj z funkcji (metody) startswith()

# string_P = lambda string_P: string_P.startswith("P")
# print(string_P("Python"))
# Ćwiczenie
# Napisz program w Pythonie, aby wyodrębnić rok, miesiąc, dzień i godzinę za pomocą lambda
# Podpowiedź: skorzystaj z modułu datetime:
# now = datetime.datetime.now() - przypisuje do nowaktualną lokalną datę i godzinę.
# now.year - wyodrębnia i zwraca rok z now.
# now.month - wyodrębnia i zwraca miesiąc z now.
# now.day - wyodrębnia i zwraca dzień z now.
# now.time() - wyodrębnia i zwraca godzinę z now.

# import datetime
# now = datetime.datetime.now()
# print(now)
# dzien = lambda a: a.day
# miesiac = lambda b: b.month
# rok = lambda c: c.year
# godzina = lambda d: d.time()
# print("Godzina {},\n Rok {},\n Miesiac {},\n Dzien {}".format (godzina(now), rok(now), miesiac(now),dzien(now)))


# Ćwiczenie
# Napisz program w Pythonie, aby sprawdzić, czy dany ciąg jest liczbą, czy nie, używając lambda
# Podpowiedź: przydatna metoda to
# string.replace(oldvalue, newvalue, count)
# Składnia parametrów:
# oldvalue – Wymagany; ciąg do wyszukania
# newvalue – Wymagany; ciąg znaków, który ma zastąpić starą wartość
# count – Opcjonalny; liczba określająca, ile wystąpień starej wartości chcesz zastąpić;
# domyślnie są to wszystkie wystąpienia

# jest_liczba = lambda ciag: ciag.replace(".","",1).replace("-","",1).isdigit()
# print(jest_liczba("1342304272.0"))

# Ćwiczenie
# Napisz program w Pythonie do filtrowania listy liczb parzystych i nieparzystych całkowitych za pomocą lambda i filter


# liczby = [1,2,3,4,5,6,7,8,9]
# wynik = list(filter(lambda x: x % 2 == 0, liczby))
# print(wynik)
# wynik_niep = list(filter(lambda y: y % 2 != 0, liczby))
# print(wynik_niep)

# Ćwiczenie
# Napisz program w Pythonie, aby znaleźć przecięcie dwóch podanych list za pomocą lambda i filter
# array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
# array_nums2 = [1, 2, 4, 8, 9]
# czesc_wspolna = list(filter(lambda x: x in array_nums1, array_nums2))
# print(czesc_wspolna)

# Ćwiczenie
# Napisz program w Pythonie, aby policzyć parzyste i nieparzyste liczby w danej tablicy liczb całkowitych, używając lambda i filter
# array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
# policz_parzyste = len(list(filter(lambda x: x % 2 == 0, array_nums)))
# print(policz_parzyste)
# policz_nieparzyste = len(list(filter(lambda x: x % 2 != 0, array_nums)))
# print(policz_nieparzyste)

# Ćwiczenie
# Napisz program w Pythonie, aby znaleźć wartości o długości sześć na podanej liście za pomocą funkcji lambda i filter
# weekdays = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
# wartosci = list(filter(lambda x: len(x) == 6, weekdays))
# print(wartosci)

# Ćwiczenie
# Napisz program w Pythonie, aby znaleźć liczby podzielne przez dziewiętnaście lub trzynaście z listy liczb za pomocą lambda i filter
# nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# liczby = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, nums))
# print(liczby)

# Ćwiczenie
# Napisz program w Pythonie, aby znaleźć palindromy na podanej liście ciągów za pomocą lambda i filter
# Palindrom – wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# Przykładem palindromu jest: „kobyła ma mały bok”
# texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
# palindrom = list(filter(lambda x: x[::1] == x[::-1], texts))
# print(palindrom)

# Ćwiczenie
# Napisz program w Pythonie, który zsumuje długość imion z danej listy imion po usunięciu imion zaczynających się od małej litery
# Użyj funkcji lambda
# sample_names = ['antoni', 'Jakub', 'zuzanna', 'Julia', 'Jan', 'szymon']
#
# wynik = list(filter(lambda x: x[0].isupper() == True and x[1:].islower() == True, sample_names))
# imiona = "".join(wynik)
# print(imiona, len(imiona))

# Ćwiczenie
# Napisz program w Pythonie podnoszący do kwadratu i sześcianu każdą liczbę z podanej listy liczb całkowitych, używając lambda i map
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# kwadrat = list(map(lambda x: x**2, nums))
# print(kwadrat)
# szescian = list(map(lambda x: x**3, nums))
# print(szescian)

# Ćwiczenie
# Napisz program w Pythonie, aby dodać dwie podane listy za pomocą map i lambda
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# nums3 = list(map(lambda x, y: x+y,nums1, nums2))
# print(nums3)

# Ćwiczenie
# Napisz program w Pythonie, który za pomocą funkcji lambda mnoży każdą liczbę z podanej listy przez określoną liczbę
# Wydrukuj wynik
# nums = [2, 4, 6, 9, 11]
# n = 2
# wynik = list(map(lambda x: x*n, nums))
# print(wynik)

# Ćwiczenie
# Napisz program w Pythonie, który usuwa liczby dodatnie z podanej listy liczb
# Zsumuj liczby ujemne i wydrukuj wartość bezwzględną za pomocą tworzenia listy – ang. list comprehension
# Wydrukuj wynik
# nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
#
# l_c =  abs(sum([i for i in nums if i < 0]))
# print(l_c)

# Ćwiczenie
# Napisz program w Pythonie, aby zmienić kolejność liczb dodatnich i ujemnych w danej liście
# (najpierw wszystkie ujemne, potem wszystkie dodatnie) za pomocą tworzenia listy – ang. list comprehension
# array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
# wynik = [x for x in array_nums if x<=0] + [x for x in array_nums if x>0]
# print(wynik)

# Ćwiczenie
# Napisz program w Pythonie, aby:
# Znaleźć liczby z podanego ciągu
# Zapisać je na liście
# Wyświetlić liczby w posortowanej formie
# Użyj funkcji tworzenia listy – ang. list comprehension, aby rozwiązać problem
# str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
# wynik = sorted(int(x) for x in str1.split(' ') if x.isdigit())
# print(wynik)

# Zadanie 1
# Napisz funkcję anonimową obliczającą kwadrat danej wartości
# Czy potrafisz wytłumaczyć czym się to różni od użycia funkcji
# pow(a, b) lub operatoraa ** b?

# kwadrat = lambda x: x*x
# print(kwadrat(5))

# Zadanie 2
# Napisz funkcję anonimową obliczającą średnią arytmetyczną dwóch wartości

# srednia = lambda x,y: (x+y)/2
# print(srednia(2,7))


# Zadanie 3
# Napisz funkcję anonimową sprawdzającą czy dana wartość jest większa (lub mniejsza) od pewnej wartości
# Taka funkcja anonimowa powinna zwracać wartość logiczną

# porownanie = lambda x,y: x>y
# print(porownanie(2,4))
# print(porownanie(4,2))


# Zadanie 4
# Znajdź wszystkie wartości mniejsze od 36.6
temperatury = [
    37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
    35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
    39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
    36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
    33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
    39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
    34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
    34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
    34.2, 40.2, 34.3, 35.3]
# temp_min = list(filter(lambda x: x < 36.6, temperatury))
# print(sorted(temp_min))

# Zadanie 5
# Odfiltruj wszystkie wartości, które są:
# Mniejsze bądź równe 35.0, lub
# Większe bądź równe 40.0
# temp_random = list(filter(lambda x: x <= 35.0 or x >= 40.0, temperatury))
# print(temp_random)

# Zadanie 6
# Oblicz dla każdej liczby w zbiorze temperatur kwadrat:
# Różnicy tej liczby, i Średniej arytmetycznej całego zbioru

# temp_kwadrat_roznicy = list(map(lambda x: (x*x + x*x) - (2*x * 2*x), temperatury))
# licznik = 0
# for x in temperatury:
#     licznik += x

# print(temp_kwadrat_roznicy)
# print(round(licznik/len(temperatury)))

# Zadanie 7
# Mając obliczone wartości odchyleń temperatur od średniej temperatury, oblicz wariancję tych wartości
# Wariancja:
# Klasyczna miara zmienności
# Intuicyjnie utożsamiana ze zróżnicowaniem zbiorowości
# Jest średnią arytmetyczną kwadratów odchyleń (różnic):
# Poszczególnych wartości cechy, od
# Wartości oczekiwanej
# https://www.matemaks.pl/wariancja.html
# Nie zapomnij o podzieleniu przez ilość elementów w zbiorze!

# suma_zbioru = round(sum(temperatury))
# srednia_zbioru = suma_zbioru / len(temperatury)
# wartosc_odchylen = [y - srednia_zbioru for y in temperatury]
# # for y in temperatury:
# #     wartosc_odchylen.append(y - srednia_zbioru)
# wariancje = [(x - srednia_zbioru) ** 2 for x in temperatury]
# # for x in temperatury:
# #     wariancje.append((x - srednia_zbioru)**2)
# waraincje_wynik = sum(wariancje)/len(wariancje)
# print("Wariancja temperatur wynosi: {}".format(waraincje_wynik))


# Zadanie 8
# Napisz pogram, który policzy kwadraty liczb z zakresu [1,10000], które podzielne są przez:
# 5, lub 9
# Następnie sprawdź, które z uzyskanych liczb są podzielne:
# Zarówno przez 5,
# Jak i przez 9

# sqrt_number = [x**2 for x in range(1, 10000) if x % 5 == 0 or x % 9 == 0]
# print(sqrt_number)
# podzielne_przez_5 = []
# podzielne_przez_9 = []
# for number in sqrt_number:
#     if number % 5 == 0:
#         podzielne_przez_5.append(number)
#     else:
#         number % 9 ==0
#         podzielne_przez_9.append(number)
# print("Liczby podzielne przez 5:\n {}".format(podzielne_przez_5))
# print("Lidzby podzielne przez 9:\n {}".format(podzielne_przez_9))


# Zadanie 9
#
# Stwórz zbiór, który wypełnisz 30 wywołaniami funkcji:
# random.randint(1, 30)
# Ile razy wylosowana została ta sama wartość?
# Sprawdzisz to porównując liczbę elementów zbioru.
# Jak się zachowa program, jeśli zmienisz argumenty do funkcji randint?
# A jeśli zmienisz liczbę wywołań tej funkcji?

# import random
# zbior = [random.randint(1, 30) for x in range(0, 30)]
# print(zbior)
# wywolania = {x: zbior.count(x) for x in zbior}
# print(wywolania)

# Zadanie 10
# Napisz program w Pythonie do tworzenia ciągu Fibonacciego aż do n za pomocą lambda i reduce
# Podpowiedzi:
# Da się to zrobić w zasadzie w jednej linijce!
# Przypomnij sobie, co robiła zmienna _
# from functools import reduce
# fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],range(n - 2), [0, 1])
#
# print("Ciąg Fibonacciego do 2:")
# print(fib_series(10))

# def fibbonaci_numbers(n):
#     ''' zwraca liczby Fibonacciego mniejsze od n '''
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#     # while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik