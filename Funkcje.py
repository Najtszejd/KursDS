# def simple_function():
#     print('Hello world!')
#     print('Wikipedia')
#
#
# simple_function()
#
# def my_function():
#     return 3+3
#
#
# print(my_function())
def fibbonaci_numbers(n):
    ''' zwraca liczby Fibonacciego mniejsze od n '''
    wynik = []
    a, b = 0, 1
    while a < n:
    # while len(wynik) < n:
        wynik.append(a)
        a, b = b, a+b
    return wynik