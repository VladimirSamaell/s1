first = 123
second = 321
third = 321
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third or second == second:
    print(2)
elif first != second and first != third:
    print(0)