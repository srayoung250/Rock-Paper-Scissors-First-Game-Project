import turtle
import time
import random

COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan", "magenta"]
WIDTH, HEIGHT = 800, 800

def get_number_of_turtles():
    racers = 0
    while True:
        racers = input("Please enter number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input. Please enter a number between 2-10.")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Invalid number of racers. Please enter a number between 2-10.")
            
def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
    

def create_turtles(colors):
    turtles = []
    spacingx = HEIGHT // (len(colors) + 1)
    for i, color in enumerate(colors):
        racers = turtle.Turtle()
        racers.color(color)
        racers.shape("turtle")
        racers.penup()
        racers.left(90)
        racers.setpos(-HEIGHT//2 + (i + 1) * spacingx, -WIDTH//2 + 20)
        racers.pendown()
        turtles.append(racers)
        
    return turtles

def init_turtles():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    
racers = get_number_of_turtles()
init_turtles()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is the {winner} turtle!")
time.sleep(5)
