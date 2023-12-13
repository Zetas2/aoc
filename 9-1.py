totalsum=0
with open("input.txt", "r") as f:
    num = 17
    for next in f:
        values = next.strip().split(" ")
        values = [int(l) for l in values if l != ""]
        side = values[-1]
        diffset = values.copy()
        step = len(values)-1
        round = 0
        checker = values.copy()
        while not(all(val == 0 for val in checker)):
            checker = []
            for i in range(len(diffset)-1):
                checker.append(diffset[i+1]-diffset[i])
            checker = checker[:len(values)]
            diffset = checker.copy()
            side += checker[-1]
            round +=1
        totalsum += side
        num+=1
print(totalsum)
