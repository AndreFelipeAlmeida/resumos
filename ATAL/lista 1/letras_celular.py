
def main():
  digits = input()
  
  if digits.strip() == "" or not digits:
    print([])
    return
  
  output = []

  mapa = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
  }
  
  def combina(i, comb_atual):
    if i >= len(digits):
      output.append(comb_atual)  
      return ""
    
    possibilidades = mapa[digits[i]]
    
    for poss in possibilidades:
      prox_string = comb_atual + poss
      combina(i + 1, prox_string)
    
  combina(0, "")
    
  print(output)

if __name__ == "__main__":
    main()
