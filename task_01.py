# Вычислить число π c заданной точностью d
#
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


num_pi = []
summ_ = 0
for i in range(0, 30):
    num_pi.append(1 / ((2 * i + 1) * (-3)**i))
    summ_ += num_pi[i]
num_pi_us = 2 * (3**0.5) * summ_
print('pi = ', num_pi_us)


num_us_d = float(input('Пример в вода значения d: 0.001 \n Введите d: '))
count = -1
num_pi_us = num_pi_us // num_us_d
while num_us_d <= 1:
    num_us_d *= 10
    count += 1
print(num_pi_us/(10**count))
