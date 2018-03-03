#Shane Healy, 25-FEB
# 2,520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any 
# remainder. Write a Python program using for and 
# range to calculate the smallest positive number 
# that is evenly divisible by all of the numbers 
# from 1 to 20. 
  
n = 0
y = 1

while y != 0: # continue loop until y=0
  n = n + 2520 # increase by smallest number divisible 1:10

  for i in range(1,20,1): 
    y = n % (i)   

    if y != 0: 
      break
      
print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is ", n)

