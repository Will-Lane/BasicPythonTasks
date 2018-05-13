#Phys = 75
#Chem = 94
#Math = 125
Phys = input("Please enter physics mark")
Chem = input("Please enter chemistry mark")
Math = input("Please enter maths mark")


Total = int(Phys)+int(Chem)+int(Math)
Per = Total * 100/450

print("Total = ", Total)
print("Percentage = ", Per, "%")

if Per>=60:
    print("Pass")
else:
    print("Fail")