import turtle

wndw = turtle.Screen()
wndw.title("Pong Game")
wndw.bgcolor("black")
wndw.setup(width = 800, height= 600)
wndw.tracer(0)

#marcador
score1 = 0
score2 = 0

#Barra 1
barra1= turtle.Turtle()
barra1.speed(0)
barra1.shape("square")
barra1.shapesize(stretch_wid=7, stretch_len=1)
barra1.color("white")
barra1.penup()
barra1.goto(-350,0)

#Barra2
barra2= turtle.Turtle()
barra2.speed(0)
barra2.shape("square")
barra2.shapesize(stretch_wid=7, stretch_len=1)
barra2.color("white")
barra2.penup()
barra2.goto(350,0)


#Pelota
pelota= turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)

pelota.dx= 0.05
pelota.dy= 0.05


#pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0 , 260)
pen.write("Jugador 1: 0  -  0 : Jugador 2", align= "center", font= ("Arial", 27, "normal"))


#funciones

def barra1_up():
    y= barra1.ycor()
    y += 20
    barra1.sety(y)

def barra2_up():
    y= barra2.ycor()
    y += 20
    barra2.sety(y)
    
def barra1_down():
    y= barra1.ycor()
    y -= 20
    barra1.sety(y)
    
def barra2_down():
    y= barra2.ycor()
    y -= 20
    barra2.sety(y)
    
#binding del teclado

wndw.listen()  #listen the keyboard input
wndw.onkeypress(barra1_up, "w")
wndw.onkeypress(barra1_down, "s")
wndw.onkeypress(barra2_up, "Up")
wndw.onkeypress(barra2_down, "Down")

#Main loop del juego
while True:
    wndw.update()
    
    #que se mueva la pelota
    pelota.setx(pelota.xcor ()+ pelota.dx)
    pelota.sety(pelota.ycor ()+ pelota.dy)
    
    #marcamos los bordes
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1
        
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1
        
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx = 0.05
        pelota.dy = 0.05
        pelota.dx *= -1
        score1 +=1
        pen.clear()
        pen.write(f"Jugador 1: {score1}  -  {score2} : Jugador 2", align= "center", font= ("Arial", 27, "normal"))
        
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx = 0.05
        pelota.dy = 0.05
        pelota.dx *= -1
        score2 += 1
        pen.clear()
        pen.write(f"Jugador 1: {score1}  -  {score2} : Jugador 2", align= "center", font= ("Arial", 27, "normal"))
    #rebotes con las barras
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < barra2.ycor() + 40 and pelota.ycor() > barra2.ycor() - 40):
        pelota.setx(340)
        pelota.dx *= -1
        
    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < barra1.ycor() + 40 and pelota.ycor() > barra1.ycor() - 40):
        pelota.setx(-340)
        pelota.dx *= -1
        
    if pelota.xcor() > 340 and pelota.xcor() < 350:
        pelota.dx *= 1.5
        pelota.dy *= 1.5
    if pelota.xcor() < -340 and pelota.xcor() > -350:
        pelota.dx *= 1.5
        pelota.dy *= 1.5