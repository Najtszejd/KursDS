# # Otwórz plik
# fo = open("text.txt", "r")
# print("Nazwa pliku: ", fo.name)
#
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Ponownie ustaw wskaźnik na początek
# fo.seek(0, 0)  # fo.seek(0)
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Zamknij otwarty plik
# fo.close()

# Otwórz plik
fo = open("text.txt", "r")
print("Nazwa pliku: ", fo.name)

# Uzyskaj aktualną pozycję pliku.
pos = fo.tell()
print("Aktualna pozycja: " + str(pos))

line = fo.readline()
print("Czytaj linię: >" + line + "<")

# Uzyskaj aktualną pozycję pliku.
pos = fo.tell()
print("Aktualna pozycja: " + str(pos))

# Zamknij otwarty plik
fo.close()