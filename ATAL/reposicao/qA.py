def main():
    n = int(input())

    intervalos = []

    final_atual = float("inf")
    intervalo_escolhido = -1
    removidos = 0

    for i in range(n):
        start_i, end_i = map(int, input().split())
        intervalos.append((start_i, end_i))

        if end_i < final_atual:
            final_atual = end_i
            intervalo_escolhido = i

    intervalos.pop(intervalo_escolhido)

    intervalos.sort()

    for comeco, fim in intervalos:
        if comeco >= final_atual:
            final_atual = fim
        else:
            removidos += 1

    print(removidos)



if __name__ == "__main__":
    main()
