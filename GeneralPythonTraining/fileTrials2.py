inputF = open("data1.txt",mode ="r")
nFile = open("data2.txt","w")
outputF = open("data2.txt","a")

difference = ord('a')-ord('A')
search = str(input("What would you like to search for?"))
lenSearch = len(search)
firstLetter = search[0]
numSearchFound = 0
checkMatch = 0

for x in inputF:
    a = 0

    while a<len(x):
        if a+lenSearch < len(x):
            if ord(x[a]) == ord(firstLetter) or ord(x[a]) == ord(firstLetter) + difference or ord(x[a]) == ord(firstLetter) - difference:
                print( x[a:a + lenSearch],"---", search)
                if x[a:a+lenSearch]==search:
                    print(checkMatch)
                    checkMatch = checkMatch+1
        a=a+1

print(search + " = " + str(checkMatch))