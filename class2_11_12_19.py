'''
import time


def main():
    for i in range(60, -1, -1):
        print(i)
        time.sleep(1.0)

main()
'''


def fileOpener():
    file = open("Grades.txt", 'r')
    count = 0
    theSum = 0
    # for line in file:
    line = file.readline().rstrip()

    while line != '-END-':
        student = line.split(',')
        count += 1
        print(line.rstrip())
        theSum += float(student[1])
        line = file.readline()

    print(theSum/count)

    file.close()


fileOpener()
