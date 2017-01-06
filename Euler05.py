#Euler project 5
#Anthony Scaglione

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return (a*b)/gcd(a, b)

currentLcm=1

for i in range(1,21): #Finds least common multiple of 1 then finding the lcm of that result with 2, and so on up to 20
    currentLcm=lcm(i,currentLcm)

print currentLcm
