"""Создайте массив, содержащий пять чисел (два из которых
должны повторяться). Выведите весь массив. Предложите
пользователю ввести одно из чисел массива, после чего 
выведите сообщение, в котором указано, сколько раз число
встречается в этом массиве."""

from array import *

array_new = array("i", [54, 44, 89, 54, 92])
print(array_new)
num1 = int(input("Plese enter number: "))
print(array_new.count(num1))