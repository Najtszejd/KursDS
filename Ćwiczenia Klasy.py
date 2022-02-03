# class Parrot:
#
#     # atrybuty instancji
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # metoda instancji
#     def sing(self, song):
#         return self.name + " śpiewa " + song
#
#     def dance(self):
#         return self.name + " teraz tańczy"
#
#
# 6: 50
# # utworzenie wystąpienia obiektu
# blu = Parrot("Blu", 10)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Cześć, mam na imię " + self.name, "i mam ", self.age, "lat")
# p1 = Person("Jan",36)
# print(p1.myfunc())
# p1.age = 40
# print(p1.myfunc())
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Cześć, mam na imię " + self.name, "i mam ", self.age, "lat")
# p1 = Person("Jan",36)
# print(p1.myfunc())
# p1.age = 40
# print(p1.myfunc())
# # del p1.age
# # print(p1.myfunc())

# Ćwiczenie: Klasa o nazwie MyClass z atrybutem o nazwie x
# No to jeszcze raz! Utwórz klasę o nazwie MyClass z atrybutem o nazwie x = 5.
# Teraz użyj klasy o nazwie MyClass do stworzenia obiektu.
# Utwórz obiekt o nazwie p1 i wydrukuj wartość x.
#
# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)


# # Ćwiczenie
# # Utwórz klasę Vehicle bez żadnych zmiennych i metod.
# class Vehicle:
#     pass
# Ćwiczenie
# Klasa (class) dotycząca wyimaginowanego inwentarza odrzutowca
# jest już dla Was zdefiniowana. Również instancja tej klasy Jets jest stworzona
# i przypisana do zmiennej first_item. Wydrukuj name z first_item.
# class Jets:
#
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
#
# first_item = Jets("F16", "USA")
#
#
# a= first_item.name
# print(a)

#
# Ćwiczenie
# Tym razem wydrukuj origin z first_item.

# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
#
# first_item = Jets("F16", "USA")
#
# a=first_item.name
# b=first_item.origin
#
#
# print(a,b)

# Ćwiczenie
# Utwórz klasę Vehicle z atrybutami instancji max_speed i mileage.
# Stwórz obiekt i w trakcie inicjacji przypisz jego atrybutom (odpowiednio) wartości 240 i 18.
# Wydrukuj te atrybuty.

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.maxspeed = max_speed
#         self.mileage = mileage
# pojazd = Vehicle(240,18)
# print("Speed = ",pojazd.maxspeed,"Mileage = ",pojazd.mileage)
# Ćwiczenie
# Utwórz klasę Car z dwoma atrybutami instancji:
# .color, który przechowuje nazwę koloru samochodu jako ciąg testowy (str)
# .mileage, który przechowuje liczbę kilometrów przejechanych przez samochód jako liczbę całkowitą (int)
# Następnie utwórz instancję dwóch obiektów Car - niebieski samochód mający 20 000 kilometrów przebiegu
# i czerwony samochód mający 30 000 kilometrów przebiegu - i wydrukuj ich kolory oraz przebiegi.
# Twój wynik powinien wyglądać następująco:
# Niebieski samochód ma 20,000 kilometrów przebiegu.
# Czerwony samochód ma 30,000 kilometrów przebiegu.

# class Car:
#     def __init__(self,color, mileage):
#         self.color = str(color)
#         self.mileage = int(mileage)
# blue_car = Car(color = "Niebieski",mileage = "20000")
# red_car = Car(color = "Czerwony",mileage ="30000")
# green_car = Car(color ="Zielony",mileage ="15000")
# for cars in blue_car,red_car,green_car:
#     print("{} samochód ma {} kilometrów przebiegu".format(cars.color,cars.mileage))
# # print("{} samochód ma {} kilometrów przebiegu".format(blue_car.color,blue_car.mileage))
# # print("{} samochód ma {} kilometrów przebiegu".format(red_car.color,red_car.mileage))
# # print("{} samochód ma {} kilometrów przebiegu".format(green_car.color,green_car.mileage))

