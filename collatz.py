# collatz conjecture, Exercise 3
# starting with a value print to screen
# if even divide by 2
# if odd multiply by 3 and add 1

n = int(input("Insert number for Collatz Sequence: "))
print(n)
while n > 1:
  if (n % 2 == 0):
    n = n / 2
  elif(n % 2 > 0):
    n = (n*3)+1
  print(int(n)) 
