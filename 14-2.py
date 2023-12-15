import numpy as np

totalsum =0

def moverocks(funcrow, stones, laststop):
    for a in range(laststop, laststop+stones):
        funcrow[a]="O"
    return funcrow


loops = []

x = 0 
y = 0
goal = 1000000000
np.set_printoptions(threshold=np.inf)

with open("input.txt", "r") as f:
    f = list(f)
    flip = []

    for row in f:
        fliprow = []
        for letter in row:
            if letter != "\n":
                fliprow.append(letter)
        flip.append(fliprow)
    visited = {}
    for m in range (goal):
        flip = np.transpose(flip)
        flip = list(flip)
        # North
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

        #west
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
        flip = np.flip(flip)
        flip= list(flip)

        #soputh
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

        #east
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
        flip = np.flip(flip)

        
        
        if str(flip) in visited:
            if x == 0:
                x = m 
                z = visited.get(str(flip))
            if visited.get(str(flip)) in loops:
                #print(f"loops after {m} times with {visited.get(str(flip))}")
                #print("complete loop")
                if y == 0:
                    y = m - x
                    offset = m%y 
                break
            loops.append(visited.get(str(flip)))
            #print(flip)
        else:
            visited.update({str(flip):m})

    actual = goal%y-offset+z
    if actual < z:
        actual += y
        

    flip = []

    for row in f:
        fliprow = []
        for letter in row:
            if letter != "\n":
                fliprow.append(letter)
        flip.append(fliprow)
    visited = {}
    for m in range (actual):
        flip = np.transpose(flip)
        flip = list(flip)
        # North
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

        #west
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
        flip = np.flip(flip)
        flip= list(flip)

        #soputh
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

        #east
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
        flip = np.flip(flip)

    flip = list(flip)


    multiplier = len(f)
    for row in flip:
        stones = np.count_nonzero(row == "O")
        totalsum += stones*multiplier
        multiplier -=1

print(totalsum)
