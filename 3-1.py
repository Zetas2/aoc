totalsum = 0
symbols = ["*","@","-","+","#","%","=","/","$","&"]
with open("input.txt", "r") as f:
    f = list(f)
    for row in range(len(f)):
        j=0
        while j < len(f[row]):
            startnum = 0
            lenght = 0
            try:
                int(f[row][j])
            except:
                j+=1
            else:
                startnum = j
                try:
                    int(f[row][j+1])
                except:
                    lenght = 1
                else:
                    try:
                        int(f[row][j+2])
                    except:
                        lenght = 2
                    else:
                        lenght = 3

            finally:
                j += lenght
                if "" != f[row][startnum:startnum+lenght]:
                    add = False
                    if startnum == 0:
                        for symbol in symbols:
                            if symbol in f[row][startnum:startnum+lenght+1] or symbol in f[row-1][startnum:startnum+lenght+1] or symbol in f[row+1][startnum:startnum+lenght+1]:
                                add = True
                    elif row == 0:
                        for symbol in symbols:
                            if symbol in f[row][startnum-1:startnum+lenght+1] or symbol in f[row+1][startnum-1:startnum+lenght+1]:
                                add = True
                    elif startnum+lenght== len(f[row]):
                        for symbol in symbols:
                            if symbol in f[row][startnum-1:startnum+lenght] or symbol in f[row-1][startnum-1:startnum+lenght] or symbol in f[row+1][startnum-1:startnum+lenght]:
                                add = True
                    elif row == len(f)-1:
                        for symbol in symbols:
                            if symbol in f[row][startnum-1:startnum+lenght+1] or symbol in f[row-1][startnum-1:startnum+lenght+1]:
                                add = True
                    else:
                        for symbol in symbols:
                            if symbol in f[row][startnum-1:startnum+lenght+1] or symbol in f[row-1][startnum-1:startnum+lenght+1] or symbol in f[row+1][startnum-1:startnum+lenght+1]:
                                add = True

                    if add:
                        totalsum += int(f[row][startnum:startnum+lenght])
print(totalsum)

                    
                    
                    
