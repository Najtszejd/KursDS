# Ćwiczenie
# Podczas pisania funkcji najlepiej jest przeprowadzić walidację liczb.
# Jeśli użytkownicy wprowadzą tekst, pojawi się błąd podczas próby konwersji na int.
# Napisz program, który poprosi użytkownika o podanie dwóch liczb.
# Dodaj i wydrukuj wynik.
# Jeśli nie zostanie wprowadzona liczba, zwróć komunikat o błędzie i poproś ponownie.

# while ValueError: #może byc True
#     x = input("Podaj pierwszą liczbę")
#     y = input("Podaj drugą liczbę")
#     try:
#         x = int(x)
#         y = int(y)
#         print(x+y)
#         break
#     except ValueError:
#           print("Podane wartości nie są liczbami")

# Ćwiczenie
# Podziel przez siebie dwie liczby
# Umieść:
# result = "Nie możesz podzielić przez 0"
# we właściwym miejscu, aby program uniknął ZeroDivisionError
# Podpowiedź 1: Po prostu umieść przypisanie wartości dla wyniku po linii Except
# Podpowiedź 2: Zwróć uwagę na wcięcia
# a = 10
# b = 2
# try:
#     result = a/b
# except ZeroDivisionError:
#     result = "Nie możesz podzielić przez 0"
# print(result)
# Polecenie except, który nic nie robi
# Ćwiczenie
# Napisz dowolny kod.
# Wychwyć w nim wyjątek, ale nic nie rób.

# a = 10
# b = "c"
# try:
#     print(int(b))
# except:
#     pass
#
# print("Nic sie nie stalo")

# Ćwiczenie
# Spróbuj dodać int do ciągu.
# Umieść:
# msg = "Nie możesz dodać int do string"
# aby program uniknął błędu BaseException.
# Możesz użyć wyjątku Exception, chociaż
# zwykle powinno się ostrożnie używać tak potężnych instrukcji wyjątków.

# try:
#     msg = 10 + "10"
# except TypeError:
#     msg = "Nie można dodać int do string"
# print(msg)

# Wyjątek IndexError w instrukcjach try except
# Ćwiczenie
# Stwórz trójelementową listę.
# Spróbuj wydrukować piąty element.
# Umieść:
# msg = "Jesteś poza zakresem listy"
# aby uniknąć wyjątku IndexError.

# a = [1,2,"asd"]
# try:
#     print(a[5])
# except IndexError as err:
#     msg = err
# print (msg)


# Ćwiczenie
# Spróbuj otworzyć do czytania plik (podpowiedź: f = open(arg, "r")).
# W razie braku możliwości otwarcia pliku, obsłuż wyjątek.
# W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy (podpowiedź: len(f.readlines()).
# Na koniec zamknij ten plik (podpowiedź: f.close()).
# arg = "Typy.py"
# try:
#     f = open(arg,"r")
# except IOError:
#     print("Plik nie istnieje")
# else:
#     print("Ilość wierszy to: ", str(len(f.readlines())))
#     f = f.close()

# Ćwiczenie
# Użyj finally do zamykania obiektów i czyszczenia zasobów.
# Spróbuj otworzyć i zapisać (podpowiedź: write) w pliku, którego nie można zapisać.
# Zapewnij, aby program mógł kontynuować bez pozostawiania otwartego obiektu pliku.
# try:
#     plik = open("main.py","r")
#     plik.write("string")
# except IOError:
#     print("coś poszło nie tak")
# finally:
#     plik.close()


# Ćwiczenie
# Napisz funkcję dzielącą jej argument pierwszy przez drugi.
# Spróbuj wykonać działanie i zwrócić wynik.
# W przypadku błędu dzielenia przez zero, wypisz komunikat o błędzie.
# Wypisz komunikat, który zawsze się wypisze.
# Wywołaj funkcję z różnymi argumentami.

# def dzielenie(x,y):
#     try:
#         return x/y
#     except ZeroDivisionError:
#         return "Nie dziel przez zero"
#     finally:
#         print("operacja zakończona")
#
# print(dzielenie(2,2))