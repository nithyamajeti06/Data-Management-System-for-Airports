""" Thurs54"""
def passenger_data(filename):
    """ This function returns a 2D list that contains 
    all the passengers information in each plane that was taken from
    passenger_data_v3 file"""
    passengerFile = open(filename + ".txt", "r")
    totalPassengerList = []
   
    for line in passengerFile:
        passengerList = line.strip("\n").split(",")
        totalPassengerList.append(passengerList)
       
    passengerFile.close()
    return totalPassengerList
"""Thurs54"""
def fleet_data(filename):
    """ This function returns a 2D list that includes the plane modles
    and their information that was taken from fleet_data file"""
    fleetFile = open(filename + ".txt", "r")
    totalFleetList = []
   
    for line in fleetFile:
        fleetList = line.strip("\n").split(",")#splitting all the lines in the file into a list
        totalFleetList.append(fleetList)
       
    fleetFile.close()
    return totalFleetList



# Maia Antolic 400598105
def daily_data(passenger_data,fleet_data):
    """this function takes in passenger and plane data lists to compare the gates 
    and see which plane a passenger is on. It then checks if passengers are economy
    or business class and totals the number of passengers in each class for each plane"""
    passengerlist = passenger_data
    fleetlist = fleet_data
    daily_data_list = []
   # extracting passenger and plane gates to compare them and creating lists for each plane
    for plane in fleetlist:
        planegate= plane[4]
       
        business_seats = 0
        economy_seats = 0
   
       
        for passenger in passengerlist:
            passengergate = passenger[3]
           # checking if passenger is in E or B and increasing that number for respective planes
            if passengergate == planegate:
                if passenger[4] == "E":
                    economy_seats += 1
                else:
                    business_seats += 1
           
               
        daily_data_list.append([planegate, business_seats, economy_seats])
    return daily_data_list



"""
Logan Prince -- 400584088
"""

def oversold(passenger_data, fleet_data, daily_data):
    """ This function returns the oversold seats for economy and buisness seats
    for each plane modle"""
   
    oversold_economy = []
    oversold_business = []
    for row in fleet_data:
        plane_model = row[0]
        availible_business = int(row[1]) #Finding the number of buisness seats on a plane
        availible_economy = int(row[2]) #Finding the number of economy seats on a plane
        requested_business = 0
        requested_economy = 0
        for gate in daily_data:
            if gate[0] == row[4]:#Checking if the gate of the plane and the gate for the passenger are the same
                requested_business += int(gate[1])
                requested_economy += int(gate[2])
                if requested_business > availible_business:
                    oversold_business.append([plane_model, requested_business - availible_business])#finding the number of extra business seats and appending it with the plane modle
                else:
                    oversold_business.append([plane_model, 0])
                if requested_economy > availible_economy:
                    oversold_economy.append([plane_model, requested_economy - availible_economy])#finding the number of extra economy seats and appending it with the plane modle
                else:# No oversold seats
                    oversold_economy.append([plane_model, 0])
    return oversold_economy,oversold_business


def overweight(passengerData,fleetData):
    passengers = []
    planes = []  
   
    for plane in fleetData:
        """ This function returns the passengers that have
        more than the maximum weight allowed per passenger
        Name: Lisa
        mcID: Zhengl53"""
        planeName = plane[0] #setting a variable to the plane modle index
        planeInfo = [planeName,0]
       
        planeGate = plane[4] #Finding the gate index
        weightLimit = float(plane[7]) # Finding the max weight in each plane
       
        for passenger in passengerData:
            passengerInfo = [None,None,None,None]
           
            weight = float(passenger[6])
            gate = passenger[3]
            if gate == planeGate and weight > weightLimit: #Comparing the gate number to the passenger's gate and checking if they have more than the max weight
                planeInfo[1] += 1
                passengerInfo[0] = passenger[0]
                passengerInfo[1] = passenger[1]
                passengerInfo[2] = gate
                passengerInfo[3] = round(weight - weightLimit,2)# Calculating the excess weight
                passengers.append(passengerInfo)
        planes.append(planeInfo)
    return planes,passengers

def time_delay(passenger_data,fleet_data):
    """ Reports the passengers that have layovers and lates
    Mustafa Alhamadni 400577345"""
    time_delay = []
    for gate in fleet_data:
        count = 0 # setting the count to zero in every loop
        gate_num = gate[4] #gate index in the fleet data file
        for passenger in passenger_data:
            if passenger[3] == gate_num: # Checking if the gate of the passenger matches the gate of the plane
                if passenger[2] == "Late" and passenger[7] == "Layover": #Checks if the passenger is late and have a layover
                    count += 1
        time_delay.append([gate[0],count])
    return time_delay

