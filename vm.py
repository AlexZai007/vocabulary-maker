# -*- coding:utf -8 -*-
#!/usr/bin/python3


#bvgjhnbhe.v ,b,kbjntrb
import sys
import random
from termcolor import colored
import collections
from prettytable import PrettyTable


#задаем переменные
chars = input(colored("Ведите все используемые символы для создания пароля: "+"\n", 'red'))
length = input(colored('длина пароля?'+ "\n", 'red'))
length = int(length)
number = (len(chars)**length)
 


 #выводим макс числовых комбиныций и ждем согласия пользователя
my_file = open("parser.txt", "w")
start = input(colored(str(number) + " - цифровых комбинаций (НАЖМИТЕ ENTER для продолжения)" + '\n', 'red'))

#задаем переменную для чистого словаря
l= []

#главный процесс
# рандом и хардкор :)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
        l.append(password)
    print(password)
    my_file.write(password + "\n")

my_file.close()
#закрыли файл с неочищенными паролями





#открыли файл для очистки
f = open("cp.txt", 'w')

l = (list(set(l)))

f.write(str(l) + "\n")

#записали файл 
#моя подпись

print ("Made By AlexZai")




# программа завершенна