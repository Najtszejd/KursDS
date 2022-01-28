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

jest_liczba = lambda ciag: ciag.replace(".","",1).replace("-","",1).isdigit()
print(jest_liczba("1342304272.0"))