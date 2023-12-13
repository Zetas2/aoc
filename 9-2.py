totalsum=0
with open("input.txt", "r") as f:
    for next in f:
        values = next.strip().split(" ")
        values = [int(l) for l in values if l != ""]
        side = values[-1]
        diffset = values.copy()
        step = len(values)-1
        round = 0
        checker = values.copy()
        start = [values[0]]
        while not(all(val == 0 for val in checker)):
            checker = []
            for i in range(len(diffset)-1):
                checker.append(diffset[i+1]-diffset[i])
            checker = checker[:len(values)]
            diffset = checker.copy()
            start.append(checker[0])
            round +=1
        prevvalue = 0
        for curvalue in start[::-1]:
            nextvalue = curvalue-prevvalue
            prevvalue = nextvalue
        totalsum += nextvalue
print(totalsum)
