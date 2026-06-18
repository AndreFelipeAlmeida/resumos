def main():
    _, alvo = map(int, input().split(" "))

    cads = list(map(int, input().split(" ")))
    total = sum(cads)

    ans = set()

    if total < alvo:
        print()
        return
    
    def bt(i, conj):
        if sum(conj) > alvo:
            return
        
        if sum(conj) == alvo:
            conj.sort()
            con = " ".join(map(str, conj))

            ans.add(con)
            return
        
        if i >= len(cads):
            return
        

        atual = cads[i]

        bt(i + 1, conj + [atual])
        bt(i + 1, conj)


    bt(0, [])
    for j in ans:
        print(j)


main()
