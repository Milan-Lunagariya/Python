# WAP to create Marksheet
py = int(input("Enter mark of Python: "))
cyber = int(input("Enter mark of Cyber: "))
java = int(input("Enter mark of Java: "))
project = int(input("Enter mark of Project: "))

total = (py + cyber + java + project)
grade = "***"
result = "Fail"
persentage = "***"

if ( (py > 35) and (cyber > 35) and (java > 35) and (project > 35) ):
    persentage = (total / 4)
    result = "Pass"
    if persentage > 80    : grade = "A"
    elif persentage > 70  : grade = "B"
    elif persentage > 60  : grade = "C"
    elif persentage > 50  : grade = "D"
    else : grade = "E"

print("---------------------------------------------------")
print( "Total       : ", total)
print( "Persentage  : ", persentage)
print( "Grade       : ", grade)
print( "Result      : ", result)
print("---------------------------------------------------")