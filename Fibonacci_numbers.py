# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.

# The desired output is like this:

# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


num=int(input("Please enter any number :  "))
a,b=1,1
fiblist=[a,b]
for i in range(2,num):
  c=a+b
  fiblist.append(c)
  a=b
  b=c
print(fiblist)


