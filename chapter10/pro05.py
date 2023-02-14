class Train:
    def __init__(self , name, fare, nofseats):
        self.name = name
        self.fare = fare 
        self.nofseats = nofseats
    def getstatus(self):
        print(f"the name of the train is {self.name} and fare is {self.fare} and number of seats are {self.nofseats}")
    
    def numberofseats(self):
        print(f"the seats are {self.nofseats}")
    
    def bookticket(self):
        if int(self.nofseats)>0:
            print(f"your ticket is booked and your seat number is {self.nofseats}! happy Yatra")
            self.nofseats = int(self.nofseats)-1
            print(f"khow seats avilable is - {self.nofseats}")
        else:
            print("this train is full please try in tatkal !")

rajdhani = Train("rajdhani","90","300")
rajdhani.getstatus()
rajdhani.numberofseats()
rajdhani.bookticket()