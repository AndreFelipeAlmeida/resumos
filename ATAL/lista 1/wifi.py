def main():
    s1 = input()
    s2 = input()
    pos_possiveis = []
    
    def backtracking(i, pos_final):
        if i >= len(s2):
            pos_possiveis.append(pos_final)
            return
        
        if s2[i] == "+" or s2[i] == "?":
            backtracking(i + 1, pos_final + 1)
        if s2[i] == "-" or s2[i] == "?":
            backtracking(i + 1, pos_final - 1)
            
    backtracking(0, 0)
    pos_real = s1.count("+") - s1.count("-")
    ans = pos_possiveis.count(pos_real) / len(pos_possiveis)
    print(f"{ans:.12f}")


if __name__ == "__main__":
    main()
