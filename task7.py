def retry_func_decorator(fff):
    def wrapper(*args, **kwargs):
        result = fff(*args, **kwargs)
        while result == 'Ошибка, попробуйте ещё раз':
            print("Число меньше 2")
            result = fff(*args, **kwargs)
        return result

    return wrapper

@retry_func_decorator
def function():
    x = 1
    while x < 2:
        print('Ошибка, попробуйте ещё раз')
        x += 1
    return 'Число больше или равно 2'

print(function())