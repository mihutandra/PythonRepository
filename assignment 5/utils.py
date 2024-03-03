

from pickle import FALSE
from random import getrandbits


def mySort( array , k ):
    '''
        the function returns the sorted list of elements by the rule given 
        by the function key
        INPUT:
            array - list of elements
            k - function to be applied
    '''
    for i in range(0,len(array)-1):
        for j in range(i+1, len(array)):
            if not( k(array[i],array[j]) ):
                array[i],array[j] = array[j],array[i]
    return array


def myFilter(array, k):
    '''
        the function returns the list of elements from the given list that 
        meets the criteria given by the function
        INPUT:
            array - list of elements
            key - function to be applied
    '''

    res = [ ]
    for elem in array:
       if k(elem):
           res.append(elem)
    return res

def same_name(name,sub):
    '''
        the function verifiies if the given string "name" starts with the given
        substring "sub" and returns True if the conditions is verified and
        False otherwise
        INPUT:  name - string, the string which you want to be verified
                sub - string, the substring that is being searched in the 
                      string "name"  
    '''
    if len(sub) > len(name):
        return False
    for i in range(len(sub)):
        if name[i] != sub[i]:
            return False
    return True

def same3letters(plane):
    for i in range(len(plane.getPlane())-1):
        for j in range(i+1, len(plane.getPlane())):
            if plane.getPlane()[i].getNr()[0:3] == plane.getPlane()[i].getNr()[0:3]:
                return True
    return False
    
def getNext(index):
    return index+1

def initSolution(domain):
    return domain[0]   

def isConsistent(sol, myList, constraints):
    for c in constraints:
        if not c(sol, myList):
            return False
    return True

def getLast(domain):
    return domain[ len(domain) - 1 ]

def isSolution(sol, param):
    return len(sol) == param[0] 

def myBacktracking(param, myList, constraints):
    '''
    Forms groups of elements from the myList.
    IN: a list, a list, a list with functions.
    OUT: one or more lists with indices
    CONDIS: -
    '''
    domain = [  i  for i in range(-1, len(myList))   ]
    k = 0 #indexul curent din solutie 'sol'
    sol = [] #solutia, la fiecare pas, lista cu indici
    sol.append(initSolution(domain))

    while(k >= 0):
        isSelected = False
        while not isSelected and sol[k] < getLast(domain):
            sol[k] = getNext( sol[k] )
            isSelected = isConsistent( sol, myList, constraints )
        
        if isSelected:
            if isSolution(sol, param):
                yield sol
            else:
                k = k+1
                sol.append(initSolution(domain))
        else:
            sol.pop()
            k = k - 1