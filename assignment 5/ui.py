from curses.ascii import isalpha
import airport

def start():
    stop = False
    while stop == False:
        printMenu()
        mylist=airport.Airport()
        try:
            option = int(input("Enter an option: "))
        except:
            print("Please enter a valid integer")
            print()
            continue
        else:
            if option>=0 and option<=9:
                if option == 0:
                    print('Exit')
                    stop = True

                elif option == 1:
                    while True:
                        try:
                            index= int(input("Give index: "))
                        except:
                            print("Give correct index: ")
                            print()
                            continue
                        else:
                            if index>=0 and index<len(mylist.getAirport()):
                                print(mylist.sortByLastName(index))
                                break
                            else:
                                print("Index out of range")
                                print()
                                continue
                
                elif option == 2:
                    print(mylist.sortNrOfPassengers())

                elif option == 3:
                    bool = False
                    while bool == False:
                        substring = input("Give substring: ")
                        bool = substring.isalpha()
                        if bool == False:
                            print("Give a correct substring: ")
                    for element in mylist.sortNumberAndSubstring(substring):
                         print(element)

                
                elif option == 4:
                    print(mylist.sortPassengersAndDestination())
                
                elif option == 5:
                    for el in mylist.findPassInPlane():
                        print(el)

                elif option == 6:
                    while True:
                        try:
                            index =int(input( "Give plane: "))
                            string= input("Give string: ")
                            print()
                        except:
                            print("Enter a number")
                            continue
                        else:
                            if index > 0 and index < len(mylist.getAirport()):
                                        for el in  mylist.findInAPlane(index, string):
                                            print(el)
                                        break
                            else:
                                print("Enter index")
                                continue
                elif option == 7:
                    bool = False
                    while bool == False:
                        name = input("Give name: ")
                        bool = substring.isalpha()
                        if bool == False:
                            print("Give a correct name: ")
                    for el in mylist.findByNameInPlane(name):
                        print(el)
                
                elif option == 8 or option == 9:
                    print('I did not know how to do this, sorry :(')

                
def printMenu():
    
    msg = 'Menu:\n'
    msg += "\t 0. Exit\n"
    msg += "\t 1: Sort passangers by last name\n"
    msg += "\t 2: Sort planes according to the number of passengers\n"
    msg += "\t 3: Sort planes according to the number of passengers with the first name starting with a given substring\n"
    msg += "\t 4: Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination\n"
    msg += "\t 5: Identify planes that have passengers with passport numbers starting with the same 3 letters\n"
    msg += "\t 6: Identify passengers from a given plane for which the first name or last name contain a string given as parameter\n"
    msg += "\t 7: Identify plane/planes where there is a passenger with given name\n"
    msg += "\t 8: Form groups of k passengers from the same plane but with different last names\n"
    msg += "\t 9: Form  groups  of  k  planes  with  the  same  destination  but  belonging  to  different  airline companies\n"
    print(msg)

start()