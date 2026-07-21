def compara(a, b):
    a = sorted(a)
    b = sorted(b)

    return a == b


def main():
    a = input()
    b = input()

    if a == b:
        print("YES")
        return
    
    a1 = a[:(len(a) // 2)]
    a2 = a[(len(a) // 2):]
    b1 = b[:(len(b) // 2)]
    b2 = b[(len(b) // 2):]
    
    if compara(a1, b1) and compara(a2, b2):
        print("YES")
    elif compara(a1, b2) and compara(a2, b1):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
