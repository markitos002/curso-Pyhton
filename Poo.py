import matplotlib.pyplotdir as plt


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