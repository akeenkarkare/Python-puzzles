#Defining a function.
def getSum(n): 

    #Established "sum" as a veriable.
    sum = 0 

    #Making a while loop, until it hits zero. 
    while (n != 0): 

        #Mod function, gets the remainder
        sum = sum + (n % 10)

        #Quuotient function, which gets, the quotient.
        n = n // 10

    #Returns the sum
    return(sum)

#The input function + variable.
n = int(input("Enter number: "))

#prints the sum of the digits.
print(getSum(n))