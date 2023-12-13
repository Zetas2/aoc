import numpy as np

totalsum =0

with open("input.txt", "r") as f:
    f = list(f)
    f.append("\n")
    f.append("\n")
    prevrow = f[0]
    rownum = 0
    notfound = True
    for i in range(1,len(f)):
        rownum +=1
        if f[i] == "\n":
            if notfound:
                rownum2 = 0
                flip = []
                for row in f[(i-rownum):i]:
                    fliprow = []
                    for letter in row:
                        if letter != "\n":
                            fliprow.append(letter)
                    flip.append(fliprow)
                flip = np.transpose(flip)
                flip = list(flip)
                flip.append("\n")
                
                prevrow2 = ''.join(flip[0])
                for k in range(1,len(flip)):
                    rownum2 +=1
                    if ''.join(flip[k]) == "\n":
                        
                        rownum2 = 0
                        notfound = True
                    elif prevrow2 == ''.join(flip[k]):
                        valid = True
                        for l in range(rownum2+1):
                            if ''.join(flip[k+l-1]) != ''.join(flip[k-l]):
                                valid = False
                            if ''.join(flip[k+l]) == "\n":
                                break
                        if valid:
                            totalsum += rownum2
                    prevrow2 = ''.join(flip[k])
            rownum = -1
            notfound = True
        elif prevrow == f[i]:
            valid = True
            for j in range(rownum+1):
                if f[i+j-1].strip() != f[i-j].strip():
                    valid = False
                if f[i+j] == "\n":
                    break
            if valid:
                totalsum += rownum*100
                notfound = False
        prevrow = f[i]
print(totalsum)


