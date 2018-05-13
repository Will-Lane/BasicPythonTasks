import pymysql as database

def inputData(regNo, name, address):
    data = database.connect("localhost", "root", "", "newbank")
    curs = data.cursor()
    curs.execute("insert into personel values(%s,%s)",(regNo, name, address))
    data.commit()
    data.close()

def displayData():
    data = database.connect("localhost", "root", "", "data")
    curs = data.cursor()
    curs.execute("select * from personel")
    


Y = ord("Y")
N = ord("N")
y = ord("y")
n = ord("n")

whatDo = input("What would you like to do? Add record (A), Display records (D)")
anotherRecord = True

if whatDo == "A" or whatDo == "a":
    while anotherRecord:
        addData = input("Add record? Y,N")

        if ord(addData[0]) == Y or ord(addData[0]) == y:
            regNo = str(input("Reg number"))
            name = str(input("Name"))
            address = str(input("Address"))

            checkSaveUnchecked = True
            while checkSaveUnchecked:
                saveCheck = str(input("Save record? Y/N"))
                if ord(saveCheck[0]) == Y or ord(saveCheck[0]) == y:
                    inputData(regNo, name, address)
                    checkSaveUnchecked = False
                elif ord(saveCheck[0]) == N or ord(saveCheck[0]) == n:
                    print("Input Cancelled")
                    checkSaveUnchecked = False
                else:
                    print("Input invalid, please choose 'Y or 'N")

        elif ord(addData[0]) == N or ord(addData[0]) == n:
            anotherRecord = False

        else:
            print("Input invalid, please choose 'Y' or 'N'")

elif whatDo == "D" or whatDo == "d":
    displayData()