# Ćwiczenie
# Stwórz nowe instancje od pierwszej do szóstej pozycji w tej kolejności:
# F14, SU 33, AJS37, Mirage 2000, Mig 29, A10. Możesz sprawdzić Podpowiedź 1, aby sprawdzić origin.
# Wskazówka 1
# SU33: Rosja
# AJS37: Szwecja
# Mirage2000: Francja
# F14: USA
# Mig29: ZSRR
# A10: USA
# first_item=Jets(name, country)
# class Jets:
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#     def info(self,jet):
#         print(self.name, self.origin)
#         print(jet.name, jet.origin)
#
# first_item= Jets("F14","USA"),
# second_item= Jets(name ="SU33", country= "Rosja"),
# third_item= Jets(name = "AJS37", country="Szwecja"),
# fourth_item=Jets(name = "Mirage2000", country= "Francja"),
# fifth_item=Jets("Mig29","ZSRR"),
# sixth_item=Jets("A10","USA")



# first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
#
#
# print(first_army)
# first_item.info(fifth_item)

# Ćwiczenie
# Dodaj kolejny atrybut o nazwie „quantity” do metody inicjalizacji
# (zwykle nazywanej konstruktorem lub __init__).
# Następnie zdefiniuj przypisanie tego atrybutu do atrybutu self.quantity wewnątrz konstruktora.
# Następnie utwórz 2 instancje dla: F14 i Mirage2000 z ilościami 87 i 35.
# Wskazówka 1
# Możesz dodać parametr quantity do konstruktora w następujący sposób:
# def __init__(self, name, country, quantity):
# Następnie musisz przypisać ten parametr do atrybutu self, aby istniało sensowne połączenie między parametrem a atrybutem.
# Wskazówka 2
# Możesz dodać parametr quantity do konstruktora w następujący sposób:
# def __init__(self, name, country, quantity):
#
#     self.name = name
#     self.origin = country
#     self.quantity = quantity
# Następnie musisz przypisać ten parametr do atrybutu self, aby istniało sensowne połączenie między parametrem a atrybutem.
# Wskazówka 3
# Możesz tworzyć instancje klasy Jets jak poniżej:
# first_item=Jets("F14","USA",87)
# second_item=Jets("Mirage2000","France",35)
# class Jets:
#     def __init__(self, name, country,quantity):
#         self.name = name
#         self.origin = country
#         self.quantity = quantity
#
# first_item= Jets("F14","USA",87)
# second_item= Jets("Mirage2000","France",35)
# a = Jets("MIG29", "ZSRR", 10)
# b = Jets("SU33", "Rosja", 15)
# suma = [first_item,second_item,a,b]
# # total= first_item.quantity+second_item.quantity
# ilosc = 0
# for i in suma:
#     ilosc +=i.quantity
# print(ilosc)

import math


class Figura:
    def obwod(self):  # L
        """Obliczanie obwodu."""
        raise NotImplementedError

    def pole(self):  # S/P
        """Obliczanie pola powierzchni."""
        raise NotImplementedError


# 1. Koło
# Ćwiczenie
class Kolo(Figura):
    def __init__(self, r):
        self.r = r
    def obwod(self):
        return 2 * math.pi * self.r
    def pole(self):
        return math.pi * self.r ** 2

f = Kolo(5)
# print(f.obwod())
# print(f.pole())

# 2. Trójkąt równoboczny

class trojkat(Figura):
    def __init__(self, bok):
        self.bok = bok
    def obwod(self):
        return self.bok * 3
    def pole(self):
        return 0.433 * self.bok **2
t = trojkat(5)
# print(t.obwod())
# print(t.pole())

# 3. Prostokąt

class Prostokat(Figura):
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def obwod(self):
        return 2 * self.a + 2 * self.b
    def pole(self):
        return self.a * self.b
p = Prostokat(2,5)
# print(p.obwod())
# print(p.pole())

class Kwadrat(Prostokat):
    def __init__(self,a):
        self.a = a
        self.b = a

k = Kwadrat(5)
# print(k.obwod())
# print(k.pole())

class Rbk(Prostokat):
    def __init__(self,a,b,h):
        self.a,self.b,self.h = a,b,h
    def obwod(self):
        return 2*self.a + 2*self.b
    def pole(self):
        return self.a * self.h
