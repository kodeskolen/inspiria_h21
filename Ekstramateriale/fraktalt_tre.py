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
