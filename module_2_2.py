number = input('Введите 3 числа:').split()
first = number[0]
second = number[1]
third = number[2]
if first == second == third:
    print(3)
elif first == second or first == third or second == third or second == first:
    print(2)
elif second != first != third:
    print(0)