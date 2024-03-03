
class Passenger:
    def __init__(self,first,last,nr):
        ''' 
             creates new instance of passanger
        '''
        self.__first = first
        self.__last = last
        self.__nr = nr
    
    def __str__(self):
        return( 'Passenger '+ str(self.__nr) + " : " + str(self.__first) + " " + str(self.__last))
    
    def __repr__(self):
        return( 'Passenger '+ str(self.__nr) + " : " + str(self.__first) + " " + str(self.__last))

    def getFirst(self):
        '''
            getter method: returns the first name of the passanger
        '''
        return self.__first
    
    def getLast(self):
        '''
            getter method: returns the last name of the passanger
        '''
        return self.__last

    def getNr(self):
        '''
            getter method: returns the number of the passanger
        '''
        return self.__nr
    
    def setFirst(self,f):
        '''
        setter method: sets the first name for a passanger
        '''
        self.__first = f
    
    def setLast(self,l):
        '''
        setter method: sets the last name for a passanger
        '''
        self.__last = l
    
    def setNr(self,n):
        '''
        setter method: sets the number for a passanger
        '''
        self.__nr = n
        
    def _eq_(self, other):
        '''
        Checks if 2 Patients have the same attributes.
        IN: 2 instances of a class
        OUT: True if equal, else False
        CONDIS: -
        '''
        if self.__first != other.__first and self.__last != other.__last and self.__nr != other.__nr:
            return False
        return True
    
