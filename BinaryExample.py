from collections import Counter
def count_args(func):
    def decorator(func):
        cache = dict()
        counter = dict()
        def wrapper(*args):
            counter[args] = counter.get(args,0) +1
            if args in cache:
                print(args,counter[args])
                return cache[args]
            else:
                result = func(*args)
                cache[args] = result
                return result
        return wrapper()
    return decorator()


def my_func(a,b):
    return a**b