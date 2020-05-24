from numpy import arange

def sum(n):
    a = arange(n) ** 2 # square for each element in the array
    print(a)
    print(a.shape[0])
    b = arange(n) ** 4 # power(4) for each element in the array
    print(b)
    return a + b

print(sum(5))
