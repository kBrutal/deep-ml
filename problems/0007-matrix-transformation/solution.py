import numpy as np


def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	det_T = np.linalg.det(T)
	det_S = np.linalg.det(S)
	if(det_T == 0 or det_S == 0):
		return -1
	T_inv = np.linalg.inv(T)
	X = T_inv @ A
	transformed_matrix = X @ S
	return transformed_matrix