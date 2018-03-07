#Shane Healy 07-MAR-2018
#Exercise 6
#Single input and return factorial. Test calling 5, 7, 10

def factorial(x):
    f = 1
    for i in range(1,x,1):
        f = f * (i + 1)
    return f


print(f'Factorial of 5 is {factorial(5)}')
print(f'Factorial of 7 is {factorial(7)}')
print(f'Factorial of 10 is {factorial(10)}')