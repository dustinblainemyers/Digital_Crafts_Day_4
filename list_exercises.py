#Sum the numbers
#Given a list of numbers, print their sum

# list_num = [5,6,8,10,200,34,45]

# summed_num = 0
# for num in list_num:
#     summed_num =+ num

# print(summed_num)


#Largest Number
#Given a list of number, print the largest of the numbers

# largest_number = 0

# numbers_to_compare = [8,200,1,2000,3,45,657,987, 398,43985, 34859, 23,34059,30458]

# for number in numbers_to_compare:
#   if number > largest_number:
#     largest_number = number
 

# print(largest_number)

#smallest number
#Given a list of number, print the smallest of the numbers



# numbers_to_compare = [8,200,100,2000,3,45,657,987, 398,43985, 34859, 23,34059,30458]

# smallest_number = numbers_to_compare[0]
# for number in numbers_to_compare:
#   if number < smallest_number:
#     smallest_number = number
 

# print(smallest_number)

#even numbers
#Given a list of number, print each number in the list that is even



# numbers_to_analyze = [8,200,100,2000,3,45,657,987, 398,43985, 34859, 23,34059,30458]

# print("Even numbers found", end=": ")
# for number in numbers_to_analyze:
#   if number % 2 == 0:
    
#     print(number, end=",")
 

#positive numbers
#Given a list of number, print each number in the list that is greater than zero



# numbers_to_analyze = [8,-200,100,2000,3,45,657,-987, 398,43985, -34859, -23,34059,30458]

# print("Numbers greater than zero found", end=": ")
# for number in numbers_to_analyze:
#   if number > 0:
    
#     print(number, end=",")


#positive numbers 2
# Given a list of number, create a new list which contains every number in give list which is positive.



# numbers_to_analyze = [8,-200,100,2000,3,45,657,-987, 398,43985, -34859, -23,34059,30458]

# positive_list = []
# print("Numbers greater than zero found", end=": ")
# for number in numbers_to_analyze:
#   if number > 0:
    
#     positive_list.append(number)
#   print(positive_list)
# print(positive_list)
 

#Multiply a list
# Given a list of numbers, and a single factor, crate a new list consisting of each of the numbers in the first list mulitiplied by the factor. Print the new list out to the screen.

# numbers_to_multiply = [8,200,1,2000,3,45,657,987, 398,43985, 34859, 23,34059,30458]

# factor = 5

# new_list = []

# for num in numbers_to_multiply:
#   new_list.append(num * 5)
# print(new_list)

#Multiply vectors
# given tow lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists

# numbers_to_multiply1 = [8,200,1,2000,3,45,657,987, 398,43985, 34859, 23,34059,30458]
# numbers_to_multiply2 = [6.0, 150.0, 0.75, 1500.0, 2.25, 33.75, 492.75, 740.25, 298.5, 32988.75, 26144.25, 17.25, 25544.25, 22843.5]
# factor = 5

# new_list = []
# count = 0
# for factor1 in numbers_to_multiply1:
#   new_list.append(factor1 * numbers_to_multiply2[count])
#   count += 1
# print(new_list)
   
#Matrix Addition
# given two two-dimensional lists of numbers of the size 2 x 2 calculate the result of adding the two matrices.

# so I need to take the first indice of the first list and add it to the first indice of the first list on the accompying nested list.  Then take the second indice of the first list and add it to second indice of accompying nested list.

matrix1 = [[1, 3], [2,4],[5,6]]
matrix2 = [[5,2],[1,0],[7,8]]

matrix_leng = 2
matrix_width = 3
new_matrix = []


for dimen in range(matrix_width):
  new_matrix.insert(dimen, [])
  print(dimen)
  
  for num in range(matrix_leng):
    print(new_matrix)
    
    new_matrix[dimen].insert(num, (matrix1[dimen][num] + matrix2[dimen][num]))
    

  

print(new_matrix)


 