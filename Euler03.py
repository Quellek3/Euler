#Euler 3 Project
#Anthony Scaglione
#
#Ty based stack exchange http://math.stackexchange.com/questions/187061/find-the-largest-prime-factor

a=600851475143L
b=2
c=1

while a!=b:
    if a%b==0:
        c=b
        a/=b
    else:
        b+=1

print a


