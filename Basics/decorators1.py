# Timing Function Execution
# Write a decorator that measures the time a function takes to execute

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__}: Execution time: {end-start}")
        return result
    return wrapper
# if we want to make decorator we need to make function inside function and return the wrapper function

@timer
def example_function(n):
    time.sleep(n)

example_function(2)