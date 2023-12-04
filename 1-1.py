more = True
totalsum = 0
while more:
    next = input()
    if next == "":
        print(totalsum)
        more = False
    else:
        stringnum1 = ""
        stringnum2 = ""
        for i in next:
            try:
                int(i)
                if stringnum1 == "":
                    stringnum1 = i
                    stringnum2 = i
                else:
                    stringnum2 = i
            except:
                pass
        totalsum += int(stringnum1+stringnum2)
