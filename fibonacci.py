
fib1 = 0
fib2 = 1

for i in range(20):

    
    print(str(i+1) + '. Fibonacciarv on ' + str(fib1))

    fib = fib1 + fib2

    fib1 = fib2
    fib2 = fib
