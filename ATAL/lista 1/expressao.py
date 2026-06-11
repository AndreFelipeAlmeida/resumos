def main():
    a = int(input())
    b = int(input())
    c = int(input())
    maior = a * b * c

    if a + b + c > maior:
        maior = a + b + c
    if (a + b) * c > maior:
        maior = (a + b) * c
    if a + b * c > maior:
        maior = a + b * c
    if a * (b + c) > maior:
        maior = a * (b + c)
    if a * b + c > maior:
        maior = a * b + c

    print(maior)


if __name__ == '__main__':
    main()
