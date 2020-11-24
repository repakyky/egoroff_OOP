from time import perf_counter

def timer():
    start = perf_counter()

    def inner():
        nonlocal start

        difference = perf_counter() - start
        start = perf_counter()
        return difference

    return inner