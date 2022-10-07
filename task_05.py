# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными.
# Степени многочленов могут отличаться.

def count_str(str):
    count = []
    for i in range(len(str)-1):
        if '-' == str[i] or i == 0:
            if i > 0 and '^' == str[i - 1]:
                i += 1
            elif i == 0 and '-' != str[i]:
                count.append(str[i])
            else:
                count.append(str[i] + str[i + 1])
        elif '^' == str[i]:
            if '-' == str[i + 1]:
                count.append(str[i] + str[i + 1] + str[i + 2])
            else:
                count.append(str[i] + str[i + 1])
        elif '+' == str[i]:
            if '-' == str[i + 2]:
                count.append(str[i + 2] + str[i + 3])
            else:
                count.append(str[i + 2])
    return(count)


file_first = open('new_file_task_05_first', 'r', encoding='utf-8')
file_second = open('new_file_task_05_second', 'r', encoding='utf-8')

list_file_first = str(file_first.read())
list_file_second = str(file_second.read())

count_1 = count_str(list_file_first)
count_2 = count_str(list_file_second)

if len(count_1) > len(count_2):
    for k in range(len(count_1) - 1):
        if count_1[k] == count_1[k+1]:
            index = k
    count_1.pop(index)
elif len(count_1) < len(count_2):
    for k in range(len(count_2) - 1):
        if count_2[k] == count_2[k+1]:
            index = k
    count_2.pop(index)

count_3 = []
for i in range(len(count_1)):
    if count_1[i] == count_2[i]:
        count_3.append(count_1[i])
    else:
        num1 = int(count_1[i])
        num2 = int(count_2[i])
        count_3.append(num1 + num2)

file_ = open('new_file_task_05_third', 'w', encoding='utf-8')
file_.write(f'{count_3[0]} * x{count_3[1]} + {count_3[2]} * x^{count_3[3]} + {count_3[4]} = 0 \n')
file_.close()

