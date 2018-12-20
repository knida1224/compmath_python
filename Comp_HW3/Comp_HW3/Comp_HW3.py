'''
Kyle Nida
Z 23410025
Due: 10/29/2018
'''

#Problem 1
'''Write a function countdown(n), which in 1-second intervals outputs n messages of the form 
"n seconds to go", "n-1 seconds to go", ..., "2 seconds to go", "1 second to go", and then 
returns the string "Countdown finished." Your program must ensure that the countdown cannot be 
interrupted by pressing Ctrl-C.'''

from time import sleep
import signal

#Helper function blocking CTRL-C
def c_block(signum, frame):
    print("CTRL-C NOT ACCEPTED")

#Signal handle call blocking ctrl-c
signal.signal(signal.SIGINT, c_block)

#Countdown function
'''counts down from a given 'n' every second'''
def countdown(n):
    
    while (n > 0): #Stops when n reaches zero
        print(n, "seconds to go")
        n-=1
        sleep(1) #Second counter from time library
        if (n == 0):
            print("Countdown finished")


#Problem 2
'''Write four functions to compute the factorial n! of a non-negative integer n:

   func1(n) must use a for-loop, no while-loop, and no recursion.
   func2(n) must use no for-loop, a while-loop, and no recursion.
   func3(n) must use no for-loop, no while-loop, but recursion.
   func4(n) builds a list [1...n] and applies the reduce command from the functools module to this list to find n!.
'''
#Factorial of n with a for-loop
def func1(n):
    #base cases
    if (n < 0): #Can't have negative factorial
        return False
    elif (n == 0): #0!=1
        return 1
    elif (n == 1): #1!=1
        return 1
    else:
        fact = 1 #starting value eliminates zero
        
        '''For loop going from 2 (don't need zero or one because of our base case)
           to n+1 because going to n doesn't include the final value
        '''
        for x in range (2,n+1): 
            fact = fact * x #fact * x ---> x goes to n+1

        return fact

#Factorial of n with a while-loop
def func2(n):
    #base cases
    if (n < 0): #Can't have negative factorial
        return False
    elif (n == 0): #0!=1
        return 1
    elif (n == 1): #1!=1
        return 1
    else:
        fact = 1 #starting value eliminates zero
        #while loop, similar to setup of for-loop in func1
        while(n>1):
            fact = fact * n
            n-=1
        return fact

#Factorial of n with recursion
def func3(n):
    #base cases
    if (n < 0): #Can't have negative factorial
        return False
    elif (n == 0): #0!=1
        return 1
    elif (n == 1): #1!=1
        return 1
    else:
        '''Recursion for factorial of n. Works similarly
        to the previous functions. Takes n and multiplies 
        it with n-1 until a base case is found.'''
        return n*func3(n-1)


#Factorial of n with a reduce
from functools import reduce

def func4(n):

    final = [] #list of found values
   
    #base cases
    if (n < 0): #Can't have negative factorial
        return False
    elif (n == 0): #0!=1
        return 1
    elif (n == 1): #1!=1
        return 1
    else:
        #for loop building list
        for x in range (n):
            fact = n * (n-1) #Gets values for factorial mult.
            if(fact!=0): #If a negative entry is found, it is not added to list
                final.append(fact)
            n-=2 #Subtracts n by 2 for satisfaction of function
            if(n<=0): #If n ever goes negative, we break
                break
       
        fact = reduce((lambda x, y: x * y), final) #reduce for list mult.
        return fact

#Problem 3
'''
Write a Python class TinyNumber as follows:

    Instances of this class are generated by providing an integer x such that LaTeX: 0\le x\le999 0 ≤ x ≤ 999 , e.g., we can write a=TinyNumber(42).
    Provide an implementation of __str__ , returning a representation of the number as English text. E.g., print(TinyNumber(12)) should return the string "twelve".
    Provide an implementation of +, adding two TinyNumbers modulo 1000.
    Provide an implementation of == to check if two TinyNumbers are equal.
'''

class TinyNumber:
    def __init__(self, num):
        self.num = num
        if (self.num < 0) or (self.num > 999):
            raise ValueError("Number out of range")

    def __str__(self):
            
        nums_one_to_nine=["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        nums_ten_to_nineteen=["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen","Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        nums_twenty_to_ninety=[" ", " ","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        #Returned string representation of given number 0-999
        ret_num = ""
    
        if self.num == 0: #base case for zero entry
            ret_num = nums_one_to_nine[0]
        
        # calculations for ones,tens,and hundreds places
        hundreds_place = (self.num % 1000) // 100
        tens_place = (self.num % 100) // 10
        ones_place = (self.num % 10)
        
        # Coordinating calculations above with the values in each list entered
        if (hundreds_place > 0): #hundreds 
            ret_num = ret_num + nums_one_to_nine[hundreds_place] + " Hundred "
    
        if (tens_place > 1): #tens more the one
            ret_num = ret_num + nums_twenty_to_ninety[tens_place] + " "
        
        if (tens_place == 1): #tens = 1
            ret_num = ret_num + nums_ten_to_nineteen[ones_place] + " "

        else: 
            if (ones_place > 0): #puts ones on after tens
                ret_num = ret_num + nums_one_to_nine[ones_place] + " "
        
        return ret_num 

    def __add__(self, other):
        #pow returns x**y % z. This is the addition mod 1000
        return ((pow(self.num,1,1000)+(pow(other.num,1,1000))))

    def __eq__(self, other):
        if(self.num == other.num):
            return True
        else:
            return False


#Main function
if __name__ == '__main__':
    #tester from Problem 1
    countdown(5)

    #testers for Problem 2
    print(func1(7))
    print(func2(7))
    print(func3(7))
    print(func4(7))
   
    #tester for Problem 3
    #for str
    print(TinyNumber(201))
    #test for add
    a = TinyNumber(702)
    b = TinyNumber(12)
    print(a+b)
    #test for eq
    print(b == a)

    
    
    
