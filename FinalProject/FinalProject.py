# -----------------------------------------------------------------
# Assignment Name:      Final Project
# Name:                 Anastasiia Efimova
# -----------------------------------------------------------------
import datetime
from datetime import datetime, timedelta

class Customer:


    def __init__(self, strName, intBikeAmount, strBikeType, strRentType, strDiscount):
        self.Name = strName
        self.BikeAmount = intBikeAmount
        self.BikeType = strBikeType
        self.strRentType = strRentType
        self.strDiscount = strDiscount



    def RequestBike(self, intBikeAmount):

        intBikeAmount = input("How many bikes would you like to rent?: ")
        try:
            intBikeAmount = int(intBikeAmount)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if intBikeAmount < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.intBikeAmount = intBikeAmount

        return self.intBikeAmount



    def RequestBikeType(self, strBikeType):        
        strBikeType = input("Please choose Type of Bike: Enter 'M' for Mountain Bikes, 'T' - Touring Bikes, 'R' - Road Bike ")
        try:
            strBikeType = str(strBikeType)
        except ValueError:
            print("Please Enter 'M' for Mountain Bikes, 'T' - Touring Bikes, 'R' - Road Bike ")
            return -1
        if (strBikeType == 'M') or (strBikeType == 'T') or (strBikeType == 'R'):
            self.strBikeType = strBikeType
            return self.strBikeType



    def RequestRentType(self, strRentType):
            strRentType = input("Please choose Type of rental: Enter 'H' for Hourly (5$), 'D' - Daily(20$), 'W' - Weekly(60$) ")
            try:
               strRentType = str(strRentType)
            except ValueError:
               print("Please Enter 'H' for Hourly (5$), 'D' - Daily(20$), 'W' - Weekly(60$) ")
               return -1
            if (strRentType == 'H') or (strRentType == 'D') or (strRentType == 'W'):
                self.strRentType = strRentType
            return self.strRentType



    def RequestDiscount(self, strDiscount):
        strDiscount = input("Please Enter Discount If you Have any: ")
        try:
            strDiscount = str(strDiscount)
        except ValueError:
            print("There ae NO Discount with this Code ")
        return -1
        if (strDiscount == '***BBP'):
            self.strDiscount = strDiscount
            self.intDiscount = 0.1
        return self.intDiscount
     


    def ReturnBike(self, strRentType, intBikeAmount):
        if strRentType and intBikeAmount:
            return strRentType, intBikeAmount  
        else:
            return '',0



