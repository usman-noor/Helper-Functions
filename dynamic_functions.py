def fn_factory(n):
    def addx(x):
        return x + n 
    return addx

add2 = fn_factory(2)

print(add2(5))
