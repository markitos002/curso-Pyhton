class Flight:
    def __init__(self, capacity): # constructor, capacity is the parameter
        self.capacity = capacity # attribute
        self.passengers = [] # list
    def add_passenger(self, name): # method to add a passenger
        if not self.open_seats(): # if there are no open seats return False
            return False
        self.passengers.append(name) # add the passenger to the list, append is a method of the list class
        return True
    def open_seats(self): # method to return the number of open seats
        return self.capacity - len(self.passengers) # capacity is an attribute of the class, len is a method of the list class

flight = Flight(capacity=5) # create an instance of the class, capacity is the parameter    
people = ["Harry", "Ron", "Hermione", "Ginny", "Jack", "Jen", "Frank"] # list of people
for person in people: # loop through the list
    #success = flight.add_passenger(person) # call the add_passenger method, person is the parameter
    if flight.add_passenger(person): # if the person is added to the flight
        print(f"Added {person} to flight.") # print a message
    else: # otherwise
        print(f"No available seats for {person}.") # print a message
# Output:

# Added Harry to flight.
# Added Ron to flight.
# Added Hermione to flight.
# No available seats for Ginny.
# Path: flight.py   
