import math
turnedOn = int(input())
horas = [1, 2, 4, 8]
minutos = [1, 2, 4, 8, 16, 32]
ans = set()

def h_bin_num(bin):
    result = 0
    for i in range(len(bin)):
        if bin[i] == 1:
            result += horas[i]

    return result

def m_bin_num(bin):
    result = 0
    for i in range(len(bin)):
        if bin[i] == 1:
            result += minutos[i]

    return result

def check(horas, minutos):

    if 0 <= h_bin_num(horas) <= 11:
        if 0 <= m_bin_num(minutos) <= 59:
            return True
    
    return False

def backtracking(horas, minutos, idx_h, idx_m, cont):
    if cont == turnedOn:
        if check(horas, minutos):
            min = str(m_bin_num(minutos))
            hor = h_bin_num(horas)
            if len(min) == 1:
                min = "0" + min

            ans.add(f"{hor}:{min}")
        return

    horas_atualizadas = horas[:]
    minutos_atualizados = minutos[:]

    if idx_m < len(minutos):
        minutos_atualizados[idx_m] += 1
        backtracking(horas, minutos_atualizados, idx_h, idx_m + 1, cont + 1)
        backtracking(horas, minutos, idx_h, idx_m + 1, cont)
    
    if idx_h < len(horas):
        horas_atualizadas[idx_h] += 1
        backtracking(horas_atualizadas, minutos, idx_h + 1, idx_m, cont + 1)
        backtracking(horas, minutos, idx_h + 1, idx_m, cont)

    return


backtracking([0, 0, 0, 0], [0, 0, 0, 0, 0, 0], 0, 0, 0)

print(list(ans))
