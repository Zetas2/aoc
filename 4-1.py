totalsum = 0
with open("input.txt", "r") as f:
    for next in f:
        win = next.strip().split(":")[1].split("|")[0].split(" ")
        my = next.strip().split(":")[1].split("|")[1].split(" ")
        win = [l for l in win if l != ""]
        my = [l for l in my if l != ""]
        score = 0

        for num in my:
            if num in win:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        totalsum += score
print(totalsum)
        
