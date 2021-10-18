# Jack and Will's Program
import turtle

maze = turtle.Turtle()

maze.speed(0)
maze.pensize(3)

for index in range(30):
    maze.fd(20 + 20*index)
    maze.left(90)


wn = turtle.Screen()
wn.listen()
wn.mainloop()