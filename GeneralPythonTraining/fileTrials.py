inputF = open("data1.txt",mode ="r")
nFile = open("data2.txt","w")
outputF = open("data2.txt","a")

difference = ord('a')-ord('A')
search = str(input("What would you like to search for?"))
replace = str(input())
lenSearch = len(search)
firstLetter = search[0]
numSearchFound = 0

for x in inputF:
    a = 0
    while a<len(x):
        if a+lenSearch < len(x):
            checkMatch = 0
            if ord(x[a]) == ord(firstLetter) or ord(x[a]) == ord(firstLetter) + difference or ord(x[a]) == ord(firstLetter) - difference:
                for i in range (0,lenSearch):
                    if ord(x[a+i]) == ord(search[i]) or ord(x[a+i]) == ord(search[i]) + difference or ord(x[a+i]) == ord(search[i]) - difference:
                        checkMatch = checkMatch+1
                if checkMatch == lenSearch:
                    numSearchFound = numSearchFound+1
        a=a+1

print(search + " = " + str(numSearchFound))