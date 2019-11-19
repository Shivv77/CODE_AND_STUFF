'''
import random


class MSDie():  # constructor method
    def __init__(self, sides):  # self is not returned
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = random.randint(1, self.sides)

    def getValue(self):
        return self.value

    def getsides(self):
        return self.sides

    def setValue(self, value):
        self.value = value

    def setSides(self, sides):
        self.sides = sides


dieBag = []

for i in range(7):
    dieBag.append(MSDie(6))

for die in dieBag:
    die.roll()
    print(die.getValue())

for die in dieBag:
    die.setSides(10)
    die.setValue(2)
    print(die.getValue(), die.getsides())

die1 = MSDie(6)
for i in range(1100):
    die1.roll()
    print(die1.value)


die1.value = 3
print(die1.sides)
print(die1.value)
die2 = MSDie(100)



class Customer():
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setNumber(self, number):
        self.number = number

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getNumber(self):
        return self.number

cust1 = Customer('kevin','3471 se 169th CT', 2343456)
print(cust1.getName())

'''


class ServiceQuote():
    def __init__(self, parts, labor, tax, total):
        self.parts = parts
        self.labor = labor
        self.tax = tax
        self.total = total

    def setParts(self, parts):
        self.parts = parts

    def getParts(self):
        return self.parts

    def setLabor(self, labor):
        self.labor = labor

    def getLabor(self):
        return self.labor

    def setTax(self, tax):
        self.tax = tax

    def getTax(self):
        return self.tax

    def setTotal(self, Total):
        self.total = Total

    def getTotal(self):
        return self.total


quote1 = ServiceQuote("truck", '123.34', '.34', "145.89")

print(quote1.getTotal())
