#Euler project2
#Anthony Scaglione

total = 0
fib1 = 1
fib2 = 1

while total <= 4000000:
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp
    if temp%2==0:
        total += temp

print total
