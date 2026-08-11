def main():
    n, capacidade_max = map(int, input().split())
    items = []

    for i in range(n):
        peso_i, valor_i = map(int, input().split())
        items.append((peso_i, valor_i))

    def bt(i, peso_atual, valor_atual):
        if i >= len(items):
            return valor_atual
        
        item = items[i]

        if peso_atual + item[0] > capacidade_max:
            return bt(i + 1, peso_atual, valor_atual)

        adicionando = bt(i + 1, peso_atual + item[0], valor_atual + item[1])
        n_adicionando = bt(i + 1, peso_atual, valor_atual)

        return max(adicionando, n_adicionando)

    print(bt(0, 0, 0))

if __name__ == "__main__":
    main()
