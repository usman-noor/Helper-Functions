def add(x,y):
    return x + y 
    
def mul(x,y):
    return x * y

def fn_factory(op,n):
    def opx(x):
        result = op(x,n)
        return result
    return opx

add2 = fn_factory(add,2)
mul5 = fn_factory(mul,5)

print(add2(5))
print(mul5(5))    
