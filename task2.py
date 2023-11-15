numbers = [1,3,4,5,6,8,9,27]

a = 3

print(list(filter(lambda x: x % a == 0, numbers)))
