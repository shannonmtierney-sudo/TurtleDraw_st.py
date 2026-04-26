import turtle

screen = turtle.Screen()
screen.setup(width=450, height=450)

print("TurtleDraw_st.py")

# Todo: Ask user for the file name
filename = input("Enter the name of the text file to read: ")
if filename == "":
    filename = "turtle-draw-sample.txt"

turtledrawpart3 = turtle.Turtle()
turtledrawpart3.speed(10)
turtledrawpart3.penup()

total_distance = 0
prev_x, prev_y = 0, 0

print("Reading a text file line by line.")
turtleDrawTextfile = open(filename, 'r')

for line in turtleDrawTextfile:
    print(line, end='')
    parts = line.strip().split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        # Calculate distance here
        distance = ((x - prev_x)**2 + (y - prev_y)**2) ** 0.5
        total_distance += distance

        prev_x, prev_y = x, y

        turtledrawpart3.color(color)
        turtledrawpart3.goto(x,y)
        turtledrawpart3.pendown()

    if (len(parts) == 1): # Assumes that a single word on a line is "stop"
        turtledrawpart3.penup()

line = turtleDrawTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        # Calculate distance here
    if turtledrawpart3.isdown():
        distance = ((x - prev_x)**2 + (y - prev_y)**2) ** 0.5
        total_distance += distance
        prev_x, prev_y = x, y

        turtledrawpart3.color(color)
        turtledrawpart3.goto(x,y)
        turtledrawpart3.pendown()

    if (len(parts) == 1): # Assumes that a single word on a line is "stop"
        turtledrawpart3.penup()

    line = turtleDrawTextfile.readline()

turtleDrawTextfile.close()

# Todo: Print the total near the bottom
screen = turtle.Screen()
width = screen.window_width()
height = screen.window_height()
turtledrawpart3.penup()
turtledrawpart3.goto(200, -200) # Bottom right corner 

turtledrawpart3.write(
    f"Total distance: {total_distance:.2f}",
    align="right",
    font=("Arial", 16, "normal")
)

turtle.done()

# Todo: Wait for the user to press the enter key before closing.
input("Press Enter to exit...")
print('\nEnd')