import turtle               
window = turtle.Screen()    
window.bgcolor("white")
window.title("Forca")

tartaruga   = turtle.Turtle()  
tartaruga.speed(0)  
tartaruga.penup()   
tartaruga.setpos(-300,-150)
tartaruga.pendown()
tartaruga.color("black")

dist = 400
angulo = -90

for i in range(1):
    tartaruga.left(angulo)  
    tartaruga.backward(dist)
dist3 = 150
angulo3 = -90

for i in range(1):
    tartaruga.left(angulo3)  
    tartaruga.backward(dist3) 
dist2 = 50
angulo2 = -90
for i in range(1):
    tartaruga.left(angulo2)  
    tartaruga.backward(dist2)    

window.exitonclick()
