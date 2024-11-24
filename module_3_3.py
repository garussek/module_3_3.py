def print_params(a = 1, b ="Строка", c = True):
    print(a, b, c)

print_params()                             # по умолчанию
print_params(9, "шарик", False)   # три аргумента
print_params(9, "шарик")             # два арумента
print_params(b = "15")                     # один аргумент

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = (23, "слово", [9, 8, 7])
values_dict = {"a":12, "b": "мяч", "c": None}
print_params(* values_list)
print_params(** values_dict)

values_list_2 = [54.32, "Строка"]
print_params(* values_list_2, 42)









