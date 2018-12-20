'''
Kyle Nida
Z 23410025
Homework 2
Due: 9/30/2018
'''


#Problem 1
'''For any natural number n, define the complex number defined in homework. 
Write a Python function cool_matrix(n), which for any given natural number n, 
returns the n x n matrix (defined in homework) with complex entries. To represent 
matrices, use the same convention as in class, i.e., a matrix is represented as 
a list of lists.
Hint: The cmath module contains various functions that can handle complex numbers. '''


'''I tried my best for this problem, not sure I got it exactly how you
want it. I created an n x n matrix sort of how we did in class, then
instead of how we solved a matrix addition of multiplication, I input
the proper formula that you gave us in the assignment at the right place
to place them in the matrix spot arrived at by the for loops.'''

from cmath import *

def cool_matrix(n):
    
    #initialize empty matrix of dim n X n
    cool_mat = [[0 for i in range(n)] for j in range(n)]

    for i in range(n): #row
        for j in range(n): #column
            '''setting value of matrix equal to formula given in 
            homework with 'n' and complex values 'i' and 'j' plugged in'''
            cool_mat[i][j] = exp(((-2*pi*i*j)/n)) / sqrt(n) 

    return cool_mat #returns final matrix

#Problem 2
'''Write a Python function compose(p1,p2), which computes the composition of two 
permutations, i.e., the permutation that first applies (the permutation represented 
by the list) p2 and then applies (the permutation represented by the list) p1. Your 
function must check that p1 and p2 represent valid permutations on the same set of 
numbers.'''

#Helper checking if the lists are permutations of eachother
def check(p1,p2):
    
    '''check for string length, case 1 check
    if the lengths are not equal, returns false'''
    if len(p1) != len(p2):
        return False

    p1_new = sorted(p1) #sorts p1 for checking
    p2_new = sorted(p2) #sorts p2 for checking
    
    '''For loop using the length of p1 as the lengths of the lists are assumed 
    equal if previous check returned true. Checks if the values of the new, sorted 
    lists are equal eachother, if yes, returns true, if no, returns false'''
    for i in range(len(p1)):
        if p1_new[i] != p2_new[i]:
            return False

    return True

#Function for problem 2
def compose(p1,p2):

    comp = [] #list of the composition of the 2 given permutations
    x = len(p1) #length of the lists as they are known to be equal

    if check(p1,p2) == True: #check function implementation
        for i in range(x): #walkthrough of first permutation
            for j in range(x): #walkthrough of second permutation
                '''if statement to check each value of first permutation
                against each value of second permutation'''
                if p1[i] == p2[j]: 
                    comp.append(j) #adds positional value 'i' to comp list

    return comp #returns final composition

#Problem 3
'''With the same conventions as in Problem 2, write a function is_power(p1,p2), 
which returns True, if and only if the permutation p2 can be obtained by repeatedly 
composing the permutation p1 with itself. For instance, is_power([1,2,0],[0,1,2]) 
must return True, and is_power([0,1,2],[2,1,0]) must return False.'''

#Function for problem 3
def is_power(p1,p2):
    
    temp = [x for x in p1] #copy of p1 for additional compositions
    const = [x for x in temp] #constant to check for repeating compositions

    temp = compose(temp,p1) #first composition

    '''
    Checks for equivalence after first composition.
    '''
    if temp == p2:
        return True

    '''
    Loop for compositions while temp (copy of p1) does not equal 
    target value (p2) AND temp (copy of p1) does not equal our 
    constant list which allows the loop to stop after the first
    repeating value is found.
    '''
    while temp != p2 and temp != const:
        temp = compose(temp,p1) #call to compose for composition computation
        if temp == p2: #if temp ever equals p2, returns true
            return True
        
    return False #if p2 is never met, returns false 

#Main function for testing.
if __name__ == '__main__':
    #tester for problem 1
    print(cool_matrix(2))

    #tester for problem 2
    p1 = [1,0,2]
    p2 = [1,2,0]
    print(compose(p1,p2))

    #tester for problem 3
    print(is_power(p1,p2))