r = Rbk(2,4,5)
# print(r.obwod())
# print(r.pole())

class Trapez(Figura):
    def __init__(self,a,b,h):
        self.a,self.b,self.h = a,b,h
        d = a -b
        self.c = (h**2+d**2)**0.5
    def obwod(self):
        return self.a + self.b + self.c
    def pole(self):
        return 0.5 * (self.a + self.b) * self.h
t = Trapez(4,6,5)
# print(t.obwod())
# print(t.pole())

# Ćwiczenie
# Utwórz podrzędną klasę Bus, która odziedziczy wszystkie zmienne i metody klasy Vehicle
# Utwórz obiekt klasy Bus, która dziedziczy wszystkie zmienne i metody klasy Vehicle i wyświetli je.
# Dane wejściowe:
# Nazwa pojazdu: Szkolne Volvo Prędkość: 180 Przebieg: 12
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# class Bus(Vehicle):
#     pass
# bus = Bus("Volvo",180,12)
# print("Szkolne {} Prędkość: {} Przebieg: 12 ".format(bus.name, bus.max_speed, bus.mileage))
#
# Ćwiczenie
# Utwórz klasę Bus, która dziedziczy po klasie Vehicle.
# Podaj argument pojemności w metodzie Bus.seating_capacity() o domyślnej wartości 50.
# Dane wejściowe:
# Użyj poniższego kodu dla swojej nadrzędnej klasy Vehicle.
# Musisz przesłonić/nadpisać metodę - w klasie pochodnej na
# specyficznie zaimplementować metodę która została już zdefiniowana w klasie bazowej.
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"Liczba miejsc siedzących w {self.name} to {capacity} pasażerów"
# class Bus(Vehicle):
#     def seating_capacity(self, capacity = 50):
#         return super().seating_capacity(capacity)
#
#
# bus = Bus("Szkolne Volvo", 180, 12)
# print(bus.seating_capacity(100))
# print(bus.seating_capacity())  # Brak domyślnej wartości
# # Oczekiwany wynik:
# # Liczba miejsc siedzących w Szkolne Volvo to 50 pasażerów

# Ćwiczenie
# Zdefiniuj atrybut (właściwość), który powinna mieć taką samą wartość dla każdej instancji klasy
# Zdefiniuj atrybut klasy „color” z domyślną wartością biały. Oznacza to, że każdy Vehicle (pojazd) powinien być biały.
# Użyj poniższego kodu do tego ćwiczenia.

# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#     kolor = "Biały"
#
# class Bus(Vehicle):
#     kolor = "Czerwony"
#
# class Car(Vehicle):
#     pass
#
#
# bus = Bus("Volvo",180,12)
# car = Car("Audi Q5", 240, 18)
# # Kolor: Biały, Nazwa pojazdu: Szkolne Volvo, Prędkość: 180, Przebieg: 12
# # Kolor: Biały, Nazwa pojazdu: Audi Q5, Prędkość: 240, Przebieg: 18
# print(bus.kolor)
# print(car.kolor)

# Dziedziczenie klas
# Ćwiczenie
# Dane:
# Utwórz podrzędną klasę Bus, która dziedziczy po klasie Vehicle.
# Domyślna opłata za przejazd dla dowolnego pojazdu to liczba miejsc * 100.
# Natomiast jeśli School_bus to instancja klasy Bus, musimy dodać
# dodatkowe 10% do pełnej ceny jako opłatę za utrzymanie.
# Tak więc łączna opłata za przejazd autobusem stanie się ostateczną
# kwotą = opłata całkowita + 10% ceny całkowitej.
# Uwaga: autobus może pomieścić 50 osób,
# więc ostateczna kwota taryfy powinna wynosić 5500.
# Musisz zastąpić metodę fare() klasy Vehicle w klasie Bus.
# Użyj poniższego kodu dla swojej nadrzędnej klasy
# Vehicle. Musimy uzyskać dostęp do klasy nadrzędnej z wnętrza metody klasy potomnej.

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         return super().fare()*1.1
#
# School_bus = Bus("Szkolne Volvo", 12, 50)
# print("Całkowita opłata za przejazd autobusem wynosi:", School_bus.fare())
# Vehicle = Vehicle("Zwykły samochód", 20,50)
# print(Vehicle.fare())

