inputFile = open("data1.txt",mode ="r")
newFile = open("data2.txt","w")
replaceFile = open("data2.txt","a")
#outputF = open("data3.txt","a")

difference = ord('a')-ord('A')
search = str(input("What would you like to search for?"))
replace = str(input("Replace with?"))
lenReplace = len(replace)
lenSearch = len(search)
firstLetter = search[0]


tempStoreStringLine = " "
storeNewFile = list()

for x in inputFile:
    startReplace=list()
    a = 0
    numSearchFound = 0
    while a<len(x):
        if a+lenSearch < len(x):
            #print(a)
            checkMatch = 0
            if ord(x[a]) == ord(firstLetter) or ord(x[a]) == ord(firstLetter) + difference or ord(x[a]) == ord(firstLetter) - difference:
                for i in range (0,lenSearch):
                    if ord(x[a+i]) == ord(search[i]) or ord(x[a+i]) == ord(search[i]) + difference or ord(x[a+i]) == ord(search[i]) - difference:
                        checkMatch = checkMatch+1

                if checkMatch == lenSearch:
                    numSearchFound = numSearchFound+1
                    startReplace.append(a)

        a = a + 1

    tempStoreStringLine = " "
    if numSearchFound >= 1:
        for i in range(0, len(x)):
            for j in range(0, numSearchFound):
                if i == startReplace[j]:
                    tempStoreStringLine = tempStoreStringLine + replace + " "
                elif i < startReplace[j]:
                    tempStoreStringLine = tempStoreStringLine + x[i] + " "

                elif i > startReplace[j] + lenSearch:
                    tempStoreStringLine = tempStoreStringLine + x[i]
        print(tempStoreStringLine, file = replaceFile, end ="", sep = "")
    else:
        for i in range(0, len(x)):
            tempStoreStringLine = tempStoreStringLine + x[i]
        print(tempStoreStringLine, file=replaceFile, end = "", sep = "")


    storeNewFile.append(tempStoreStringLine)

    startReplace = list()

