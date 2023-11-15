import time

def time_of_function(f):
    def wrap(*args):
        start_time = time.perf_counter()
        #start_time_ns = time.perf_counter_ns()
        result = f(*args)
        print("Время вычислений,с:",time.perf_counter() - start_time)
        #print("Время вычислений,нс:", time.perf_counter_ns() - start_time_ns)
        return result
    return wrap

@time_of_function
def func(x):
    return x**2


print("Результат выполнения функции =",func(4))