
def extractnum(f,row,j):
    stringnum = ""
    try:
        int(f[row][j])
    except:
        pass
    else:
        stringnum = f[row][j]
        try:
            int(f[row][j-1])
        except:
            try:
                int(f[row][j+1])
            except:
                pass
            else:
                stringnum = stringnum + f[row][j+1]
                try:
                    int(f[row][j+2])
                except:
                    pass
                else:
                    stringnum = stringnum + f[row][j+2]
        else:
            stringnum = f[row][j-1] + stringnum
            try:
                int(f[row][j-2])
            except:
                try:
                    int(f[row][j+1])
                except:
                    pass
                else:
                    stringnum = stringnum + f[row][j+1]    
            else:
                stringnum = f[row][j-2] + stringnum
    return stringnum

totalsum = 0
with open("input.txt", "r") as f:
    f = list(f)
    for row in range(len(f)):
        j=0
        while j < len(f[row]):
            if f[row][j]=="*":
                numbers = []
                if row != 0:
                    num = extractnum(f,row-1,j-1)
                    numbers.append(num)
                    num = extractnum(f,row-1,j)
                    numbers.append(num)
                    num = extractnum(f,row-1,j+1)
                    numbers.append(num)
                
                num = extractnum(f,row,j-1)
                numbers.append(num)
                num = extractnum(f,row,j)
                numbers.append(num)
                num = extractnum(f,row,j+1)
                numbers.append(num)

                if row != len(f):
                    num = extractnum(f,row+1,j-1)
                    numbers.append(num)
                    num = extractnum(f,row+1,j)
                    numbers.append(num)
                    num = extractnum(f,row+1,j+1)
                    numbers.append(num)

                for k in range(len(numbers)-1):
                    if numbers[k] == numbers[k+1]:
                        numbers[k] = ""
                
                numbers = [l for l in numbers if l != ""]
                if len(numbers) == 2:
                    totalsum += int(numbers[0]) * int(numbers[1])

            j+=1


print(totalsum)
