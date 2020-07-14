# 10-1
grades = [40, 55, 70, 58]
g = max(grade)
print(g, "is an A")
for index, grade in enumerate(grades):
    if (grade >= (g - 10)):
        print('Student', index,  "is an A")
    elif (grade >= (g - 20)):
        print('Student', index,  "is an B")
    elif (grade >= (g - 30)):
        print('Student', index,  "is an C")
    elif (grade >= (g - 40)):
        print('Student', index,  "is an D")
    else:
        print("Failure")
        
print(g)

# 10-3
integers = [2, 5, 6, 5, 4, 3, 23, 43, 2]
unique = set(integers)
for each in unique:
    print(each, 'occurs', integers.count(each), 'times')
    
# 10-5
unique = set(integers)


# 10-9
def mean(x):
    return sum(x) / len(x)
def std(x):
    return (sum([(i - mean(x)) ** 2 for i in x]) / (len(x) - 1)) ** (1/2)

integers = [1.9, 2.5, 3.7, 2, 1, 6, 3, 4, 5, 2]
print(mean(integers), std(integers))


# 11-1
def sumColumn(m, index):
    return sum([row[index] for row in m])
m = [[1.5, 2, 3, 4], [5.5, 6, 7, 8], [9.5, 1, 3, 1]]
sumColumn(m, 0)


# 11-2
def sumMajorDiagonal(m):
    return sum([row[i] for i, row in enumerate(m)])
m = [[1, 2, 3, 4], [5, 6.5, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
sumMajorDiagonal(m)


# 11-4
def sum_weekly_hours(m):
    return [sum(row) for row in m]
hours = [[2, 4, 3, 4, 5, 8, 8],\
         [7, 3, 4, 3, 3, 4, 4],\
         [3, 3, 4, 3, 3, 2, 2],\
         [9, 3, 4, 7, 3, 4, 1],\
         [3, 5, 4, 3, 6, 3, 8],\
         [3, 7, 4, 8, 3, 8, 4],\
         [6, 3, 5, 9, 2, 7, 9]]
sum_weekly_hours(hours)


