physMarks = int(input("physics marks"))
matMarks = int(input("maths arks"))
chemMarks = int(input("chem marks"))

count = 0

if (physMarks *100/150) < 60:
    count = count+1
if (matMarks *100/150) < 60:
    count = count+1
if (chemMarks * 100 / 150) < 60:
    count = count+1

if count ==0:
    total = physMarks + matMarks + chemMarks
    print("Total marks =", total, "/450")
    print("Percentage = " , total*(100/450), "%")

elif count ==1:
    print("Please retake exam")
elif count ==2:
    print("Please repeat course")
else:
    print("Fuck off, you're not welcome here any more")

