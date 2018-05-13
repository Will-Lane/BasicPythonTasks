message = input("input message")
# message = message.upper()
count = ord('A')
difference = ord('a')-ord('A')


nLetters=[0 for i in range (26)]

while count <= (ord('A')+25):
    letters = 0
    messageCount = 0
    while messageCount < (len(message)):
        if (message[messageCount]) == chr(count) or (message[messageCount]) == chr(count+difference):
            letters = letters + 1.
        messageCount = messageCount+1

    if letters > 0:
        nLetters[count-(ord('A'))] = nLetters[count-(ord('A'))] + 1


    count = count+1
print(nLetters)


