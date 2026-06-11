def main():
    n = int(input())
    tam = 2 ** n
    
    def difere_digito(num1, num2):
        dig_diff = 0
        ultimo_digito = format(num2, "b")
        elem = format(num1, "b")
        tamanho_maximo = max(len(ultimo_digito), len(elem))

        elem = elem.zfill(tamanho_maximo)
        ultimo_digito = ultimo_digito.zfill(tamanho_maximo)
        
        for i in range(len(ultimo_digito)):
            if ultimo_digito[i] != elem[i]:
                dig_diff += 1
            
            if dig_diff > 1:
                return True
        
        if dig_diff != 1:
            return True
        
        return False
    
    def poda(lista, elem):
        if lista.count(elem) > 0:
            return True
        
        if difere_digito(lista[-1], elem): return True
        return False    
    
    
    def backtracking(lista):
        if len(lista) >= tam:
            if not difere_digito(lista[0], lista[-1]):
                return lista
            return []
        
        for i in range(1, tam):
            if poda(lista, i):
                continue
            retorno = backtracking(lista + [i])
            if retorno:
                return retorno
        
        return []
    
    ans = backtracking([0])
    print(ans)
    
if __name__ == "__main__":
    main()