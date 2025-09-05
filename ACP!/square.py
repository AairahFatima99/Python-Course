import turtle

# Create a screen object
wn = turtle.Screen()
wn.bgcolor("lightgreen") # Set background color (optional)
wn.title("Drawing a Square") # Set window title (optional)

# Create a turtle object
pen = turtle.Turtle()
pen.color("blue") # Set pen color (optional)
pen.pensize(3) # Set pen size (optional)

# Draw the square
side_length = 150 # Define the length of each side

for _ in range(4): # Loop four times for the four sides
    pen.forward(side_length) # Move the turtle forward
    pen.right(90) # Turn the turtle 90 degrees to the right

# Keep the window open until clicked
wn.exitonclick()