import numpy as np

totalsum =0

with open("input.txt", "r") as f:
    f = list(f)
    galaxies = []            
    row = 0
    while row < len(f):
        if "#" not in f[row]:
            f.insert(row,"."*len(f[row].strip()))
            row +=1
        row += 1
    
    flip = []
    for row in f:
        fliprow = []
        for letter in row:
            if letter != "\n":
                fliprow.append(letter)

        flip.append(fliprow)
    flip = np.transpose(flip)

    flip = list(flip)

    row = 0
    while row < len(flip):
        if "#" not in flip[row]:
            flip.insert(row,"."*len(flip[row]))
            row +=1
        row += 1
    
    backflip = []
    for row in flip:
        backfliprow = []
        for letter in row:
            if letter != "\n":
                backfliprow.append(letter)
        backflip.append(backfliprow)
    backflip = np.transpose(backflip)

    for row in range (len(backflip)):
        for column in range(len(backflip[row])):
            if backflip[row][column] == "#":
                galaxies.append([row,column])


    for galaxy in galaxies:
        for galaxy2 in galaxies:
            distance = abs(int(galaxy[0])-int(galaxy2[0]))+abs(int(galaxy[1])-int(galaxy2[1]))
            totalsum += distance
    totalsum = totalsum /2


    print(int(totalsum))
