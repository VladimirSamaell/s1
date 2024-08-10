numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for num in numbers:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                not_prime.append(num)
                break
        else:
            prime.append(num)
    else:
        not_prime.append(num)
print('Primes:', prime)
print('Not Primes:', not_prime)