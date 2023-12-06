with open("input.txt", "r") as f:
    f = list(f)
    times = int(f[0].strip().split(":")[1].replace(" ",""))
    records = int(f[1].strip().split(":")[1].replace(" ",""))
    numways = 0
    for b in range(times):
        if (times-b)*b > records:
            numways +=1
print(numways)
