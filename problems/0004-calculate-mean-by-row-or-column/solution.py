def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	rows, cols = len(matrix), len(matrix[0])
	if mode == 'column':
		for j in range(cols):
			s = 0
			for i in range(rows):
				s+=matrix[i][j]
			means.append(s/rows)
	
	else:
		for i in range(rows):
			s = 0
			for j in range(cols):
				s+=matrix[i][j]
			means.append(s/cols)
	return means