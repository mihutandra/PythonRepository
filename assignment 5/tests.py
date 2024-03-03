
import unittest
import utils
from plane import Plane 
from plane import initialize as g
from airport import Airport
from airport import initializeAirport as f
from passenger import Passenger

class TestingUtils(unittest.TestCase):
    def test_mySort(self):
        l = ['a','h','e','b']
        utils.mySort(l, lambda x,y: x<=y)
        self.assertEqual(l,['a','b','e','h'])

        l1 = [[1,-1,'a'],[3,2,'z'],[1,10,'c'],[5,6,'b']]
        utils.mySort(l1, lambda x,y: x[0]<y[0])
        self.assertEqual(l1,[[1,10,'c'],[1,-1,'a'],[3,2,'z'],[5,6,'b']])

        utils.mySort(l1, lambda x,y: x[2]<y[2])
        self.assertNotEqual(l1,[[3,2,'z'],[1,-1,'a'],[5,6,'b'],[1,10,'c']])

    def test_mySearch(self):
        l = [[1,-1,'ana'],[3,2,'maria'],[1,10,'carina'],[5,-6,'andreea']]
        rez = utils.myFilter(l,lambda x: x[1]%2 == 0)
        self.assertEqual(rez,[[3,2,'maria'],[1,10,'carina'],[5,-6,'andreea']])

        rez = utils.myFilter(l,lambda x: x[2][0:2] == 'an')
        self.assertEqual(rez,[[1,-1,'ana'],[5,-6,'andreea']])

        rez = utils.myFilter(l,lambda x: x[0]<=0)
        self.assertEqual(rez,[])

    def test_same(self):
        self.assertTrue(utils.same_name('Maria','Mar'))
        self.assertFalse(utils.same_name('Maria','mar'))
        self.assertFalse(utils.same_name('Maria','Mariaa'))


class TestingPassengers(unittest.TestCase):
    def test_setFirstName(self):
        p1 = Passenger('Neag','Georgiana','RO6546')
        p1.setFirst('Alina')
        self.assertEqual(p1.getFirst(),'Alina')

        p1.setFirst('NeAgu')
        self.assertNotEqual(p1.getFirst(),'Neagu')

        p1.setFirst('NeagU')
        self.assertEqual(p1.getFirst(),'NeagU')

    def test_setLastName(self):
        p1 = Passenger('Neag','Georgiana','RO6546')
        p1.setLast('Teo')
        self.assertEqual(p1.getLast(),'Teo')

    def test_setPassport(self):
        p1 = Passenger('Neag','Georgiana','RO6546')
        p1.setNr('RO65465')
        self.assertEqual(p1.getNr(),'RO65465')

        p1.setNr('65465')
        self.assertNotEqual(p1.getNr(),'RO65465')

    def test_getFirstName(self):
        p1 = Passenger('Neagu','Georgiana','RO6546')
        self.assertEqual(p1.getFirst(),'Neagu')
        self.assertNotEqual(p1.getFirst(),'Georgiana')

        p1 = Passenger('Incze','Victor','RO6546')
        self.assertEqual(p1.getFirst(),'Incze')

    def test_getLastName(self):
        p1 = Passenger('Neagu','Georgiana','RO6546')
        self.assertNotEqual(p1.getLast(),'Neagu')
        self.assertEqual(p1.getLast(),'Georgiana')

        p1 = Passenger('Incze','Victor','RO6546')
        self.assertEqual(p1.getLast(),'Victor')

    def test_getPassport(self):

        p1 = Passenger('Neagu','Georgiana','6546')
        self.assertEqual(p1.getNr(),'6546')
        self.assertNotEqual(p1.getNr(),6546)

