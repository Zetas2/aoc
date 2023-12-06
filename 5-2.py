import time
starttime = time.time()
currentmode = 0
lowest = 251346198
with open("input.txt", "r") as f:
    start = int(input())
    f = list(f)
    f = [l for l in f if l != ""]
    seeds = f[0].strip().split(":")[1].split(" ")
    seeds = [l for l in seeds if l != ""]
    f = [l for l in f if not(l == "" or l == "\n")]
    f = f[1:]
    for a in range(start,len(seeds),2):
        print(f"next seed (after {time.time()-starttime} seconds)")
        for b in range(int(seeds[a+1])):
            if b % 100000 == 0:
                print(f"{b/int(seeds[a+1])*100}% complete")
            number = int(seeds[a])+b
            for rule in f:
                if "map" in rule:
                    changed = False
                else:
                    startsoil = int(rule.strip().split(" ")[0])
                    startseed = int(rule.strip().split(" ")[1])
                    length = int(rule.strip().split(" ")[2])
                    if number >= startseed and number <= startseed+length and not changed:
                        number = number-startseed+startsoil
                        changed = True
            if number < lowest:
                lowest = number
                print(lowest)

print(f"The lowest is {lowest}\nIt took {time.time()-starttime} seconds to find")

# Took like 110 hours.. Ran all ten at the same time so took 12 hours real time

