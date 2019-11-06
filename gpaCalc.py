'''
DATE: 2019-11-06
NAME: GERARD AGADA BCOMP,BCOMM
GITHUB USERNAME: GCAGADA
DESC: A basic python program that computes the grade-point-average GPA
'''
print("Hello, Welcome to the GPA Calculator.")
print("Please enter all your letter grades and enter on per line.")
print("Enter a blank line to designate the end of the program.")

#Mapping from letter grade to point value
points = {'A+':4.0,'A':4.0,'A-':3.67,'B+':3.33,'B':3.0,'B-':2.67,'C+':2.33,'C':2.0,'C-':1.67,'D+':1.33,'D':1.0,'F':0.0}

num_courses = 0
total_points = 0 
done = False

while not done:
	grade = input()
	if grade == '':
		done = True 
	elif grade not in points:
		print("This is an unknown grade '{0}' being ignored".format(grade))
	else:
		num_courses += 1 
		total_points += points[grade]

if num_courses > 0:
	print('Your Final GPA is {0:.3}'.format(total_points/num_courses))

