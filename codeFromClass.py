
'''
def main():
grades=[]
letters = []


biggest = max(grade)
print(biggest)
position = grade.index(biggest)

print(letters[position])

stuf = 'BruceSeesADog'

main()
'''

"""
def hsu(p, q):
    print(p*q)


def main():

    pizza = "Papa Murphy"
    hsu(pizza, 42)
"""


def product(a, b, c, d):
    TheProduct = a * b * c * d
    return TheProduct


def summer(a, b, c, d):
    TheSum = a + b + c + d
    return TheSum


def subtractor(a, b, c, d):
    TheSubber = a - b - c - d
    return TheSubber


def main():
    num1, num2, num3, num4 = eval(input("enter for numbers: "))
    print(product(num1, num2, num3, num4))


main()
