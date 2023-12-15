currvalue=0
totalsum = 0
with open("input.txt", "r") as f:
    for row in f:
        for char in row:
            if char ==",":
                totalsum += currvalue
                currvalue = 0
            else: 
                currvalue += ord(char)
                currvalue *= 17
                currvalue = currvalue%256
        totalsum += currvalue
    print(totalsum)
