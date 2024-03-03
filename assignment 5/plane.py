from email import utils
from utils import same_name
from passenger import Passenger

def initialize(l):
    p1 = Passenger("Mihai","Andrei",'159')
    l.append(p1)

    p2 = Passenger("Mihut","Andra",'170')
    l.append(p2)

    p3 = Passenger("Neagu","Georgiana",'890')
    l.append(p3)
    
    p4= Passenger('Mihut', 'Cristina', '166')
    l.append(p4)

    p5=Passenger('Bergmann', 'Christian', '987')
    l.append(p5)

    p6= Passenger('Pop', 'Cristina', '743')
    l.append(p6)

    p7= Passenger('Moldovan', 'Iulia', '177')
    l.append(p7)

class Plane:
    def __init__(self,n,a,s,d):
        ''' 
             creates new instance of plane
        '''
        self.__plane = [ ]
        list= [ ]

        initialize(list)
        for i in list:
            self.__plane.append(i)

        self.__name = n
        self.__airline= a
        self.__seats = s
        self.__destination = d
    
    def getName(self):
        '''
            getter method: returns the name of the plane
        '''
        return self.__name
    
    def getAirline(self):
        '''
            getter method: returns the airline of the plane
        '''
        return self.__airline
    
    def getSeats(self):
        '''
            getter method: returns the seats of the plane
        '''
        return self.__seats

    def getDestination(self):
        '''
            getter method: returns the destination of the plane
        '''
        return self.__destination
    
    def getPlane(self):
        '''
            getter method: returns the passengers of the plane
        '''
        return self.__plane
    
    def setName(self,n):
        '''
        setter method: sets the  name for a plane
        '''
        self.__name = n
    
    def setAirline(self,a):
        '''
        setter method: sets the airline for a plane
        '''
        self.__airline = a
    
    def setSeats(self,s):
        '''
        setter method: sets the seats for a plane
        '''
        self.__seats = s

    def setDestination(self,d):
        '''
        setter method: sets the destination of a plane
        '''
        self.__destination = d
    
    def __len__(self):
        '''
        Returns the length of the list.
        IN: -
        OUT: a positive number
        CONDIS: -
        '''
        return len(self.__plane)

    def __str__(self):
        '''
            Returns the string representiation of the plane
        '''
        return ( "Plane " + str(self.__name) + " from airline " + str(self.__airline) + " containing " + 
                str(self.__seats) + " seats, going to " + str(self.__destination) + " and having the passengers " + str(self.__plane))

    def __repr__(self):
        return ( "Plane " + str(self.__name) + " from airline " + str(self.__airline) + " containing " + 
                str(self.__seats) + " seats, going to " + str(self.__destination) + " and having the passengers " + str(self.__plane))

    def _eq_(self,other):
        '''
            Checks if 2 planes are equal or not
        '''
        return self.__name == other.__name and self.__airline == other.__airline and self.__seats == other.__seats and self.__destination == other.__destination

    def add(self,p):
        '''
            setter function - adds passenger to plane
            INPUT: p - Passenger
        '''
        for passenger in self.getPlane():
            if p.getNr() == passenger.getNr():
                return False

        self.__plane.append(p)
        return True  

    def updatePassenger(self,fn,ln,nr,index):
        '''
            updates passenger's first name,last name and passport number 
            INPUT:  fn      =  first name of a passenger
                    ln      =  last name of a passenger
                    pn      = passport number of a passenger
                    index   = passenger's index
        '''
        for passenger in self.getPlane():
            if nr == passenger.getNr():
                return False
        self.getPlane()[index].setFirst(fn)
        self.getPlane()[index].setLast(ln)
        self.getPlane()[index].setNr(nr)
        return True
    
    def deleteAtIndex(self,index):
        '''
            Deletes at a given index
        '''
        self.__plane.pop(index)
    

    def nrWithSameSubstring(self,substr):
        '''
            Returns the nr of passangers in a plane with the same name
        '''
        nr = 0
        for passenger in self.__plane:
            if same_name(passenger.getFirst(),substr):
                nr+=1
        return nr
    
