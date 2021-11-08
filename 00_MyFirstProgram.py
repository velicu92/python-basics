
# define variables
a = 1.23
x = 10

# print and view variables or variable type
print(x)
print(type(x))
print(type(a))

text1 = "Hello World"
text2 = "Are you ok"
print(text1, "!", text2, "?")

# calculate the SUM
y = x + a
print("Sum of x and a is =",y,"and the type is", type(y))

B = 3
print("Mark is spending",B,"hours daily on Facebook")
print("Mark is spending too many hours daily on Facebook")

print()


# Working directory

import os

print(os.getcwd())   ### print current directory

os.chdir('C:/Work') #changes the current working directory to the specified one

# pay attention to "/" char from the path, some software use "\"

