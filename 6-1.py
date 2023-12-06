totalsum = 1
with open("input.txt", "r") as f:
    f = list(f)
    times = f[0].strip().split(":")[1].split(" ")
    records = f[1].strip().split(":")[1].split(" ")
    times = [int(l) for l in times if l != ""]
    records = [int(l) for l in records if l != ""]
    for a in range(len(times)):
        numways = 0
        for b in range(times[a]):
            if (times[a]-b)*b > records[a]:
                numways +=1
        totalsum *= numways
print(totalsum)
