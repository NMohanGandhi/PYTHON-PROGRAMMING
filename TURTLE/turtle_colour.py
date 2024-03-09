import turtle
colours=['red','blue','green','yellow','violet','indigo','purple','black']
paper=turtle.Screen()
pen=turtle.Turtle()
i=0
while True:
    pen.forward(10)
    pen.right(90)
    k  =  i%8
    pen.color(colours[k])
    i+=1

