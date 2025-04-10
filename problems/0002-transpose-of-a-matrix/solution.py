def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	rows = len(a)
    cols = len(a[0])

    transpose = []

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(a[j][i])
        transpose.append(new_row)
    return transpose