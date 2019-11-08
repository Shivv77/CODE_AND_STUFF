'''
def main():

    accu = 0

    total = input("please enter numbers without seperator: ")

    line1 = total[0]
    line2 = total[1]
    line3 = total[2]
    line4 = total[3]
    line5 = total[4]
    #line5 = int(total[4])
    #line6 = int(total[5])
    #line7 = int(total[6])
    
    gradTotal = int(total[0])+int(total[1])+int(total[2])+int(total[3])+int(total[4])
    
    print(gradTotal)


main()
'''


def main():
    total = 0.0
    #count = 0
    xStr = input("Enter a number: ")
    for i in range(len(xStr)):
        x = eval(xStr)
        total = total + xStr
       # count = count + 1
      #  xStr = input("Enter a number (<Enter> to quit) >> ")
   # print("\nThe average of the numbers is", total )
    print(total)


main()
