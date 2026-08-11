def main():
    num = input()
    idx = 0

    while idx < len(num):
        if idx + 2 < len(num) and num[idx] + num[idx + 1] + num[idx + 2] == "144":
            idx += 3
        elif idx + 1 < len(num) and num[idx] + num[idx + 1] == "14":
            idx += 2
        elif num[idx] == "1":
            idx += 1
        else:
            print("NÃO")
            return
    
    print("SIM")

if __name__ == "__main__":
    main()
