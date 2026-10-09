def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	B = -1*(matrix[0][0] + matrix[1][1])
	C = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])

	eigenvalues = []
	eigenvalues.append((- B + ((B**2 - 4*C)**(0.5)))/2)
	eigenvalues.append((- B - ((B**2 - 4*C)**(0.5)))/2)
	return eigenvalues