class TestingPlanes(unittest.TestCase):
    def test_set_name(self):
        p = Plane('15540',"BlueAir",100,"Bali")
        p.setName('543')
        self.assertEqual(p.getName(),'543')
        self.assertNotEqual(p.getName(),543)
        p.setName('RO9748')
        self.assertEqual(p.getName(),'RO9748')

    def test_set_nrSeats(self):
        p = Plane('15540',"BlueAir",100,"Bali")
        p.setSeats(20)
        self.assertEqual(p.getSeats(),20)
        self.assertNotEqual(p.getSeats(),'20')
        self.assertNotEqual(p.getSeats(),100)

    def test_set_destination(self):
        p = Plane('15540',"BlueAir",100,"Bali")
        p.setDestination('Hawaii')
        self.assertEqual(p.getDestination(),'Hawaii')
        self.assertNotEqual(p.getDestination(),'Bali')

    def test_get_myPlane(self):
        l=[]
        rez=[]
        pl = Plane('463546',"Wizz",150,"Maldive")

        p1 = Passenger("Mihai","Nicolae",'159')
        l.append(p1)
        p2 = Passenger("Mihut","Andra",'170')
        l.append(p2)
        p3 = Passenger("Rotoiu","Cristina",'890')
        l.append(p3)

        rez = pl.getPlane()
        for i in range(len(l)):
            self.assertFalse(l[i] == rez[i])

    def test_get_name(self):
        pl = Plane('463546',"Wizz",150,"Maldive")
        self.assertEqual(pl.getName(), '463546')

        pl1 = Plane('15540',"BlueAir",100,"Bali")
        self.assertEqual(pl1.getName(), '15540')
        self.assertNotEqual(pl1.getName(), 15540)


    def test_get_nrSeats(self):
        pl = Plane('463546',"Wizz",150,"Maldive")
        self.assertEqual(pl.getSeats(), 150)

        pl1 = Plane('15540',"BlueAir",100,"Bali")
        self.assertEqual(pl1.getSeats(), 100)
        self.assertNotEqual(pl1.getSeats(), "100")

    def test_get_destination(self):
        pl = Plane('463546',"Wizz",150,"Maldive")
        self.assertEqual(pl.getDestination(), 'Maldive')

        pl1 = Plane('15540',"BlueAir",100,"Bali")
        self.assertEqual(pl1.getDestination(), 'Bali')

        pl2 = Plane('15540',"BlueAir",100,"Hawaii")
        self.assertEqual(pl2.getDestination(), 'Hawaii')

    def test_add(self):
        pl = Plane('463546',"Wizz",150,"Maldive")
        p= Passenger('Incze','Victor','RO5456')
        pl.add(p)
        self.assertFalse(pl.getPlane()[3] == p)

        p1 = Passenger("Mihai","Nicolae",'159')
        self.assertFalse(pl.add(p1))
        
        p2=Passenger('Incze','Victor','5456')
        pl.add(p2)
        self.assertFalse(pl.getPlane()[4] == p2)

    def test_updatePsg(self):
        pl = Plane('463546',"Wizz",150,"Maldive")
        pl.updatePassenger('Sebesan','Claus','561',1)
        p = Passenger('Sebesan','Claus','561')
        self.assertFalse(pl.getPlane()[1] == p)
        
        self.assertFalse(pl.updatePassenger("Cristina","Maria",'890',2))

        self.assertTrue(pl.updatePassenger("Cristina","Maria",'100',2))

    def test_deleteAtIndex(self):
        pl = Plane('463546',"Wizz",150,"Maldive")
        l = []
        g(l)
        pl.deleteAtIndex(1)

        self.assertFalse(l == pl.getPlane())

        l.pop(1)
        self.assertListEqual(l , pl.getPlane())

        pl1 = Plane('15540',"BlueAir",100,"Bali")
        l1 = []
        g(l1)
        l1.pop(0)
        pl1.deleteAtIndex(0)

        self.assertListEqual(l1,pl1.getPlane())


    def test_nrSameSubstr(self):
        pl = Plane('463546',"Wizz",150,"Maldive")
        nr = pl.nrWithSameSubstring('Mih')
        self.assertNotEqual(nr,2)

        nr = pl.nrWithSameSubstring('ih')
        self.assertEqual(nr,0)

        nr = pl.nrWithSameSubstring('rot')
        self.assertEqual(nr,0)



