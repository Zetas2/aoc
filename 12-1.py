totalsum = 0

with open("input.txt", "r") as f:
    for row in f:
        guess = row.strip().split(" ")[0]
        answers = row.strip().split(" ")[1].split(",")
        answers = [int(l) for l in answers]
        allpossible = []
        allpossible.append(guess)
        for i in range(guess.count("?")):
            plausible = []
            for possible in allpossible:
                plausible.append(possible.replace("?",".",1))
                plausible.append(possible.replace("?","#",1))
                allpossible = plausible.copy()
    
        for test in allpossible:
            test = test.split(".")
            test = [l for l in test if l != ""]
            valid = True
            if len(test) != len(answers):
                valid = False
            else:
                for i in range(len(answers)):
                    if len(test[i]) != answers[i]:
                        valid = False
            if valid:
                totalsum += 1
print(totalsum)
