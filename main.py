import turtle
import random
from turtle import Turtle, Screen
turtle_color = ["red", "green", "blue", "yellow", "orange", "purple"]
turtle_list = []
screen = Screen()

screen.setup(width=1280, height=720)
while True:
    user_guess = turtle.textinput("Faça a sua aposta",
                                  "Quem vai ganhar a corrida? (vermelho, verde, azul, amarelo, roxo)").lower()
    if (user_guess == "vermelho" or user_guess == "verde" or user_guess == "azul" or user_guess == "amarelo" or
            user_guess == "laranja" or user_guess == "roxo"):
        break

pos = -250
for tur in turtle_color:
    turtle_general = Turtle(shape="turtle")
    turtle_general.shapesize(3)
    turtle_general.color(tur)
    turtle_general.penup()
    turtle_general.goto(x=-520, y=pos)
    pos += 100
    turtle_list.append(turtle_general)
finish_line = False
while not finish_line:
    for turt in turtle_list:
        turt.forward(random.randint(1, 15))
        if turt.pos()[0] >= 640 - 58:
            winner = turt.color()[0]
            finish_line = True

if winner == "red":
    winner = "vermelho"
elif winner == "green":
    winner = "verde"
elif winner == "blue":
    winner = "azul"
elif winner == "yellow":
    winner = "amarelo"
elif winner == "orange":
    winner = "laranja"
else:
    winner = "roxo"

if user_guess == winner:
    print(f"Você ganhou! O venceder é o {winner}!")
else:
    print(f"Você perdeu. O venceder é o {winner}!")