totalsum = 0
with open("input.txt", "r") as f:
    for next in f:
        words = next.split(" ")
        gameid = int(words[1][:-1])
        
        valid = True
        red = 0
        blue = 0
        green = 0
        for i in range(2,len(words),2):
            

            colour = words[i+1][:-1]
            if colour == "red" and int(words[i])> red:
                red = int(words[i])
            elif colour == "blue" and int(words[i])> blue:
                blue = int(words[i])
            elif colour == "green" and int(words[i])> green:
                green = int(words[i])

        power = red*green*blue
        totalsum += power
        
print(totalsum)
