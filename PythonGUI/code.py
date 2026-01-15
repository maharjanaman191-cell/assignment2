import turtle
import math


def koch_inward(t, length, depth):
    if depth == 0: ## If we have reached the last level, just draw a straight line
        t.forward(length)
        return

    #SPLITING THE LINE TO 3 PARTS
    length /= 3

    #DRAWING THE KOCH DESIGN
    koch_inward(t, length, depth - 1)
    t.left(60)
    koch_inward(t, length, depth - 1)
    t.right(120)
    koch_inward(t, length, depth - 1)
    t.left(60)
    koch_inward(t, length, depth - 1)


#DRAWING THE POLYGON THAT IS REQUESTED
def draw_polygon(sides, length, depth):
    screen = turtle.Screen() ## Create the window where the drawing will appear
    screen.title("Asign 2 Quest 3")
    screen.tracer(0)

    # Create the turtle and set its speed
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Move turtle roughly to center
    radius = length / (2 * math.sin(math.pi / sides)) # Calculate a value to help place the shape near the center
    t.penup()
    t.goto(-length / 2, -radius / 2)
    t.pendown()

    angle = 360 / sides # Calculate how much the turtle should turn after each side
    for _ in range(sides):
        koch_inward(t, length, depth)
        t.left(angle)

    
    # Showing the final drawing on the screen
    screen.update()
    turtle.done()


# Asking the user for input values
def main():
    sides = int(input("Number of sides: "))
    length = float(input("Side length: "))
    depth = int(input("Recursion depth: "))

    
    # Checking if the input values make sense
    if sides < 3 or length <= 0 or depth < 0:
        print("Invalid input values.")
        return

    draw_polygon(sides, length, depth)


main()
