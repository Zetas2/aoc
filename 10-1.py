totalsum =0
x = 0
y=1
def testpossible(pos):
    try:
        symbol = f[pos[x]][pos[y]]
        return symbol
    except:
        return "."



with open("input.txt", "r") as f:
    f = list(f)
    for row in range(len(f)):
        row = int(row)
        if "S" in f[row]:
            for column in range(len(f[row])):
                column = int(column)
                if "S" in f[row][column]:
                    startpos = [row,column]
                    pos = [row,column+1]

    visited = []
    lastpos = startpos
    symbol = ""
    while symbol != "S":
        if lastpos in visited:
            print("stuck!")
            break
        visited.append(lastpos.copy())
        symbol = testpossible(pos)
       
        if symbol == "-":
            if lastpos[y] < pos[y]:
                lastpos[y] = pos[y]
                pos[y] = pos[y]+1
            else:
                lastpos[y] = pos[y]
                pos[y] = pos[y]-1
        elif symbol == "7":
            if lastpos[y] < pos[y]:
                lastpos[y] = pos[y]
                pos[x] = pos[x]+1
            else: 
                lastpos[x] = pos[x]
                pos[y] = pos[y]-1
        elif symbol == "|":
            if lastpos[x] < pos[x]:
                lastpos[x] = pos[x]
                pos[x] = pos[x]+1
            else:
                lastpos[x] = pos[x]
                pos[x] = pos[x]-1
        elif symbol == "J":
            if lastpos[x] < pos[x]:
                lastpos[x] = pos[x]
                pos[y] = pos[y]-1
            else:
                lastpos[y]=pos[y]
                pos[x]=pos[x]-1
        elif symbol == "L":
            if lastpos[x] < pos[x]:
                lastpos[x] = pos[x]
                pos[y] = pos[y]+1
            else:
                lastpos[y] = pos[y]
                pos[x]=pos[x]-1
        elif symbol == "F":
            if lastpos[y] > pos[y]:
                lastpos[y] = pos[y]
                pos[x] = pos[x]+1
            else:
                lastpos[x] = pos[x]
                pos[y] = pos[y]+1
        elif symbol == "S":
            print("LOOPS")
        elif symbol == ".":
            print("NO LOOP")
            break
        totalsum +=1


print(int(totalsum/2))