class TestingAirport(unittest.TestCase):
    def test_updateAirport(self):
        l = []
        f(l)
        air = Airport()
        air.updateAirport('657','FranceAirline','50','Dublin',0)

        self.assertFalse(l==air.getAirport())

        pl = Plane('657','FranceAirline','50','Dublin')
        l[0] = pl

        self.assertListEqual(l,air.getAirport())

        self.assertFalse(air.updateAirport('657','Wizz','500','London',0))


    def test_clearAirport(self):
        air1 = Airport()
        air1.clearAirport()
        self.assertListEqual(air1.getAirport(),[])

        air1.clearAirport()
        self.assertListEqual(air1.getAirport(),[])

        pl = Plane('6513',"BlueAir",150,"Zurich")
        air1.addPlane(pl)
        air1.clearAirport()
        self.assertListEqual(air1.getAirport(),[])

    def test_sort_NrOfPassengers(self):
        air1 = Airport()
        air1.clearAirport()
        air1.sortNrOfPassengers()
        self.assertEqual(air1.getAirport(),[])

        pl1 = Plane('6513',"BlueAir",150,"Zurich")
        pl2 = Plane('564',"Wizz",100,"Malaga")
        pl3 = Plane('5321',"AmericanAirLines",0,"London")
        air1.addPlane(pl1)
        air1.addPlane(pl2)
        air1.addPlane(pl3)
        air1.sortNrOfPassengers()
        self.assertListEqual(air1.getAirport(),[pl3,pl2,pl1])

        air1.updateAirport('5321',"AmericanAirLines",100,"London",0)
        self.assertListEqual(air1.getAirport(),[pl3,pl2,pl1])

    def test_sort_NrAndStr(self):
        air1 = Airport()
        air1.clearAirport()

        p3 = Plane('56465',"TGV",300,"Paris")
        p3.add(Passenger("Ana","Maria",'6653'))
        p3.add(Passenger("Neagu","Florin",'6546'))
    
        p1 = Plane('15540',"BlueAir",100,"Bali")
        p1.add(Passenger("Ana","Maria",'6653'))
        p1.add(Passenger("Ana","Florin",'6546'))
    
        p2 = Plane('463546',"Wizz",150,"Maldive")
        p2.add(Passenger("Hodut","Casian",'514'))

        air1.addPlane(p3)
        air1.addPlane(p1)
        air1.addPlane(p2)

        air1.sortNumberAndSubstring('Mih')
        self.assertListEqual(air1.getAirport(),[p3,p1,p2])

        air1.sortNumberAndSubstring('Ana')
        self.assertListEqual(air1.getAirport(),[p2,p3,p1])

        air1.sortNumberAndSubstring('ana')
        self.assertListEqual(air1.getAirport(),[p2,p3,p1])

    def test_fingInGivenPlane(self):
        air = Airport()

        p1 = Passenger("Mihai","Ardelean",'159')
        p2 = Passenger("Mihut","Andra",'170')
        p3 = Passenger("Rotoiu","Cristina",'890')
        p4 = Passenger("Mihnea","Maria",'6653')
        p5 = Passenger("Mihai","Florin",'6546')
        p6 = Passenger("Neagu","Florin",'554')
        p7 = Passenger("Mogage","Cristina",'51235')
        p8 = Passenger("Paris","Hilton",'1566')
        p9 = Passenger("Dimitrie","Carina",'7864')
        p10 = Passenger("Nicolae","Iorga",'7965') 

        self.assertListEqual(air.findInAPlane(0,'lo'),[p5,p6])
        self.assertListEqual(air.findInAPlane(0,'Ni'),[p1,p10])
        self.assertListEqual(air.findInAPlane(0,'Sti'),[])
       
if __name__ == "__main__":
    unittest.main()