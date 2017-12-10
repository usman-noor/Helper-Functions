def raise_if_not_allowed_values(arguments, floats=True, ints=True):
    print("Invoked with {}, {}".format(floats, ints))
    for arg in arguments:
        if type(arg) != int:
            raise ValueError('Invalid param. Only Ints allowed')

class build_improved_op(object):
    def __init__(self, floats=True, ints=True):
        self.floats = floats
        self.ints = ints

    def __call__(self, op):
        def Ioperation(*args, **kwargs):
            raise_if_not_allowed_values(args, self.floats, self.ints)
            return op(*args, **kwargs)
        return Ioperation


# add = build_improved_op(add)
@build_improved_op(floats=False)
def add(*args):
    "Receives numbers and returns the sum"
    return sum(args)

print(add(2, 3))
