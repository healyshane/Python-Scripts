#Shane Healy 03-MAR-2018
#Data from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
#Exercise 5: Read Iris data set and print rows formatted

with open('data/iris.csv') as f:
    
    for line in f:
        x = line.split(",") # splitting data
        print(f'{x[0]} {x[1]} {x[2]} {x[3]}')  #same as print('{} {} {} {}'.format(x[0], x[1], x[2], x[3]))
