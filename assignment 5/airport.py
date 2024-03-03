from plane import Plane
import utils
from passenger import Passenger
from plane import Plane

def initializeAirport(l):
    p3 = Plane('56465',"TGV",300,"londra")
    p3.add(Passenger("Mihnea","Maria",'6653'))
    p3.add(Passenger("Mihai","Florin",'6546'))
    p3.add(Passenger("Neagu","Florin",'554'))
    p3.add(Passenger("Mogage","Cristina",'51235'))
    p3.add(Passenger("Paris","Hilton",'1566'))
    p3.add(Passenger("Dimitrie","Carina",'7864'))
    p3.add(Passenger("Nicolae","Iorga",'7965'))
    l.append(p3)
    
    p1 = Plane('15540',"BlueAir",100,"Bali")
    p1.add(Passenger("Mihalca","Carina",'514'))
    p1.add(Passenger('Mihut', 'Cristina', '166'))
    p1.add(Passenger('Bergmann', 'Christian', '987'))
    l.append(p1)
    
    p2 = Plane('463546',"Wizz",150,"Maldive")
    p2.add(Passenger('Pop', 'Cristina', '743'))
    p2.add(Passenger('Moldovan', 'Iulia', '177'))
    l.append(p2)

class Airport:
    '''
    A list that contains instances of class Plane.
    '''
    
    def __init__(self):
        '''
        Each instance of the class will have a list of objects Plane
        '''
        self.__airport = [ ]
        list = [ ]
        initializeAirport(list)
        for i in list:
            self.__airport.append(i)
    
    def __len__(self):
        return len(self.__airport)
    
    def getAirport(self):
        '''
            getter function: returns list of Airplanes contained in onbect of
            type Airport
        '''
        return self.__airport

    def addPlane(self,pl):
        '''
            adds an object of type Plane at the end of the list

            INPUT:  pl - Plane
        '''
        return self.__airport.append(pl)

    def updateAirport(self,plane_name,al,nrSeats,dest,index):
        '''
            updates the plane at a certain index
            INPUT:  plane_name  -  plane's name
                    al          -  airLine's name
                    nrSeats     -  number of seats in the Plane
                    dest        -  plane's destination
                    index       - plane's index
        '''
        for pln in self.getAirport():
            if plane_name == pln.getName():
                return False
        self.getAirport()[index].setName(plane_name)
        self.getAirport()[index].setAirLine(al)
        self.getAirport()[index].setSeats(nrSeats)
        self.getAirport()[index].setDestination(dest)
        return True 

    def deleteAtINdex(self,index):
        '''
            if delets a plane at a certain index
            INPUT:  index - plane's index
        '''
        self.getAirport().pop(index)
    
    def clearAirport(self):
        self.__airport.clear()
    
    def sortByLastName(self,plane_index):
        '''
            Sorts passangers by last name
        '''
        plane = self.getAirport()[plane_index].getPlane()
        return utils.mySort(plane, lambda x,y: x.getLast() < y.getLast())

    def sortNrOfPassengers(self):
        '''
            Sort planes according to the number of passengers
        '''
        return utils.mySort(self.__airport,lambda x,y:len(x.getPlane())<len(y.getPlane()))

    def sortNumberAndSubstring(self,subs):
        '''
            Sort planes according to the number of passengers with the first name starting 
            with a given substring
            INPUT: start = string, given substring
        '''
        return utils.mySort(self.__airport,lambda x,y: x.nrWithSameSubstring(subs)<=y.nrWithSameSubstring(subs))

    def sortPassengersAndDestination(self):
        '''
            Sort planes according to the string obtained by concatenation of the number of 
            passengers in the plane and the destination
        '''
        return utils.mySort(self.__airport,lambda x,y: str(len(x.getPlane()))+x.getDestination() <= str(len(y.getPlane()))+y.getDestination())

    def findPassInPlane(self):
        '''
        Identify planes that have passengers with passport numbers starting with the 
        same 3 letters
        '''
        return utils.myFilter(self.getAirport(), utils.same3letters )
          
        
    def findInAPlane(self,index, sub):
        '''
            Identify passengers from a given plane for which the first name or last name
            contain a string given as parameter
        '''
        pln = self.getAirport()[index]
        rez = []
        rez = utils.myFilter(pln.getPlane(), lambda x: x.getFirst().find(sub)!=-1 or x.getLast().find(sub)!=-1)
        return rez
    
    def findByNameInPlane(self,name):
        '''
            Identify plane/planes where there is a passenger with given name
            
        '''
        rez1= [ ]
        for plane in self.getAirport():
            rez2= [ ]
            rez2 = utils.myFilter(plane.getPlane(),lambda x: x.getLast() == name)
            if len(rez2)!=0:
                rez1.append(plane)
        return rez1
    
    def formGroupsOfPas(self,plane_given,k):
        pass
        