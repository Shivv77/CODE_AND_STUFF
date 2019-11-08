

def displayThem(theList):
    for item in theList:
        print(item, end=' ')
    print()


def main():
    print("program starting.....")


def squarThem(theList):
    for i in range(len(theList)):
        theList[i] = theList[i]**2
    return theList


numbers = []

for i in range(5):
    numbers.append(eval(input("enter a number: ")))

displayThem(numbers)

result = squarThem(numbers)

displayThem(result)


main()
