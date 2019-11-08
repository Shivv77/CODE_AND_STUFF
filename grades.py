count = [1, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
greatest = 0
position = 0
letter = 0
for thing in count:
    if thing > greatest: #iterate through string one char at a time
        greatest = thing # compare current thing with grreatest
        letter = position # assign thing to greatest
    position = position + 1 # increments next position

print(letters[letter], letter,)