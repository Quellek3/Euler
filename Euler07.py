#Euler project 7
#Anthony Scaglione

goal=10001
index=1
isPrime=True
primeList=[2]
i=0

while len(primeList)<goal: #Adds found primes to list, then uses known primes to check for new primes
    index+=2
    i=0
    isPrime=True
    while(primeList[i]**2 <= index): #limits checks to highest possible factor
        if index%primeList[i]==0: #If this passes, number is not prime
            isPrime=False
            break
        i+=1
    if isPrime:
        primeList.append(index)
        print index
