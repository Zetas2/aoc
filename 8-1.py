steps = 0
moves = {}
prevmov = "AAA"
with open("input.txt", "r") as f:
    f = list(f)
    instruction = f[0].strip()
    for a in range(2,len(f)):
        start = f[a].split(" ")[0]
        R = f[a].split(",")[0].split("(")[1].strip()
        L = f[a].split(",")[1].split(")")[0].strip()
        moves.update({start: [R,L]})
    while prevmov != "ZZZ":
        thisinstruction = 1 if instruction[steps%len(instruction)] == "R" else 0
        prevmov = moves.get(prevmov)[thisinstruction]
        steps +=1
   

print(steps)
