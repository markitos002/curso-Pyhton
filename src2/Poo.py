import matplotlib.pyplot as plt



#create a class called Circle
class Circle(object):

    #Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color
    
    #Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    #Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

#Create an object RedCircle
RedCircle = Circle(10, 'red')
#print(dir(RedCircle))
RedCircle.radius = 1

#Print the object attribute radius
print(RedCircle.radius)
RedCircle.drawCircle()


print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)
RedCircle.drawCircle()

BlueCircle = Circle(radius=100)
BlueCircle.drawCircle()


class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 3, 'blue') 
SkinnyBlueRectangle.drawRectangle()  

class Car(object):
    
    # Constructor
    def __init__(self, make, model, year, color, miles=0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.miles = miles
        self.capacity = 0
        
    # Method
    def display(self):
        print(self.make, self.model, self.year, self.color)

    def seat_capacity(self,capacity):
        self.capacity = capacity


# Create a new object car
myCar = Car('Toyota', 'Corolla', 2015, 'green', 10000)
myCar.display()