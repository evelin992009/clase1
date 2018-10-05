from graphics import *

ventana=GraphWin('hola mundo!!', 500,500)

a=1
circulo1=Circle(Point(40,40),40)
circulo1.setFill("green")
circulo1.draw(ventana)




for m in range ( 0,100000):
  if a==1:
      for i in range(0,42 ):
        time.sleep(.05)
        circulo1.move(10, 0)

      for i in range(0,42 ):
        time.sleep(.05)
        circulo1.move(0, 10)

      for i in range(0,42 ):
         time.sleep(.05)
         circulo1.move(-10, 0)

      for i in range(0,42 ):
        time.sleep(.05)
        circulo1.move(0, -10)





#time.sleep(2)

#circulo.move(200,200)
time.sleep(5)