class BikeRental(Customer):



    def __init__(self, strName, intBikeAmount, strBikeType, strRentType, strDiscount, strBikeRentalName, intMountainBikesAmount, intTouringBikesAmount, intRoadBikeAmount, intTotalBikes = 0):
        self.BikeRentalName = strBikeRentalName
        self.MountainBikesAmount = intMountainBikesAmount
        self.TouringBikesAmount = intTouringBikesAmount
        self.RoadBikeAmount = intRoadBikeAmount
        Customer.__init__(self, strName, intBikeAmount, strBikeType, strRentType, strDiscount)
        BikeRental.intTotalBikes = intMountainBikesAmount + intTouringBikesAmount + intRoadBikeAmount

    

    def DisplayStock (self, intMountainBikesAmount, intTouringBikesAmount, intRoadBikeAmount, intTotalBikes):
        print ("The Total Mountain Bikes is  ", intMountainBikesAmount)
        print ("The Total Touring Bikes is  ", intTouringBikesAmount)
        print ("The Total Road Bikes is  ", intRoadBikeAmount)
        print ("The Total Bikes is  ", BikeRental.intTotalBikes)
        return intTotalBikes



    def RentBikeOnHourlyBasis(self, intBikeAmount, RentTime, intTotalBikes):

        if intBikeAmount <= 0:
            print("Number of bikes should be positive!")
            return None

        elif intBikeAmount > self.intTotalBikes:
            print("Sorry! We have currently {} bikes available to rent.".format(self.intTotalBikes))
            return None      
        else:
            RentTime = datetime.now()                     
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(intBikeAmount,RentTime.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            intTotalBikes -= intBikeAmount
            return RentTime      


       
    def RentBikeOnDailyBasis(self, intBikeAmount, RentTime, intTotalBikes):
        
        if intBikeAmount <= 0:
            print("Number of bikes should be positive!")
            return None
        elif intBikeAmount > intTotalBikes:
            print("Sorry! We have currently {} bikes available to rent.".format(intTotalBikes))
            return None
    
        else:
            RentTime = datetime.now()                      
            print("You have rented {} bike(s) on daily basis today at {} hours.".format(intBikeAmount, RentTime.hour))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")
            intTotalBikes -= intBikeAmount
            return RentTime



    def RentBikeOnWeeklyBasis(self, intBikeAmount, RentTime, intTotalBikes):
        if intBikeAmount <= 0:
            print("Number of bikes should be positive!")
            return None
        elif intBikeAmount > intTotalBikes:
            print("Sorry! We have currently {} bikes available to rent.".format(intTotalBikes))
            return None              
        else:
            RentTime = datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(intBikeAmount, RentTime.hour))
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            intTotalBikes -= intBikeAmount
            return RentTime



    def ReturnBike(self, strName, intBikeAmount, strRentType, RentTime, rentalPeriod, now, intTotalBikes, request, bill = 0, dblTotalbill = 0):

        strName = request[0], intBikeAmount = request[1], strRentType = request[2], RentTime = request[3], intTotalBikes = request[4]
        if  strRentType and strRentType and intBikeAmount:
            intTotalBikes += intBikeAmount
            now = datetime.now()
            rentalPeriod = now - RentTime       
            if strRentType == 'H':
                bill = round(rentalPeriod.seconds / 3600) * 5 * intBikeAmount
            elif strRentType == 'D':
                bill = round(rentalPeriod.days) * 20 * intBikeAmount               
            elif strRentType == 'W':
                bill = round(rentalPeriod.days / 7) * 60 * intBikeAmount
            if (3 <= intBikeAmount <= 5):
                print(strName, ", You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            dblTotalbill += bill
            return bill, intTotalBikes, dblTotalbill    
        else:
            print("Are you sure you rented a bike with us?")
            return None
    


        def DisplayTotalPerDay(intTotalBikes, dblTotalbill ):
            print("Total of Bikes Rented for Day - ", intTotalBikes)
            print("Daily Revenue Collected for Day is ${}".format(dblTotalbill))



# -----------------------------------------------------------------
# Function Name:        Validate New Shop Input 
# Function Purpose:     Validate New Shop data
# -----------------------------------------------------------------
def Valid_strNewShop_Input( strNewShop):
        strNewShop = str(strNewShop)
        if (strNewShop == 'Y') or (strNewShop == 'N'):
            global strBln
            strBln = True
        else:
            print("Please Enter Y - for Yes or N - for No ")
        return strNewShop



# -----------------------------------------------------------------
# Function Name:        Validate Bike Type String Input 
# Function Purpose:     Validate Bike Type String data
# -----------------------------------------------------------------
def Valid_BikeType_Input( strBikeType):
        strBikeType = str(strBikeType)
        if (strBikeType == 'M') or (strBikeType == 'T') or (strBikeType == 'R'):
            global strBln
            strBln = True
        else:
            print("Please Enter 'M' for Mountain Bikes, 'T' - Touring Bikes, 'R' - Road Bike ")
        return strBikeType



# -----------------------------------------------------------------
# Function Name:        Validate Bike Type String Input 
# Function Purpose:     Validate Bike Type String data
# -----------------------------------------------------------------
def Valid_strRentType_Input( strRentType):
        strRentType = str(strRentType)
        if (strRentType == 'H') or (strRentType == 'M') or (strRentType == 'W'):
            global strBln
            strBln = True
        else:
            print("Please Enter 'H' for Hourly (5$), 'D' - Daily(20$), 'W' - Weekly(60$) ")
        return strRentType



# -----------------------------------------------------------------
# Function Name:        Validate Shoe Name Input
# Function Purpose:     Validate Shop Name Name 
# -----------------------------------------------------------------
def Valid_strBikeRentalName_Input( strBikeRentalName ):
    strBikeRentalName = str(strBikeRentalName)
    if(strBikeRentalName == ''):
        print("Please Enter The Bike Rental Name ")
        global strBln
        strBln = False
    else:
        strBln = True 
    return strBikeRentalName



# -----------------------------------------------------------------
# Function Name:        Validate Mountain Bikes Input
# Function Purpose:     Validate intMountainBikes data
# -----------------------------------------------------------------
def Valid_intMountainBikesAmount_Input(intMountainBikesAmount):
   try:
        intMountainBikesAmount = int(intMountainBikesAmount)
        if(intMountainBikesAmount >= 0):
            global strBln
            strBln = True
        else:
            print("Please Enter Positive Value.")
   except ValueError:
        intMountainBikesAmount = int(0)
        print("Value Must be Numeric")
   return intMountainBikesAmount



# -----------------------------------------------------------------
# Function Name:        Validate Touring Bikes Input
# Function Purpose:     Validate intTouringBikes data
# -----------------------------------------------------------------
def Valid_intTouringBikesAmount_Input (intTouringBikesAmount):
   try:
        intTouringBikesAmount = int(intTouringBikesAmount)
        if(intTouringBikesAmount >= 0):
            global strBln
            strBln = True
        else:
            print("Please Enter Positive Value.")
   except ValueError:
        intTouringBikesAmount = int(0)
        print("Value Must be Numeric")
   return intTouringBikesAmount



# -----------------------------------------------------------------
# Function Name:        Validate Road Bikes Input
# Function Purpose:     Validate intRoadBikes data
# -----------------------------------------------------------------
def Valid_intRoadBikeAmount_Input (intRoadBikeAmount):
   try:
        intRoadBikeAmount = int(intRoadBikeAmount)
        if(intRoadBikeAmount >= 0):
            global strBln
            strBln = True
        else:
            print("Please Enter Positive Value.")
   except ValueError:
        intRoadBikeAmount = int(0)
        print("Value Must be Numeric")
   return intRoadBikeAmount



# -----------------------------------------------------------------
# Function Name:        Validate strNavigation String Input 
# Function Purpose:     Validate strNavigation String data
# -----------------------------------------------------------------
def Valid_strNavigation_Input( strNavigation):
        strNavigation = str(strNavigation)
        if (strNavigation == '1') or (strNavigation == '2') or (strNavigation == '3') or (strNavigation == '4'):
            global strBln
            strBln = True
        else:
            print("Please Enter '1' - New Customer Rental, '2' - Rental Return, '3' - Show Inventory, '4' - End of Day: ")
        return strNavigation



# -----------------------------------------------------------------
# Function Name:        Validate Name Input
# Function Purpose:     Validate Name Name 
# -----------------------------------------------------------------
def Valid_strName_Input( strName ):
    strName = str(strName)
    if(strName == ''):
        print("Please Enter The Name ")
        global strBln
        strBln = False
    else:
        strBln = True 
    return strName



# ----------------------------------------------------------------------------
# Name:                 Controlling Main Code for Application
# Purpose:              Calculate discounts for Employees when they buy items
# ----------------------------------------------------------------------------

# declare input, output, and other needed variables
strNewShop = str("")
strBikeRentalName = str("")
intMountainBikesAmount = int(0)
intTouringBikesAmount = int(0)
intRoadBikeAmount = int(0)
intTotalBikes = int(0)
strNavigation = str("")
rentalPeriod = datetime.now()

strName = str("")
strBikeType = str("")
strRentType = str("")
strDiscount = str("")
intBikeAmount = int(0)
RentTime = datetime.now()
now = datetime.now()
dblDiscount = float(0)
intcusCount = int(0)
dblRentalBasis = float(0)
bill = float(0)
dblTotalbill = float(0)

intCounter = int(0)
z = str("")



strNewShop = input("Would you like to create a New Shop? Enter Y - for Yes or N - for No ")
strNewShop = Valid_strNewShop_Input( strNewShop)

if (strNewShop == "Y"):

    strBikeRentalName = input("Please Enter The Shop Name ")
    strBikeRentalName = Valid_strBikeRentalName_Input( strBikeRentalName)

    intMountainBikesAmount = input("Please Enter Amount for Mountain Bikes ")
    intMountainBikesAmount = Valid_intMountainBikesAmount_Input( intMountainBikesAmount)

    intTouringBikesAmount = input("Please Enter Amount for Touring Bikes ")
    intTouringBikesAmount = Valid_intTouringBikesAmount_Input( intTouringBikesAmount)

    intRoadBikeAmount = input("Please Enter Amount for Road Bikes ")
    intRoadBikeAmount = Valid_intRoadBikeAmount_Input( intRoadBikeAmount)


while strNavigation != '4':

    strNavigation = input("Please Use Navigation: Enter '1' - New Customer Rental, '2' - Rental Return, '3' - Show Inventory, '4' - End of Day: ")
    strNavigation = Valid_strNavigation_Input( strNavigation)


    if (strNavigation == "1"):

        objCustomer = Customer( strName, intBikeAmount, strBikeType, strRentType, strDiscount)

        strName = input("Please Enter Your Name and ID: ")
        strName = Valid_strName_Input( strName )

        intBikeAmount = objCustomer.RequestBike( intBikeAmount)

        strBikeType = objCustomer.RequestBikeType( strBikeType)
        strRentType = objCustomer.RequestRentType( strRentType)
        strDiscount = objCustomer.RequestDiscount( strDiscount)  

        objBikeRental = BikeRental( strName, intBikeAmount, strBikeType, strRentType, strDiscount, strBikeRentalName, intMountainBikesAmount, intTouringBikesAmount, intRoadBikeAmount, intTotalBikes)
            
        if (strRentType == 'H'):
            RentTime = objBikeRental.RentBikeOnHourlyBasis(intBikeAmount, RentTime, intTotalBikes)
        elif (strRentType == 'D'):
            RentTime = objBikeRental.RentBikeOnDailyBasis(intBikeAmount, RentTime, intTotalBikes)
        else:
            RentTime = objBikeRental.RentBikeOnWeeklyBasis(intBikeAmount, RentTime, intTotalBikes) 

        objCustomer = Customer( strName, intBikeAmount, strBikeType, strRentType, strDiscount)

        objCustomer.ReturnBike(strRentType, intBikeAmount)

        request = (strName, intBikeAmount, strRentType, RentTime, intTotalBikes)



    if (strNavigation == "2"):

        z = input("Please Enter Your Name and ID: ")
        if z == ( strName ):

            objBikeRental = BikeRental( strName, intBikeAmount, strBikeType, strRentType, strDiscount, strBikeRentalName, intMountainBikesAmount, intTouringBikesAmount, intRoadBikeAmount, intTotalBikes)
           
            objBikeRental.ReturnBike(strName, intBikeAmount, strRentType, RentTime, request, bill, rentalPeriod, now, intTotalBikes, dblTotalbill)



    if (strNavigation == "3"):

            objBikeRental = BikeRental( strName, intBikeAmount, strBikeType, strRentType, strDiscount, strBikeRentalName, intMountainBikesAmount, intTouringBikesAmount, intRoadBikeAmount, intTotalBikes)          

            objBikeRental.DisplayStock (intMountainBikesAmount, intTouringBikesAmount, intRoadBikeAmount, intTotalBikes)



    if (strNavigation == "4"):

            objBikeRental = BikeRental( strName, intBikeAmount, strBikeType, strRentType, strDiscount, strBikeRentalName, intMountainBikesAmount, intTouringBikesAmount, intRoadBikeAmount, intTotalBikes)          

            objBikeRental.DisplayTotalPerDay(intTotalBikes, dblTotalbill )