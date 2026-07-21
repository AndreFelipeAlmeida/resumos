def main():
    escadas = list(map(int,input().split()))
    valor = min(c_cost(escadas,0),c_cost(escadas,1))
    print(valor)

def c_cost(a, i):
    cost = 0

    if len(a)-1 >= i:    
        cost += a[i]
        cost += (min(c_cost(a,i+1),c_cost(a,i+2)))
    
    return cost
    

if __name__ == '__main__':
    main()
