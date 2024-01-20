#Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.


# import random
# def calculate_product(lst):
#     product = 1
#     for element in lst:
#         product *= element
#     return product
#
# random_list = [random.randint(1, 10) for i in range(5)]
# print(f"Random list: {random_list}")
# product =calculate_product(random_list)
# print(f"Product of the list: {product}")

## Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.

# import random
# def find_min(lst):
#     return min(lst)
#
#
# random_list = [random.randint(1, 10) for i in range(5)]
# print(f"Random list: {random_list}")
#
# min_value = find_min(random_list)


## Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.

# import random
# def count_primes(lst):
#     """Підраховує кількість простих чисел у списку."""
#     def is_prime(n):
#         """Перевіряє, чи є число простим."""
#         if n < 2:
#             return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     prime_count = 0
#     for num in lst:
#         if is_prime(num):
#             prime_count += 1
#
#     return prime_count
#
# random_list = [random.randint(1, 20) for _ in range(10)]
#
# print(f"Random list: {random_list}")
#
# prime_count = count_primes(random_list)
#
# print(f"Number of prime numbers in the list: {prime_count}")

#Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів.

# def remove_elements_from_list(lst, target):
#     count_removed = 0
#
#
#     while target in lst:
#         lst.remove(target)
#         count_removed += 1
#
#     return count_removed
#
# my_list = [1, 2, 3, 4, 2, 5, 2, 6, 3]
# number_to_remove = 3
#
# result = remove_elements_from_list(my_list, number_to_remove)
#
# print(f"Список після видалення: {my_list}")
# print(f"Кількість видалених елементів: {result}")


# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.

# def merge_lists(list1, list2):
#     merged_list = list1 + list2
#     return merged_list
#
# first_list = [1, 2, 3]
# second_list = [4, 5, 6]
#
# result = merge_lists(first_list, second_list)
#
# print(f"Об'єднаний список: {result}")

## Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр, список також передається як параметр. Функція повертає новий список, який містить отримані результати.

# def calculate_power_of_elements(lst, power):
#     result_list = [x ** power for x in lst]
#     return result_list
#
#
# input_list = [2, 3, 4, 5]
# exponent = 3
#
# result = calculate_power_of_elements(input_list, exponent)
#
# print(f"Вхідний список: {input_list}")
# print(f"Ступінь {exponent} для кожного елемента: {result}")
