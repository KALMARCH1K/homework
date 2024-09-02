def print_params(a=1, b='string', c=True):
    print(f'a: {a}, b: {b}, c: {c}')


print_params(a=1)
print_params(b='af', c=False)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params()
values_list = [0, 'yes', {'you': 'tube'}]
values_dict = {'a': 2, 'c': 'eeee', 'b': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