# Ćwiczenie
# Określ, do której klasy należy dany obiekt Bus (sprawdź typ obiektu)
# Dane:
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("Szkolne Volvo", 12, 50)
#
# print(type(School_bus))
#
# # Ćwiczenie 1
# # Napisz klasę (class) Rectangle w języku Python, umożliwiając zbudowanie prostokąta z atrybutami długości (length) i szerokości (width).
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
# # Ćwiczenie 2
# # Utwórz metodę perimeter(), aby obliczyć obwód prostokąta i metodę area(), aby obliczyć powierzchnię prostokąta.
#     def parimeter(self):
#         return 2*(self.length+self.width)
#     def area(self):
#         return self.length*self.width
# # Ćwiczenie 3
# # Utwórz metodę display(), która wyświetla długość, szerokość, obwód i obszar obiektu utworzonego przy użyciu instancji klasy Rectangle.
#     def display(self):
#         print("Obwód: ", self.parimeter())
#         print("Pole: ", self.area())
#         print("Length: {} Width: {}".format(self.length,self.width))
#
# # Ćwiczenie 4
# # Utwórz klasę potomną Parallelepipede dziedziczącą po klasie
# # Rectangle oraz z atrybutem wysokości (height) i metodą volume() w celu obliczenia objętości równoległościanu (Parallelepipede).
#
# class Parallelepipede(Rectangle):
#     def __init__(self,length, width, height):
#         super().__init__(length, width)
#         self.height = height
#     def volume(self):
#         return self.length * self.width * self.height
#
# kwadrat = Rectangle(10,2)
# prostopadloscian = Parallelepipede(7,6,5)
# kwadrat.display()
# prostopadloscian.display()
# print(prostopadloscian.volume())

# Zadanie 1
# Sprawdź czy cały interfejs klasy bazowej KontoBankowe znajduje się i działa w instancji klasy pochodnej KontoDebetowe.

class KontoBankowe:
    def __init__(self, nazwa, stan=0):
        self.nazwa = nazwa
        self.stan = stan

    def info(self):
        print("nazwa:", self.nazwa)
        print("stan:", self.stan)

    def wyplac(self, ilosc):
        self.stan -= ilosc

    def wplac(self, ilosc):
        self.stan += ilosc

class KontoDebetowe(KontoBankowe):
    def __init__(self, nazwa, stan=0, limit=0):
        KontoBankowe.__init__(self, nazwa, stan)
        self.limit = limit

    def wyplac(self, ilosc):
        """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
        if (self.stan - ilosc) < (-self.limit):
            print("Brak srodkow na koncie")
        else:
            KontoBankowe.wyplac(self, ilosc)

# osoba = KontoDebetowe("Andrzej", stan= 1000, limit = 500)
# osoba.info()
# osoba.wplac(500)
# osoba.info()
# osoba.wyplac(1000)
# osoba.info()

# Zadanie 2
# Przetestuj teraz działanie klasy KontoDebetowe.

class A:
    """Rodzic pierwszy"""

    def __init__(self):
        super().__init__()
        self.a = "A"

    def f(self):
        print("a:", self.a)


class B:
    """Rodzic drugi"""

    def __init__(self):
        super().__init__()
        self.b = "B"

    def f(self):
        print("b:", self.b)


class Pochodna(A, B):
    """Dziecko"""

    def __init__(self):
        super().__init__()

d = Pochodna()
print(d.a)
print(d.b)
d.f()

# Zadanie 3
# W klasach A i B zmień nazwy metod fa() i fb() na f().
# Sprawdź jak zachowa się teraz wywołanie d.f(), gdzie d jest instancją klasy pochodnej.
# Jak na to zachowanie wpływa zmiana kolejności rodziców przy definicji klasy pochodnej class Pochodna(tutaj_kolejnosc)?

# Klasa pochodna dziedziczy od rodzica, który zostanie podany w pierwszej kolejności
print(type(d.a))