def layover(passengerData, fleetData):
    """The layover function takes in the output from the passengerData and fleetData as
    parameters and returns two 2-D lists, one with the plane name and total layover
    passengers and the other is a list of passengers with layover status, Nithya
    Majeti 400569912"""
    passengerList = passengerData
    fleetList = fleetData
    status = "Layover"
   
    # Creating an empty list to store total layover passengers per plane
    layoverCountList = []
    # Iterating through each list in the 2-D list
    for plane in fleetList:
        # Storing specific elements from the list as variables
        planeName = plane[0]
        planeGate = plane[4]
       
        # Creating a counter variable to store the total layover passengers
        layoverPassengerCount = 0
        # Looping through each passenger in the 2-D list
        for passenger in passengerList:
            # Checking if the plane's gate exists in the passenger list and if they are in layover
            if planeGate in passenger and status in passenger:
                layoverPassengerCount += 1
           
        # Appending the plane name and its total layover passengers in the empty list
        layoverCountList.append([planeName, layoverPassengerCount])
       
        layoverPassengerList = []
        # Looping through each passenger in the 2-D list
        for passenger in passengerList:
        # Checking if the passenger is in layover
            if status in passenger:
            # Storing specific elements from the passenger list as variables
                firstName = passenger[0]
                lastName = passenger[1]
                planeGate = passenger[3]
            # Appending the passenger's first and last name and their plane gate in the list
                layoverPassengerList.append([firstName, lastName, planeGate])
            
    # Returning both the lists
    return layoverCountList, layoverPassengerList


def draw(flightData):
    """The draw function takes in flightData or a 2-D list as a parameter and displays
    the information using turtle graphics and doesn't return anything"""
    
    # Importing the turtle module
    import turtle 

    # Initalizing screen properties
    turtle.setup(1500, 500)
    screen = turtle.Screen()
    screen.title("Flight Data")
    t = turtle.Turtle()
    t.speed(0)
    screen.bgcolor("black")
    t.pencolor("white")
    
    # Creating a list of colours to represent each plane 
    colorList = ["orange", "pink", "red", "lightblue", "lightgreen", "violet", "salmon"]


    # Looping the process until the length of the flightData list    
    for i in range (len(flightData)):

        # Choosing a color from the colorList 
        t.fillcolor(colorList[i])
        
        # Making the title box
        t.up()
        t.goto(-700 + 200*i, 100)
        t.down()
        t.begin_fill()
        t.forward(150)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(150)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.end_fill()
    
        # Adding the title to the title box
        t.up()
        t.goto(-680 + 200*i, 75)
        t.down()
        t.write(flightData[0 + i][0], font = ("Times New Roman", 11, "normal"))
        t.up()
    
        # Making the box for flight information
        t.goto(-700 + 200*i, 100)
        t.down()
        t.forward(150)
        t.right(90)
        t.forward(200)
        t.right(90)
        t.forward(150)
        t.right(90)
        t.forward(200)
        t.right(90)
        t.up()
    
        # Adding flight information
        num = 0
        for j in range(5):
            t.goto(-695 + 200*i, 45 + -35*j)
            t.down()
            t.write(flightData[i][1 + num], font = ("Times New Roman", 9, "normal"))
            t.up()
            # Increasing number by 1 every iteration so that when extracting information it goes to the next index in the list
            num += 1
    # Trying to be creative and creating a shape
    t.penup()
    t.goto(0,550)
    t.pendown()
    a = 0
    b = 0
    while True:
        t.forward(a)
        t.right(b)
        a +=2
        b+=1
        if b == 200:
            break
           
    # Hiding turtle
    t.hideturtle()
        
    # Making a clean exit
    screen.exitonclick()
    turtle.done()
    
"""Thurs54"""
def graphical_Thurs54(oversold_economy, oversold_business, overweight_planeinfo, layover_plane, time_delay):
    """The graphical team ID takes in list outputs from the oversold, overweight, layover and timedelay
    functions and output each flight's metrics like overweight bags or total layover passengers using
    turtle graphics and the function doesn't return anything"""
    
    # Creating an empty list to store all the flight's data
    flightData = []
    
    
    num = 0
    
    # Looping the process until the length of the oversold_economy list
    for flight in range(len(oversold_economy)):
        # Creating an empty list to store each flight's information
        flightInformation = []
        # Extracting information from it's approriate list 
        flightName = oversold_economy[0 + num][0]
        businessSeats = oversold_business[0 + num][1]
        economySeats = oversold_economy[0 + num][1]
        overweightBags = overweight_planeinfo[0 + num][1]
        layoverPassengers = layover_plane[0 + num][1]
        lateLayoverPassengers = time_delay[0 + num][1]
        
        # Appending all the information to the flightInformation list
        flightInformation.append(flightName)
        flightInformation.append(f"Oversold Business Seats: {businessSeats}")
        flightInformation.append(f"Oversold Economy Seats: {economySeats}")
        flightInformation.append(f"Overweight Bags: {overweightBags}")
        flightInformation.append(f"Layover Passengers: {layoverPassengers}")
        flightInformation.append(f"Late Layover Passengers: {lateLayoverPassengers}")
        
        # Appending the flightInformation list to flightData list
        flightData.append(flightInformation)
        
        # Increasing number by 1 every iteration so that when extracting information it goes to the next index in the list
        num += 1
        
    # Calling the draw function to display the flight data using turtle graphics
    print(draw(flightData))
    
# Main Function 

# Calling the passenger_data, fleet_data, daily_data, oversold, layover and timedelay functions and storing the outputs
passengerData = passenger_data("passenger_data_v3")
fleetData = fleet_data("fleet_data")
daily_data = daily_data(passengerData,fleetData)
oversold_economy, oversold_business = oversold(passengerData, fleetData, daily_data)
overweight_planeinfo, overweight_passengerinfo = overweight(passengerData,fleetData)
layover_plane, layover_pasenger = layover(passengerData,fleetData)
time_delay = time_delay(passengerData, fleetData)

# Calling the graphical_teamID function and printing it
print(graphical_Thurs54(oversold_economy, oversold_business, overweight_planeinfo, layover_plane, time_delay))