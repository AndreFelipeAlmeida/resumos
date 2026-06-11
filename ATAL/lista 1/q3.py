f1 = input()
f2 = input()
f3 = input()
formulas = [f1, f2, f3]

def check(poss: list):
    for form in formulas:
        pos1 = poss.index(form[0])
        pos2 = poss.index(form[2])
        if form[1] == "<" and pos1 > pos2:
            return False
        elif form[1] == ">" and pos1 < pos2:
            return False
    
    return True

def backtracking(poss, idx):
    if idx >= len(formulas):
        if check(poss):
            return poss
        return "Impossible"

    form = formulas[idx]
    pos1 = poss.index(form[0])
    pos2 = poss.index(form[2])

    if form[1] == "<" and pos1 > pos2:
        for i in range(pos2, pos1):
            poss[i], poss[i+1] = poss[i+1], poss[i]
        return backtracking(poss, idx + 1)
    
    elif form[1] == ">" and pos1 < pos2:
        for i in range(pos1, pos2):
            poss[i], poss[i+1] = poss[i+1], poss[i]
        return backtracking(poss, idx + 1)
    
    else:
        return backtracking(poss, idx + 1)
    
ans = backtracking(["A", "B", "C"], 0)

print("".join(ans))
