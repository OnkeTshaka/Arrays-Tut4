

print("********************Question 1***************************************")
listExample = ['h','e','l','l','o']

print(len(listExample))

print("********************Question 2***************************************")

mylistExample = [3, 4, 5, 20, 5, 25, 1, 3]

print(mylistExample.pop(1))
print(mylistExample)

print("********************Question 3***************************************")
myList = [1, 5, 5, 5, 5, 1]
max = myList[0]
indexOfMax = 0
for i in range(1, len(myList)):
    if myList[i] > max:
        max = myList[i]
        indexOfMax = i

print(indexOfMax)


print("********************Question 4***************************************")
list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)

print("********************Question 5***************************************")
def f(values):
    values[0] = 44
v = [1, 2, 3]
f(v)
print(v)

print("********************Question 6***************************************")
numbers = [1, 2, 3, 4]

numbers.append([5,6,7,8])

print(len(numbers))

print("********************Question 7***************************************")
veggies = ['carrot', 'broccoli', 'potato', 'asparagus']
veggies.insert(veggies.index('broccoli'), 'celery')
print(veggies)

print("********************Question 8***************************************")
A = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
[A[row][1] for row in (0, 1, 2)]
print(A)

print("********************Question 9***************************************")
A = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
[A[i][i] for i in range(len(A))]
print (A)

print("********************Question 10***************************************")
l=[[1, 2, 3], [4, 5, 6]]
for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j]+=10
print(l)

print("********************Question 11***************************************")
# Find Duplicates
# def  any_dups (A):
#       if len(A) == len(set(A)):
#           return False
#       else:
#           return True
# print(any_dups(A))

def any_dups(A):
    lenghtArr = len(A)
    lenghtSet = len(set(A))
    if lenghtArr == lenghtSet:
        return False
    else:
        return True

A = [1,2,3,4,2,7,8,8,3]
print(any_dups(A))
print("********************Question 12***************************************")

list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
# def find_len(list1):
#     length = len(list1);list1.sort();
#     print("Largest element is:", list1[length - 1]),print("Second Largest element is:", list1[length - 2])
# find_len(list1)

def print_high(list1):
    list1.sort()
    print("Largest element is:", list1[len(list1) - 1])
    print("Second Largest element is:", list1[len(list1) - 2])

print(print_high(list1))
print("********************Question 13***************************************")
def find_missing(A):
    return [x for x in range(A[0], A[-1]+1)
            if x not in A]
A=[1,2,4,6,7,9,10]
print(find_missing(A))


print("********************Question 14***************************************")


#
def printMax(arr):
    max= 0
    maxRow = 0
    maxCol = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] >max:
                max = arr[row][col]
                maxRow =row
                maxCol = col
            print("Max: ",max)
            print("Row at max array: ",(maxRow+1))
            print("Column at max array: ", (maxCol+1))
myArr =[[2,5,7],[4,8,9],[2,7,6]]
for row in range(len(myArr)):
    for col in range(len(myArr[row])):
        print(myArr[row][col],end='')
        print()
printMax(myArr)
