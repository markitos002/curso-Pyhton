import time

def measure_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"La función {func.__name__} tardó {end-start} segundos en ejecutarse.")
    return wrapper

@measure_time
def my_function():
    print("Hello, world!")
    time.sleep(1)   

my_function()

"""
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function.")
    return wrapper


@announce
def hello():
    print("Hello, world!")

hello()

"""
