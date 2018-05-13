message = input("Enter message")

#print (message.count(' ')+1)

a = 0
wCount = 0
while a < len(message):
    if message[a] == ' ':
        wCount = wCount+1
    a = a+1

print (wCount+1)

