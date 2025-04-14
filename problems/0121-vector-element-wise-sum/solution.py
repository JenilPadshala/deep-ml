def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	l_a = len(a)
    l_b = len(b)

    if l_a != l_b:
        return -1
    result = []

    for i in range(l_a):
        summ = a[i]+b[i]
        result.append(summ)
    return result