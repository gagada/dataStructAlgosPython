'''
DATE: 2019-11-06
NAME: GERARD AGADA BCOMP,BCOMM
GITHUB USERNAME: GAGADA
DESC: Chapter 1 Exercises from the Data Structures & Algorithms in Python Book by: Goodrich, Tamassia & Goldwasser.
'''
import math 
import random

#Reinforcement

'''
R-1.1 Write a short Python function, is multiple(n,m), that takes two integer
values and returns True if n is a ultiple of m, that is n = mi for 
some integer i, and False otherwise.
'''
def is_multiple(n,m):
	n = int(n)
	m = int(m)

	if (n % m) ==  0:
		return True
	else:
		return False
'''
R-1.2 Write a short python function is_even(k), that takes an integer value and 
returns True if k is even, and False otherwise. However, your function cannot
use the multipliation, modulo or division operators. 
'''
def is_even(k):
	if k & 1 == 0:
		return True
	return False 
'''
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the 
form of a tuplw of length two. Do not use the built-in functions min or 
max in implementing your solution.
----> print(data) in function if you want a clearer picture.
'''
def minmax(data):
	min_data = data[0]
	max_data = data[0]

	for i in range(len(data)):
		if data[i] <= min_data:
			min_data = data[i]
		elif data[i] >= max_data:
			max_data = data[i]
	return min_data, max_data
'''
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''
def sum_squares(n):
	i_squared = 0
	square_list = []
	for i in range(1,n):
		square_list.append(i)
		i_squared += math.pow(i,2)
	result = math.pow(sum(square_list),2)/len(square_list)
	reuslt = i_squared - result
	return reuslt 
'''
R-1.5 Give a single command that computes the sum from the Top exercise
relying on Python's comprehension syntax and the built-in sum function
'''
total = sum(k * k for k in range(1,10))

'''
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive intgers smaller than n.
'''
def oddsum_squares(n):
	i_squared = 0
	square_list = []
	for i in range(1,n):
		if(i % 2 == 1):
			square_list.append(i)
			i_squared += math.pow(i,2)
	result = math.pow(sum(square_list),2)/len(square_list)
	reuslt = i_squared - result
	return reuslt   

def main():
	
	print("*is_multiple Test*")
	n = random.randint(0,20)
	m = 2
	result = is_multiple(n,m)
	print(n)
	print(result)
	
	print("*is_even Test*")
	k = random.randint(0,20)
	print(k)
	print(is_even(k))

	print("*minmax Test*")
	data = [random.randint(1,20) for i in range (10)]
	nmin,nmax = minmax(data)
	print("Min:", nmin)
	print("Max", nmax)

	print("*sum_squares Test*")
	n = random.randint(1,21)
	ss = sum_squares(n)
	print("n = ", n)
	print("Sum of squares", ss)

	print("*oddsum_squares Test*")
	ss = oddsum_squares(n)
	print("n = ", n)
	print("Odd Sum of squares", ss)

if __name__ == "__main__":
    main()