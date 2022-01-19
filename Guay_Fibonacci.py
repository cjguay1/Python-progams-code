#Purpose: Prints list of fibonacci sequence numbers
#Developer: Christopher Guay

class Fib:
    
    def printFib(): #Defining function within class
        maxcount = int(input("Enter the amount of numbers you want to see: "))
        a = 0  #Defining variables
        b = 0
        c = 1
        n = 0
        while(n<maxcount):
            print(c)
            print(" ")
            a = b
            b = c
            c = a + b
            n = n + 1 
            
    printFib() #calling function
