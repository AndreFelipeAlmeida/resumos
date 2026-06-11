def main():
    n, l, r, x = map(int, input().split())
    c = list(map(int, input().split()))

    def backtracking(i, qtd, soma, menor, maior):
        if i == n:
            if qtd >= 2 and l <= soma <= r and maior - menor >= x:
                return 1
            return 0

        if qtd == 0:
            novo_menor = novo_maior = c[i]
        else:
            novo_menor = min(menor, c[i])
            novo_maior = max(maior, c[i])

        pega = backtracking(
            i + 1,
            qtd + 1,
            soma + c[i],
            novo_menor,
            novo_maior
        )

        nao_pega = backtracking(
            i + 1,
            qtd,
            soma,
            menor,
            maior
        )

        return pega + nao_pega


    ans = backtracking(0, 0, 0, 0, 0)
    print(ans)
  
if __name__ == "__main__":
  main()