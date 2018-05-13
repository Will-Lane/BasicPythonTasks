message = input("input message")

a1 = len(message)-1
a2= len(message)
while a1 >= 0:
    if message[a1] == ' ':
        print (message[a1+1:a2])
        a2=a1+1

    a1=a1-1
print(message[0:a2])

