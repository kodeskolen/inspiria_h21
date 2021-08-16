import turtle

def tegn_tre(skilpadde, lengde, vinkel, niva):
  if niva < 1:
    return 

  skilpadde.forward(lengde)
  skilpadde.right(vinkel*0.5)

  tegn_tre(skilpadde, lengde*0.8, vinkel, niva-1)
  
  skilpadde.left(vinkel)
  
  tegn_tre(skilpadde, lengde*0.8, vinkel, niva-1)
  skilpadde.right(vinkel*0.5)
  skilpadde.backward(lengde)
  
  
penn = turtle.Turtle()
penn.left(90)
penn.penup()
penn.goto(0, -200)
penn.pendown()
tegn_tre(penn, 100, 60, 5)


turtle.done()
turtle.bye()


#%%
import random

def tegn_tre(skilpadde, lengde, vinkel, niva):
  if niva < 1:
    return 

  ny_vinkel = vinkel*random.uniform(0.5, 1.5)
  ny_lengde = lengde*random.uniform(0.5, 0.95)

  skilpadde.forward(lengde)
  skilpadde.right(vinkel*0.5)

  tegn_tre(skilpadde, ny_lengde, ny_vinkel, niva-1)
  
  skilpadde.left(vinkel)
  
  tegn_tre(skilpadde, ny_lengde, ny_vinkel, niva-1)
  skilpadde.right(vinkel*0.5)
  skilpadde.backward(lengde)
  
  
penn = turtle.Turtle()
penn.left(90)
penn.penup()
penn.goto(0, -200)
penn.pendown()
tegn_tre(penn, 100, 60, 6)


turtle.done()
turtle.bye()

#%%