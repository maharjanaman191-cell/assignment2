import turtle
import math


def koch_inward(t, length, depth):
    if depth == 0:
        t.forward(length)
        return

    length /= 3
    koch_inward(t, length, depth - 1)
    t.left(60)
    koch_inward(t, length, depth - 1)
    t.right(120)
    koch_inward(t, length, depth - 1)
    t.left(60)
    koch_inward(t, length, depth - 1)


def draw_polygon(sides, length, depth):
    screen = turtle.Screen()
    screen.title("Asign 2 Quest 3")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Move turtle roughly to center
    radius = length / (2 * math.sin(math.pi / sides))
    t.penup()
    t.goto(-length / 2, -radius / 2)
    t.pendown()

    angle = 360 / sides
    for _ in range(sides):
        koch_inward(t, length, depth)
        t.left(angle)

    screen.update()
    turtle.done()

def main():
    sides = int(input("Number of sides: "))
    length = float(input("Side length: "))
    depth = int(input("Recursion depth: "))

    if sides < 3 or length <= 0 or depth < 0:
        print("Invalid input values.")
        return

    draw_polygon(sides, length, depth)


main()
