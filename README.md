# Data Structures
<br>
Tutorial 4<br>
**Question 1**
<br>

Suppose listExample is [‘h’,’e’,’l’,’l’,’o’], what is len(listExample)?
a) 5
b) 4
c) None
d) Error
<br>
**Question 2**<br>
Suppose listExample is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after listExample.pop(1)?
a) [3, 4, 5, 20, 5, 25, 1, 3] 
b) [1, 3, 3, 4, 5, 5, 20, 25] 
c) [3, 5, 20, 5, 25, 1, 3] 
d) [1, 3, 4, 5, 20, 5, 25] <br>
**Question 3**<br>
What will be the output of the following Python code?
1. myList = [1, 5, 5, 5, 5, 1]
2. max = myList[0]
3. indexOfMax = 0
4. for i in range(1, len(myList)):
5. if myList[i] > max:
6. max = myList[i]
7. indexOfMax = i
8.
9. >>>print(indexOfMax)
a) 1
b) 2
c) 3
d) 4
<br>
**Question 4**<br>
What will be the output of the following Python code?
1. >>>list1 = [1, 3]
2. >>>list2 = list1
3. >>>list1[0] = 4
4. >>>print(list2)
a) [1, 3] 
b) [4, 3] c) [1, 4] 
d) [1, 3, 4] <br>
**Question 5**<br>
What will be the output of the following Python code?
1. def f(values):
2. values[0] = 44
3.
4. v = [1, 2, 3]
5. f(v)
6. print(v)
a) [1, 44] 
b) [1, 2, 3, 44] 
c) [44, 2, 3] 
d) [1, 2, 3] <br>
**Question 6**<br>
What will be the output of the following Python code?
1. numbers = [1, 2, 3, 4]
2.
3. numbers.append([5,6,7,8])
4.
5. print(len(numbers))
a) 4
b) 5
c) 8
d) 12>br>
**Question 7**<br>
What will be the output of the following Python code?
1. veggies = ['carrot', 'broccoli', 'potato', 'asparagus']
2. veggies.insert(veggies.index('broccoli'), 'celery')
3. print(veggies)
a) [‘carrot’, ‘celery’, ‘broccoli’, ‘potato’, ‘asparagus’]
b) [‘carrot’, ‘celery’, ‘potato’, ‘asparagus’] 
c) [‘carrot’, ‘broccoli’, ‘celery’, ‘potato’, ‘asparagus’] 
d) [‘celery’, ‘carrot’, ‘broccoli’, ‘potato’, ‘asparagus’] <br>
**Question 8**<br>
What will be the output of the following Python code?
A = [[1, 2, 3], [4, 5, 6],
 [7, 8, 9]]
[A[row][1] for row in (0, 1, 2)]
print(A)
a) [7, 8, 9] 
b) [4, 5, 6] 
c) [2, 5, 8] 
d) [1, 4, 7] <br>
**Question 9**<br>
What will be the output of the following Python code?
A = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
[A[i][i] for i in range(len(A))]
print (A)
a) [1, 5, 9] 
b) [3, 5, 7] 
c) [4, 5, 6] 
d) [2, 5, 8] <br>
**Question 10**<br>
What will be the output of the following Python code?
l=[[1, 2, 3], [4, 5, 6]]
for i in range(len(l)):
for j in range(len(l[i])):
l[i][j]+=10
print(l)
a) No output
b) Error
c) [[1, 2, 3], [4, 5, 6]] 
d) [[11, 12, 13], [14, 15, 16]]<br>
**Question 11**<br>
Write a Python function any_dups (A) to find whether a given array of integers contains any 
duplicate element. Return true if any value appears at least twice in the said array and 
return false if every element is distinct.<br>

**Question 12**<br>
Write a function print_high(A) which accepts an array of values and prints the biggest and 
second biggest numbers. Use 3 lines of code in the function.<br>
**Question 13**<br> - this is a popular interview question
An array, A, should store the numbers from 1 to n, BUT one number is missing. Write a 
function find_missing(A) which accepts the array as a parameter and returns the missing 
number. Hint: calculate the sum of all the number that are in the array. The sum of all 
numbers from 1 – n can be calculated as n(n+1) / 2. EG the sum of the numbers 1, 2, 3, 4, 5 
= 15 =(5(5+1)/2)<br>
**Question 14**<br>
Write a function printMax (arr) which accepts an array as a parameter. The function prints the 
maximum value in the array as well as the row and column element numbers where this max value 
occurs. If there exist multiple such elements in different rows and columns, print the one with 
smaller row number and smallest column number
