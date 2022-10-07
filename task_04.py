# 4 Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать
# в файл многочлен степени k.
#
# *Пример:*
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
file_ = open('new_file_task_04', 'w', encoding='utf-8')

varible_x = str(input('Введите степень: '))
rnd_varible_x = random.randrange(-10, 10)
first_num = random.randrange(-50, 50)
second_num = random.randrange(-50, 50)
third_num = random.randrange(-50, 50)

file_.write(f'{first_num} * x^{varible_x} + {second_num} * x^{rnd_varible_x} + {third_num} = 0 \n')
file_.write(f'x^{varible_x} + {third_num} = 0 \n')
file_.write(f'{first_num} * x^{varible_x} = 0 \n')
file_.close()

