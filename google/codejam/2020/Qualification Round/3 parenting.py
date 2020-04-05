t = int(input()) # number of test case

for x in range(1, t + 1):
    y = ''
    n = int(input()) # read n
    matrix = []
    lista = [None] * n

    for m in range(0, n):
        row = [int(s) for s in input().split(" ")]
        row.append(m)
        matrix.append(row)
    matrix.sort(key = lambda x: x[0])

    padre='J'
    madre='C'

    for m in range(0, n):
        se = matrix[m]

        if m == 0:
            lista[se[2]] = madre
            continue        
        elif m == 1:
            se_1 = matrix[m-1]
            if se[0] >= se_1[1]:
                lista[se[2]] = madre
            elif se[0] < se_1[1]:
                lista[se[2]] = padre
            continue
        se_1 = matrix[m-1]
        se_2 = matrix[m-2]
        if se[0] < se_1[1] and se[0] < se_2[1] and se_1[0] < se_2[1]:
            y = 'IMPOSSIBLE'
            break
        elif se[0] < se_1[1] and se[0] >= se_2[1]:
            if lista[se_2[2]] == lista[se_1[2]] and lista[se_2[2]] == madre:
                lista[se[2]] = padre
            if lista[se_2[2]] == lista[se_1[2]] and lista[se_2[2]] == padre:
                lista[se[2]] = madre
            elif lista[se_1[2]] == madre and lista[se_2[2]] == padre:
                lista[se[2]] = padre
            elif lista[se_1[2]] == padre and lista[se_2[2]] == madre:
                lista[se[2]] = madre
            print(lista[se[2]]+'a'+ str(m))
            continue
        elif se[0] >= se_1[1]:
            lista[se[2]] = lista[se_1[2]]
            print(lista[se[2]]+'b'+str(m))
            continue
    if y != 'IMPOSSIBLE':
        y = ''.join(lista)  
    
    print("Case #{}: {}".format(x, y))