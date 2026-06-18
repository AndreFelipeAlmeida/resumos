n = int(input())
menor_preco = float("inf")
ans = 0

for _ in range(n):
    ai, p1 = input().split(" ")
    
    if int(p1) < menor_preco:
        menor_preco = int(p1)
        
    ans += int(ai) * menor_preco
    
    
print(ans)
