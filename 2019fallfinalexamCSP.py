#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#
#Date
#


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl
import random
thick =1

#create turtle
drawer = trtl.Turtle()



#movement functions
# this code makes the turtle go forwards
def up():
    drawer.forward(10)



# this code makes the turtle go backwards
def down():
    drawer.backward(10)



# this code makes the turtle turn left
def left():    
    drawer.left(90)
    drawer.forward(50)



# this code makes the turtle turn right
def right():    
    drawer.right(90)
    drawer.forward(50)


# this code makes the pensize bigger
def bigger_pen():
   drawer.pensize(thick + 2)
       


# this code makes the pensize smaller
def smaller_pen():
    drawer.pensize(thick +- 1)  
   



# this code picks the pen up and down with "u"
def penup_down():    
    if drawer.isdown():
        drawer.penup()
    else:
        drawer.pendown()

# this code clears the screen with "space"
def clear():
    drawer.clear()

# this code makes the pensize color change to blue with "c"
def color_swap():
    drawer.pencolor("blue")

#color/drawing functions



#create screen
wn = trtl.Screen()
#bind to keypresses
wn.onkeypress(up,"Up")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(down,"Down")
wn.onkeypress(bigger_pen,"o")
wn.onkeypress(smaller_pen,"p")
wn.onkeypress(clear,"space")
wn.onkeypress(penup_down,"u")
wn.onkeypress(color_swap,"c")



#listen

wn.listen()

#mainloop
wn.mainloop()