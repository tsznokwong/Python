def fib(x):
    if x<2 :
        return 1
    else:
        return fib(x-1)+fib(x-2)
x=input('fib: x:\n')
print(fib(x-2))