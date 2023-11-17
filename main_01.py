# Напишите функцию print_operation_table(operation, num_rows, num_columns),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows, num_columns):
    if num_rows > 2:
        for i in range(1, num_rows+1):
            print(*[operation(i,j) for j in range(1, num_columns+1)])
    else: print("ОШИБКА! Размерности таблицы должны быть больше 2!")

print_operation_table(lambda x, y: x * y, 3, 3)
print()
print_operation_table(lambda x, y: x + y, 4, 4)
# 1 2 3 4
# 2 4 5 6
# 3 5 6 7
# 4 6 7 8

print()
print_operation_table(lambda x, y: x - y, 5, 5)
# 1 2 3 4 5
# 2 0 -1 -2 -3
# 3 1 0 -1 -2
# 4 2 1 0 -1
# 5 3 2 1 0

print()
print_operation_table(lambda x, y: x / y, 4, 4)
# 1 2 3 4
# 2 1.0 0.6666666666666666 0.5
# 3 1.5 1.0 0.75
# 4 2.0 1.3333333333333333 1.0