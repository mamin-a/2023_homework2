def decor(function):
    def wrap(*args, **kwargs):
        result = function(*args, **kwargs)
        if isinstance(result, int):
            return result
        else:
            print("Неверный тип данных!")

    return wrap


@decor
def func_int(x):
    return x


print(func_int(2))
print(func_int(2.5))
