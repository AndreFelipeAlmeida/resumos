def main():
  ano = int(input())
  menor = ano
  atual = ano + 1
  
  while(menor == ano):
    atual_str = str(atual)
    
    digitos_usados = []
    for i in range(len(atual_str)):
      if atual_str[i] in digitos_usados:
        break
      
      if atual_str[i] not in digitos_usados and i == len(atual_str) - 1:
        menor = atual
        
      digitos_usados.append(atual_str[i])
      
    atual += 1
    
  print(menor)
  
if __name__ == "__main__":
    main()
