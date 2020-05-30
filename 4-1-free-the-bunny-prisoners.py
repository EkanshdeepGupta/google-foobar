import math

def solution(num_buns, num_required):
	if num_required == 0:
		return [[] for i in range(num_buns)]

	num_keys = combi(num_buns, num_required-1)

	ans_array = [[] for i in range(num_buns)]

	permutation_iter = [i for i in range(num_buns - num_required + 1)]

	for i in range(num_keys):
		for j in permutation_iter:
			ans_array[j].append(i)

		nextPerm(permutation_iter, num_buns)

	return ans_array


def nextPerm(arr, num):
	lastIndex = len(arr)-1
	for i in range(len(arr)):
		if not arr[lastIndex-i] == num-1-i:
			break

	arr[lastIndex-i] += 1

	for j in range(1,i+1):
		arr[lastIndex-i+j] = arr[lastIndex-i]+j


def combi(n,k):
	return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))