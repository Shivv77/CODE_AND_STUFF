theList = ['A', 'B', 'C', 'D']


def main():
    theList.append('Z')
    theList.append('F')
    del theList[-1]
    print(theList)


main()
