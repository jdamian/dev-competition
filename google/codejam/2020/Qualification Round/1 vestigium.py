t = int(input()) # number of test case

for x in range(1, t + 1):
    matrix = []
    k, r, c = 0, 0, 0
    n = int(input()) # read n
    
    for m in range(0, n):
        # creacion de la matriz
        row = [int(s) for s in input().split(" ")]
        k += row[m]
        matrix.append(row)
        mylist = list(dict.fromkeys(row))
        if len(mylist) < n:
            r += 1
    
    for i in range(0, n):
        col = []
        for j in range(0,n):
            col.append(matrix[j][i])
        mylist = list(dict.fromkeys(col))
        if len(mylist) < n:
            c += 1

    print("Case #{}: {} {} {}".format(x, k, r, c))