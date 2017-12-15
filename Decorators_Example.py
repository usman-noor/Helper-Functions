#decorators tutorial
#https://www.youtube.com/watch?time_continue=53&v=FsAPt_9Bf3U

#decorators with timeout
#https://stackoverflow.com/questions/2281850/timeout-function-if-it-takes-too-long-to-finish

from functools import wraps
def raise_if_not_ints(*args):
    for arg in args:
        if type(arg) != int:
            raise ValueError('Invalid param. Only Ints allowed')


def build_improved_op(op):
    @wraps(op)
    def Ioperation(*args, **kwargs):
        "Does nasty things with your CPU"
        raise_if_not_ints(*args)
        return op(*args, **kwargs)

    # Ioperation.__name__ = op.__name__
    # Ioperation.__doc__ = op.__doc__ 
    return Ioperation


# add = build_improved_op(add)
@build_improved_op
def add(*args):
    "Receives numbers and returns the sum"
    return sum(args)

help(add)

"""
print(add(2, 3, 4, 8, 8))
print(add(2, 3))

@build_improved_op
def square(x):
    return x ** 2

print(square('a'))

"""










"""
@build_improved_op
def multiply(x, y):
    return x * y

# multiply = build_improved_op(multiply)

@build_improved_op
def subtract(x, y):
    return x - y

# subtract = build_improved_op(subtract)


res1 = add('ab','cd')
print(res1)

res2 = multiply(2, 'a')
print(res2)


"""
