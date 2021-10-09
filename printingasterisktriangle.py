#This is where I define the input variable, responsible for knowing how big/wide the triangle should be.
rows = int(input('Enter the number of asterisks you want on the base: '))

#This variable is assigned to leave space behind the asterisks, so it will make a equilateral triangle.
spaces = (2 * rows) - 2 

#This is where the printing of the triangles begins.
for r in range(0, rows):
    for s in range(0, spaces):

        #Here, this is what the above space variable is going to print behind the asterisks, to leave some space.
        print(end = " ")

    #As we are going from bottom to up, this "space" variable decreases after every loop. 
    spaces = spaces - 2

    #The reason why I've put "r + 1" here is because for loops take (0 - 5) when we give them a range of 6.
    for s in range(0, r + 1):
#printing functions for printing the final triangle:
        print("* ", end = ' ')
    print("")