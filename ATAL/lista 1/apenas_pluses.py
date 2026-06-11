def main():
    n = int(input())

    def backtracking(a, b, c, cont, maior):
        if cont > 5:
            return maior
        
        multi = a * b * c
        
        if multi > maior:
            maior = multi
            
        m1 = backtracking(a + 1, b, c, cont + 1, maior)
        m2 = backtracking(a, b + 1, c, cont + 1, maior)
        m3 = backtracking(a, b, c + 1, cont + 1, maior)
        
        return max(m1, m2, m3, maior)

    for _ in range(n):
        a, b, c = map(int, input().split(" "))
        ans = backtracking(a, b, c, 0, 0)
        print(ans)
        
if __name__ == "__main__":
    main()
