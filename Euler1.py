#euler project1
#Anthony Scaglione

total = 0

for x in range(1000):
    if x%3==0 or x%5==0:
        total += x

print total
