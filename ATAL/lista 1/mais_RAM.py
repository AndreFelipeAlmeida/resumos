def main():
  ct = int(input())
  for i in range(ct):
    n, k = map(int, input().split())
    
    ram_gasta = input().split()
    
    ram_adicional = input().split()
    
    maior_ram = k
    k_atual = k
    
    usados = []
    
    for _ in range(n):
      for j in range(n):
        if int(ram_gasta[j]) <= k_atual and j not in usados:
          k_atual += int(ram_adicional[j])
          usados.append(j)
        
    if maior_ram < k_atual:
      maior_ram = k_atual
      
    print(maior_ram)

if __name__ == "__main__":
  main()