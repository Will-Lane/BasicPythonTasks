Numbers=[]
A=0
currentLargest=0

prevLargest = 0
while A!= -1:
    A = int(input("enter number"))

    if A >=0:
        Numbers.append(A)
        if A>currentLargest:
            prevLargest = currentLargest
            currentLargest = A
        elif A>prevLargest:
            prevLargest=A


print (Numbers)
print (currentLargest)
print(prevLargest)