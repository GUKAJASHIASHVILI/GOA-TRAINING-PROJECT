from turtle import*

#drawing phone


#drawing rectangle

speed(5)
width(5)
forward(200)
left(90)

forward(350)
left(90)

forward(200)
left(90)

forward(350)
left(90)
#end of drawing rectangle

#drawing button
begin_fill()
forward(80)
left(90)

forward(15)
right(90)

forward(40)
right(90)

forward(15)
left(90)
end_fill()
#end of drawing button

forward(80)
left(90)

forward(23)
left(90)

forward(200)
right(90)

forward(304)
right(90)

forward(200)

#drawing camera
penup()
goto(80,350)
pendown()

begin_fill()
forward(40)
right(90)

forward(15)
right(90)

forward(40)
right(90)

forward(15)
end_fill()
right(90)
#end of drawing camera

#drawing buttons on the right

#drawing volume buttons
forward(120)
right(90)

forward(80)
left(90)

forward(2)
right(90)

forward(35)
right(90)

forward(2)
left(90)
#end of drawing volume buttons 

#drawing power button
forward(20)
left(90)

forward(2)
right(90)

forward(20)
right(90)






exitonclick()