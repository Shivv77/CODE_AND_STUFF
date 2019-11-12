def muncher(kevin):
    i = 0
    for grade  in kevin:
        kevin[i] = grade + 10
        i += 1
    '''
        for i in range(len(kevin))
            kevin[i] = kevin[i] = 10
            kevin[i] += 10


    '''
def main():
    grades = [1,2,3,45,6,6,7,]
    muncher(grades)
    print(grades)

main()