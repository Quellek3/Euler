#Euler Project 4
#Anthony Scaglione

def isPalindrome(num):
    return str(num)==str(num)[::-1] #str(num)[::-1] iterates through backwards giving the reverse

largestPalin = 1
largestI = 1
largestJ = 1

for i in range(999,100,-1):
    for j in range(999,100,-1):
        if isPalindrome(i*j) and i*j>largestPalin: #brute force, going backwards
            largestPalin = i*j
            print "%i at i:%i and j:%i" % (largestPalin, i, j)  
            largestI = i
            largestJ = j
            if i==largestJ and j==largestI: #If this becomes true, no value after can possibly be larger, so script terminates
                quit() 


