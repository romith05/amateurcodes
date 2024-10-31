import tkinter as tk
from turtle import *
from random import randrange
from freegames import square, vector

root = tk.Tk()
text1 = tk.Text(root, height=50, width=40)
photo = tk.PhotoImage(file='pic/snake.png')
text1.insert(tk.END, '\n')
text1.image_create(tk.END, image=photo)
text1.insert(tk.END, '\n')
text1.pack(side=tk.LEFT)
text2 = tk.Text(root, height=300, width=300)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042', font=('Tempus Sans ITC', 12, 'bold'))
text2.insert(tk.END, '\n         Snake game\n', 'big')
quote = """
The player uses the arrow keys to move a 
"snake" around the board. 
As the snake finds food, it eats the food, and thereby 
grows larger.
The game ends when the snake either moves off the 
screen or moves into itself.
Each time the snake eats its food the score increases 
by hundred.
"""
root.title("place() method")
root.geometry("750x350")
button3 = tk.Button(root, text="start", command=root.destroy)
button3.place(x=500, y=290)

text2.insert(tk.END, quote, 'color')
text2.pack(side=tk.LEFT)
root.mainloop()


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    # Change snake direction.
    aim.x = x
    aim.y = y


def inside(h):
    # Return True if head of the snake is inside boundaries.
    return -400 < h.x < 400 and -400 < h.y < 400


def move():
    # Moves the snake forward one segment.
    h = snake[-1].copy()
    # h = Head of the snake
    h.move(aim)

    if not inside(h) or h in snake:
        square(h.x, h.y, 9, 'red')
        update()
        return

    snake.append(h)

    if h == food:
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
score = (len(snake)-1)*100
print("score:", score)