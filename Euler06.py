#Euler project 6
#Anthony Scaglione

numSquare = 0
numSum = 0

for i in range(1,101):
    numSquare+=i**2
    numSum+=i

numSum*=numSum

print numSum-numSquare

