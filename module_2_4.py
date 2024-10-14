numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Исходный список чисел от 1 до 15
not_primes = []  # Список для хранения чисел, которые не являются простыми
primes = []  # Список для хранения простых чисел

for  i in numbers:
    if  i < 2:
        continue
    is_prime = True
    for div in range(2, i):
        if  i % div == 0:   
            not_primes.append( i)
            is_prime = False
            break
    if is_prime:
     print(primes)
     print(not_primes)
