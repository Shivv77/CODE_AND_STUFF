def mostFrequent():

    # list for storing alphbet count value.
    
    
    
    # variable with sting of alphabet
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # empty lists for
    maxLetter = 0
    frequent = 0
    counter = 0
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # get input from user
    user_string = input('Enter a string to be analyzed: ').upper()
    
    # loop through user string
    for letter in user_string:
        
        # variable
        position = letters.find(letter)
        if position != -1:
            
            count[position] += 1
            
            where = count.find(max(count))
            #maxLetter = count.find(max(count))
    print(count)

    # get position of max in count
    
    # use count.find(where) to get index position within count of where it is
    
    # now slice into letters to get that character

    for each in count:
        if each > frequent:
            frequent = each

    print(letters, frequent, position, where)


mostFrequent()
