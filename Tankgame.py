import turtle as tank



screen_h = 800
screen_w = 1200

#setup for tanks
wn = tank.Screen()
wn.setup(width=screen_w, height=screen_h)
wn.bgpic("battlespot.png")

tankimage = "tank.gif"
tankimage2 = "tank2.gif"
#tankimage2 = ""
#bulletimage = "bullet.png"

tank1 = tank.Turtle()
tank2 = tank.Turtle()
wn.addshape(tankimage)


#tank2 = tank.Turtle(shape=tankimage2)

def draw_tanks(drawtank):
    drawtank.shape(tankimage)
    wn.update()
#w
def forward_tank():
    tank1.setheading(90)
    tank1.forward(100)
#s
def backwards_tank():
    tank1.setheading(-270)
    tank1.backward(100)
#d
def right_tank():
    tank1.setheading(0)
    tank1.forward(100)
#a
def left_tank():
    tank1.setheading(180)     
    tank1.forward(100)  

#controls for the tank
draw_tanks(tank1)
wn.onkeypress(forward_tank, "w")
wn.onkeypress(backwards_tank, "s")
wn.onkeypress(right_tank, "d")
wn.onkeypress(left_tank, "a")
wn.listen()
wn.mainloop()



def draw_tanks(drawtank):
    drawtank.shape(tankimage2)
    wn.update()
#w
def forward_tank():
    tank2.setheading(90)
    tank2.forward(100)
#s
def backwards_tank():
    tank2.setheading(-270)
    tank2.backward(100)
#d
def right_tank():
    tank2.setheading(0)
    tank2.forward(100)
#a
def left_tank():
    tank2.setheading(180)     
    tank2.forward(100)  

#controls for the tank
draw_tanks(tank1)
wn.onkeypress(forward_tank2, "Up")
wn.onkeypress(backwards_tank, "Down")
wn.onkeypress(right_tank, "Right")
wn.onkeypress(left_tank, "Left")
wn.listen()
wn.mainloop()
