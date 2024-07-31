print('1st program')    # Task 1
print((9**0.5)*5)

print('2nd program') # Task 2
print(9.99>9.98 and 1000!=1000.1)

print('3rd program') # Task 3
print(1234, 1234%1000, 234//10)
print(5678, 5678%1000, 678//10)
print(23+67)

print('4th program') # Task 4
num1 = 13.42
num2 = 42.13

int_part1 = int(num1)
print(int_part1)
frac_part1 = int((num1-int_part1)*100)
print(frac_part1)
int_part2 = int(num2)
print(int_part2)
frac_part2 = int((num2-int_part2)*100)
print(frac_part2)
print(int_part1 == frac_part2) or (int_part2 == frac_part1)