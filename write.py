



theFile = open('gas','r')


for i in range(2):
    student = input("please enter a name: ")
    theFile.write(student + "\n")

theFile.close()