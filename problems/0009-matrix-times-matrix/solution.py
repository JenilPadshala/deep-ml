def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    a_m = len(a)
    a_n = len(a[0])
    b_m = len(b)
    b_n = len(b[0])

    if a_n != b_m:
        return -1
    
    c = [[0 for _ in range(b_n)] for _ in range(a_m)]

    for i in range(a_m):
        for j in range(b_n):
            for k in range(a_n):
                c[i][j] += a[i][k] * b[k][j]
	return c