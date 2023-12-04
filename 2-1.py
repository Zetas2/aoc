totalsum = 0
with open("input.txt", "r") as f:
    for next in f:
        words = next.split(" ")
        gameid = int(words[1][:-1])
        
        valid = True
        for i in range(2,len(words),2):
            red = 0
            blue = 0
            green = 0

            colour = words[i+1][:-1]
            if colour == "red":
                red += int(words[i])
            elif colour == "blue":
                blue += int(words[i])
            elif colour == "green":
                green += int(words[i])
                
            
            if green > 13 or red > 12 or blue > 14:
                valid = False

            if i == len(words)-2:
                if valid:
                    totalsum += gameid

print(totalsum)
