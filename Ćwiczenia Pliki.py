# Ćwiczenie
# Napisz program w Pythonie, aby odczytać i wyświetlić cały plik tekstowy.

# plik = open("text.txt","r")
# print(plik.read())

# Ćwiczenie
# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu i zapisze go na liście content_list.
# content_list to lista zawierająca przeczytane wiersze.
# Możesz skorzystać z podpowiedzi (podanej dalej).

# content_list = []
# with open("text.txt","r") as file:
#     for i in file:
#         content_list.append(i)
# print(content_list)
# print(content_list[0])

# Ćwiczenie
# Napisz program w Pythonie, który znajdzie najdłuższe słowa w pliku tekstowym.

# with open("text.txt","r") as plik:
#     content = plik.read()
# content_list = content.split()
# word = content_list[0]
# for i in content_list[1:]:
#     if len(content_list) <= len(i):
#         word = i
# print(i)

# Ćwiczenie
# Napisz program w Pythonie, który zapisze listę do pliku.
#
# wpis_do_pliku = [1,2,3,4,5,"koniec"]
#
# with open("text.txt","a") as file:
#     file.write(str(wpis_do_pliku))

# plik = open("text.txt","r")
# # plik.close()
# if plik.closed is True:
#     print("zamknięty")
# else:
#     print("Nie zamknięty - zamykam")
#     plik.close()
# print(plik.closed)

# Zadanie dom
# Napisz program, który otworzy plik sonety.txt i sprawdzi liczbę słów w całym tekście
# Dodatkowo, napisz funkcję, która zlicza słowa tylko w co 7 linijce tekstu

# words = 0
# with open("sonety.txt","r",encoding="utf8") as file:
#     file_word = file.read().split(" ")
#     for i in file_word:
#         words +=1
# print("\nW pliku {} znajduje się {} słów \n".format("sonety.txt",words))
#
# # funkcja licząca słowa w co 7 linii
# # file_check = input("Podaj nazwe pliku wraz z odpowiednim rozszerzeniem ")
# def file_lanes(file_check):
#     count = 0                                                # licznik linii
#     with open(file_check,"r",encoding="utf8") as file_lanes: # otwieramy plik, argument = nazwa pliku z rozszerzeniem
#         lanes = file_lanes.readlines()                       # przypisujemy do zmiennej każda linie pliku
#     for lane in lanes:                                       # pętla, która przechodzi przez każda linie w tekscie
#         count += 1                                           # licznik liczący linie
#         if count % 7 == 0:                                   # jeśli licznik dzieli się przez 7 to działamy dalej
#             count_word = 0                                   # ustawiamy i resetujemy licznik słow
#             lane_count = lane.split(" ")                     # dzielimy aktualną linie na ze względu na spacje (oddzielamy słowa)
#             for i in lane_count:                             # pętla przechodząca przez każde słowo w linii
#                 count_word +=1                               # zwięszkenie licznika słow
#             print("Linia {} brzmi: \n{} ----> zawiera {} słów\n".format(count, lane, count_word))   #komunikat
# print(file_lanes("sonety.txt"))                               # test funkcji, można wykorzystać na dowolnym pliu