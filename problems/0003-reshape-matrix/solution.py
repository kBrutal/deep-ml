import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	elts = len(a)*len(a[0])
	if(new_shape[0]*new_shape[1] != elts):
		return []
	nums = []
	for i in range(len(a)):
		for j in range(len(a[0])):
			nums.append(a[i][j])
	
	cnt = 0
	reshaped_matrix = []
	for i in range(new_shape[0]):
		arr = []
		for j in range(new_shape[1]):
			arr.append(nums[cnt])
			cnt+=1
		reshaped_matrix.append(arr)
	return reshaped_matrix