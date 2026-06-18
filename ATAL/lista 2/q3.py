s, n = map(int, input().split(" "))

n_der = []

for i in range(n):
    for xi, yi in n_der:
        if s > xi:
            s += yi
            n_der.remove((xi, yi))

    x, y = map(int, input().split(" "))

    if s <= x:
        n_der.append((x, y))
    else:
        s += y
    
print("YES" if not n_der else "NO")
