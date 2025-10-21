# ###############################################
# ### SETUP ###
import turtle
# ###############################################
turtle.Screen().bgcolor("PaleTurquoise")

t = turtle.Turtle()
t.penup()
t.goto(-80,-100) #This is mostly in the center
t.pendown()
t.speed(10)
t.color("Purple") #I changed this to purple because the blue did not look good
for i in range (100):
    t.forward (100)
    t.left (53)
    t.forward (20)
    t.left (53)

v = turtle.Turtle()
v.penup()
v.goto(-50,-20)
v.pendown()
v.speed(10)
v.color("Indigo")
for i in range (50): #This creates a cool crazy star
    v.forward (300)
    v.left (190)
    v.forward (300)
    v.left (300)
    
w = turtle.Turtle()
w.penup()
w.goto (-300,80)
w.pendown()
w.speed(10)
w.color("Purple") #I put this because it is my favorite color
for i in range (50):
    w.forward (500)
    w.right (90) 
    w.forward (300)
    w.right (100)
# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
