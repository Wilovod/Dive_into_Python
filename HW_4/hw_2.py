# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def create_argument_dictionary(**kwargs):
    result = {}
    for arg_name, arg_value in kwargs.items():
        key = arg_value if hashable(arg_value) else str(arg_value)
        result[key] = arg_name
    return result

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

arg_dict = create_argument_dictionary(age=36, name='Dima', name_str=[1, 2, 3])
print(arg_dict)