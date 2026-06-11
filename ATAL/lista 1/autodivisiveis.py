def main():
    n1, n2 = map(int, input().split(" "))
    lista = []
    for i in range(n1, n2, 1):
        if list(str(i)).count("0") > 0:
            continue
        else:
            j = list(str(i))
            for x in range(len(j)):
                if i % int(j[x]) != 0:
                    break
                if x == len(j) - 1:
                    lista.append(str(i))
                    
    print(" ".join(lista))


if __name__ == '__main__':
    main()
