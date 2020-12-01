#Base class
class Shape:
    def draw_shape(self,shape):
        print("Drawing a shape of:",shape)
    
    def color_shape(self,color):
        print("Coloring the shape:",color)
        

#Derived class-1 Triangle
class Triangle(Shape):
    def no_of_sides(self,side):
        print("I am a triangle")
        print("And the no of sides i have is:",side)
        
class Circle(Shape):
    def diameter_size(self,diameter):
        print("I am circle and my diameter is:",diameter)
        
class Rectangle(Shape):
    def area_of_rect(self):
        print("I am a rectangle")
        
#instatntiating of the object
r=Rectangle()
r.draw_shape("Rectangle")
r.color_shape("Red")
r.area_of_rect()


t=Triangle()
t.draw_shape("Triangle")
t.color_shape("Green")
t.no_of_sides(3)

c=Circle()
c.draw_shape("Circle")
c.color_shape("Blue")
c.diameter_size(10)


        