def func(*args):
    value = []

    for item in args:
        if isinstance(item, str):
            value.append(item)

    return value


final = func(1, 3, 'slovo', "Python")

print(final)
