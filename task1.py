import math
class point:
    """ Prints X and Y coordinates
        Adds two points
        """
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "X:Y-%.2d:%.2d" % (self.x, self.y)
    def __add__(self,other):
        if isinstance(other, point):
            return self.add_points(other)
        else:
            return self.add_points_tuple(other)
    def __radd__(self,other):
        return self.__add__(other)
    def add_points(self,other):
        return point(self.x+other.x,self.y+other.x)
    def add_points_tuple(self,other):
        return point(self.x+other[0],self.y+other[1])

def distance_between_points(p1,p2):
    return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)

def main():
    p1=point(10)
    p2=point(10,20)
    print("Distance between points is :",distance_between_points(p1,p2))
    print(p1)
    print(p2)
    print(p1+p2)
    print(p1+(20,30))
    print((20,30)+p2)


if __name__ == '__main__':
    main()
