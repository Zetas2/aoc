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
                hand[b] = 11
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
                    if sortedhand[0]==sortedhand[4]:
                        five.append([hand,bid]) #11111
                    else:
                        four.append([hand,bid]) #11112
                elif sortedhand[3] == sortedhand[4]:
                    house.append([hand,bid]) #11122
                else:
                    three.append([hand,bid]) #11123
            elif sortedhand[2]==sortedhand[3]:
                if sortedhand[3]==sortedhand[4]:
                    house.append([hand,bid]) #11222
                else:
                    two.append([hand,bid]) #11223
            elif sortedhand[3]==sortedhand[4]:
                two.append([hand,bid]) #11233
            else:
                one.append([hand,bid]) #11234
        elif sortedhand[1]==sortedhand[2]:
            if sortedhand[1]==sortedhand[3]:
                if sortedhand[1] == sortedhand[4]:
                    four.append([hand,bid]) #12222
                else:
                    three.append([hand,bid]) #12223
            elif sortedhand[3]==sortedhand[4]:
                two.append([hand,bid]) #12233
            else:
                one.append([hand,bid]) #12234
        elif sortedhand[2]==sortedhand[3]:
            if sortedhand[3]==sortedhand[4]:
                three.append([hand,bid]) #12333
            else:
                one.append([hand,bid]) #12334
        elif sortedhand[3]==sortedhand[4]:
            one.append([hand,bid]) #12344
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
