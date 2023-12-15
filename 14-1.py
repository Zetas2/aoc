import numpy as np

totalsum =0

def moverocks(funcrow, stones, laststop):
    for a in range(laststop, laststop+stones):
        funcrow[a]="O"
    return funcrow


with open("input.txt", "r") as f:
    f = list(f)
    flip = []
    for row in f:
        fliprow = []
        for letter in row:
            if letter != "\n":
                fliprow.append(letter)
        flip.append(fliprow)
    flip = np.transpose(flip)
    flip = list(flip)

    for fliprow in flip:
        stones = 0
        laststop = 0
        for i in range(len(fliprow)):
            if fliprow[i] == "O":
                stones += 1
                fliprow[i] = "."
            if fliprow[i] == "#":
                fliprow = moverocks(fliprow, stones, laststop)
                laststop = i+1
                stones = 0
        fliprow = moverocks(fliprow, stones, laststop)

    flip = np.array(flip)
    flip = np.transpose(flip,(1,0))
    flip= list(flip)

    multiplier = len(f)
    for row in flip:
        stones = np.count_nonzero(row == "O")
        totalsum += stones*multiplier
        multiplier -=1
    
print(totalsum)
