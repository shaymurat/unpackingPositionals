def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print('-------- 1. Функция с параметрами по умолчанию ---------')
print('print_params() =>                         ', end='')
print_params()
print("print_params('one', 'two', 'three') =>    ", end='')
print_params('one', 'two', 'three')
print("print_params(False, True) =>              ", end='')
print_params(False, True)
print("print_params(b=25) =>                     ", end='')
print_params(b=25)
print("print_params(c=[1, 2, 3]) =>              ", end='')
print_params(c=[1, 2, 3])
print()

print('--------------- 2. Распаковка параметров ---------------')
values_list = ['number', 1, True]
values_dict = {'a': 2, 'b': 'line', 'c': False}
print('print_params(*values_list) =>             ', end='')
print_params(*values_list)
print('print_params(**values_dict) =>            ', end='')
print_params(**values_dict)
print()

print('--------- 3. Распаковка + отдельные параметры ----------')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
