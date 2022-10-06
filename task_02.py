# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
#
# *Пример*
# - при N=236     ->        [2, 2, 59]

num_us_n = int(input('Введите число N: '))
list_prime_num_us = []
count = 0
list_prime = [2, 3, 5, 7, 11]

for i in range(len(list_prime)):
    while num_us_n % list_prime[i] == 0:
        list_prime_num_us.append(count)
        list_prime_num_us[count] = list_prime[i]
        num_us_n //= list_prime[i]
        count += 1
else:
    list_prime_num_us.append(int(num_us_n))
print(list_prime_num_us)


