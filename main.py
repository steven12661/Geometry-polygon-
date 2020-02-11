import turtle

def dibujar_figura(figura, color):
  turtle.color(color)
  if figura == "cuadro":
    for i in range(0,4):
      #fd para que avance
      turtle.fd(50)
      #angulo para que gire (90*4=360)
      turtle.lt(90)
    turtle.fd(75)

  if figura == "triangulo":
    for i in range(0,3):
      turtle.fd(70)
      turtle.lt(120)
    turtle.fd(75)
  
  if figura == "pentagono":
    for i in range (0,5):
      turtle.fd(50)
      turtle.lt(72)
    turtle.fd(75)
  
  if figura == "hexagono":
    for i in range (0,6):
      turtle.fd(50)
      turtle.lt(60)
    turtle.fd(75)


turtle.goto(-250,0)
#ejecutar funcion enviandole que figura y que color en ingles
dibujar_figura("cuadro", "red")
dibujar_figura("triangulo", "Hot Pink")
dibujar_figura("pentagono", "Deep Sky Blue	")
dibujar_figura("hexagono", "Blue Violet	")

delay = raw_input("Press enter to finish.") 