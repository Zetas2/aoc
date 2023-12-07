totalsum = 0

def addpoint(cards,points,rank):
    cards.sort(reverse=True)
    for game in cards:
        points += int(game[1])*rank
        rank -=1
    return points, rank



with open("input.txt", "r") as f:
    f = list(f)
    rank = len(f)
    five = []
    four = []
    house = []
    three = []
    two = []
    one = []
    high = []
    for a in range(len(f)):
        hand = f[a].strip().split(" ")[0]
        bid = f[a].strip().split(" ")[1]
        hand = list(hand)
        for b in range(len(hand)):
            if hand[b] == "T":
                hand[b] = 10
            elif hand[b] == "J":
                hand[b] = 1
            elif hand[b] == "Q":
                hand[b] = 12
            elif hand[b] == "K":
                hand[b] = 13
            elif hand[b] == "A":
                hand[b] = 14
            else:
                hand[b] = int(hand[b])
        
        sortedhand = sorted(hand)

        if sortedhand[0] == sortedhand[1]:
            if sortedhand[0]== sortedhand[2]:
                if sortedhand[0]==sortedhand[3]:
                    if sortedhand[0]==sortedhand[4] or sortedhand[3]==1:
                        five.append([hand,bid]) #11111,#00000,#00001
                    else:
                        four.append([hand,bid]) #11112
                elif sortedhand[3] == sortedhand[4]:
                    if sortedhand[2] == 1:
                        five.append([hand,bid])#00011
                    else:
                        house.append([hand,bid]) #11122
                    
                else:
                    if sortedhand[2] == 1:
                        if sortedhand[3]== sortedhand[4]:
                            five.append([hand,bid]) #00011
                        else:
                            four.append([hand,bid]) #00012
                    else:
                        three.append([hand,bid]) #11123
            elif sortedhand[2]==sortedhand[3]:
                if sortedhand[3]==sortedhand[4]:
                    if sortedhand[1] == 1:
                        five.append([hand,bid])#00111
                    else:
                        house.append([hand,bid]) #11222
                else:
                    if sortedhand[1] == 1:
                        four.append([hand,bid]) #00112
                    else:
                        two.append([hand,bid]) #11223
            elif sortedhand[3]==sortedhand[4]:
                if sortedhand[1] == 1:
                    four.append([hand,bid]) #00122
                else: 
                    two.append([hand,bid]) #11233
            else:
                if sortedhand[1] == 1:
                    three.append([hand,bid]) #00123
                else:
                    one.append([hand,bid]) #11234
        elif sortedhand[1]==sortedhand[2]:
            if sortedhand[1]==sortedhand[3]:
                if sortedhand[1] == sortedhand[4]:
                    if sortedhand[0] == 1:
                        five.append([hand,bid])#01111
                    else:
                        four.append([hand,bid]) #12222
                else:
                    if sortedhand[0]==1:
                        four.append([hand,bid]) #01112
                    else: 
                        three.append([hand,bid]) #12223
            elif sortedhand[3]==sortedhand[4]:
                if sortedhand[0] == 1:
                    house.append([hand,bid]) #01122
                else: 
                    two.append([hand,bid]) #12233
            else:
                if sortedhand[0] == 1:
                    three.append([hand,bid]) #01123
                else: 
                    one.append([hand,bid]) #12234
        elif sortedhand[2]==sortedhand[3]:
            if sortedhand[3]==sortedhand[4]:
                if sortedhand[0]==1:
                    four.append([hand,bid]) #01222
                else:
                    three.append([hand,bid]) #12333
            else:
                if sortedhand[0] == 1:
                    three.append([hand,bid]) #01223
                else:
                    one.append([hand,bid]) #12334
        elif sortedhand[3]==sortedhand[4]:
            if sortedhand[0] == 1:
                three.append([hand,bid]) #01233
            else: 
                one.append([hand,bid]) #12344
        elif sortedhand[0] == 1:
            one.append([hand,bid]) #01234
        else:
            high.append([hand,bid]) #12345

    totalsum,rank = addpoint(five,totalsum,rank)
    totalsum,rank = addpoint(four,totalsum,rank)
    totalsum,rank = addpoint(house,totalsum,rank)
    totalsum,rank = addpoint(three,totalsum,rank)
    totalsum,rank = addpoint(two,totalsum,rank)
    totalsum,rank = addpoint(one,totalsum,rank)        
    totalsum,rank = addpoint(high,totalsum,rank)
print(totalsum)
