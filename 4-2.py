def winning(f,next):
    copies = []
    
    
    for i in range(len(next)):
        cardnum = int(next[i].strip().split(":")[0].replace("Card",""))
        win = next[i].strip().split(":")[1].split("|")[0].split(" ")
        my = next[i].strip().split(":")[1].split("|")[1].split(" ")
        win = [l for l in win if l != ""]
        my = [l for l in my if l != ""]
        wins = 0
        for num in my:
            if num in win:
                try:
                    copies.append(f[wins+cardnum])
                except:
                    pass
                wins += 1

    return copies
        



totalsum = 0
with open("input.txt", "r") as f:
    f = list(f)
    
    cards = winning(f,f)
    totalsum += len(f)
    
    while len(cards) > 0:
        totalsum += len(cards)
        cards = winning(f,cards)
        print(totalsum)
        
        
print(totalsum)
        
