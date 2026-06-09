def main():
    ct = input()
    for i in range(int(ct)):
        vit = 0
        a1, a2, b1, b2 = input().split(" ")
        a1 = int(a1)
        a2 = int(a2)
        b1 = int(b1)
        b2 = int(b2)

        if a1 > b1 and a2 >= b2:
            vit += 1
        if a1 == b1 and a2 > b2:
            vit += 1

        if a1 > b2 and a2 >= b1:
            vit += 1
        if a1 == b2 and a2 > b1:
            vit += 1

        if a2 > b2 and a1 >= b1:
            vit += 1
        if a2 == b2 and a1 > b1:
            vit += 1

        if a2 > b1 and a1 >= b2:
            vit += 1
        if a2 == b1 and a1 > b2:
            vit += 1

        print(vit)


if __name__ == "__main__":
    main()
