more = True
totalsum = 0
while more:
    next = input()
    if next == "":
        print(totalsum)
        more = False
    else:
        next = next.replace("one","o1e").replace("two","t2o").replace("three","t3e").replace("four","f4r").replace("five","f5e").replace("six","s6x").replace("seven","s7n").replace("eight","e8t").replace("nine","n9e")
        stringnum1 = ""
        stringnum2 = ""
        print(next)
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

