ct = int(input())

for i in range(ct):
    n = int(input())
    arr = input().split(" ")
    for i in range(n):
        if arr.count(arr[i]) == 1:
            print(i + 1)
            break
