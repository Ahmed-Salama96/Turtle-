import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)

	for i in range(1,40):
		brad.right(100)
		brad.forward(100)
		brad.right(90)
		brad.forward(100)
		brad.right(90)
		brad.forward(100)
		brad.right(90)
		brad.forward(100)
	window.exitonclick()
draw_square()
