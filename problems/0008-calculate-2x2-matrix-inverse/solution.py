def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    a,b = matrix[0]
    c,d = matrix[1]

    det = a*d - b*c
    if det == 0:
        return None
    
    inv_d = 1/det
    
    inverse = [[inv_d * d,inv_d * -b],[inv_d * -c, inv_d * a]]
	return inverse