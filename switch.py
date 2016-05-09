# test array
A=[1, 4, 5, 2, -1, 3, 2]
#  0  1   2  3  4

# function below

def jump(A):
	m = 1
	n = 0
	for i in A:
		if A[n] != -1:
			n = A[n]
			m += 1
	print m

jump(A)

