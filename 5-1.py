currentmode = 0
with open("input.txt", "r") as f:
    for next in f:
        if "map" in next and currentmode != 0:
            changed = [False]*len(soils)
        elif "\n" == next:
            pass
        elif currentmode == 0:
            seeds = next.strip().split(":")[1].split(" ")
            seeds = [l for l in seeds if l != ""]
            soils = seeds.copy()
            currentmode = 1
        elif currentmode == 1:           
            soils = [int(l) for l in soils]
            startsoil = int(next.strip().split(" ")[0])
            startseed = int(next.strip().split(" ")[1])
            length = int(next.strip().split(" ")[2])

            for i in range(len(soils)):
                if soils[i] >= startseed and soils[i] <= startseed+length and not changed[i]:
                    soils[i] = soils[i]-startseed+startsoil
                    changed[i] = True
            
print(min(soils))
    
