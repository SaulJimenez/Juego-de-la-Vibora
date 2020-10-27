# Actividad 2 - Juego Vibora.
# Autores: Leonardo Delgado Rios - A00827915, Saul Jimenez
# Torres - A01283849.
# Aplicacion que desarrolla el minijuego de la vibora 
# Fecha de ultima modificacion: 10/27/2020.

# Se importan las librerias que se utilizaran para el correcto
# desarrollo de la aplicación.
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Funcion color, devuelve un color al azar de los establecidos
def color():
    colors = ['green', 'blue', 'pink', 'yellow', 'gray']
    i = randrange(0,5)
    return colors[i]

# Funcion change, cambia las coordenadas de la serpiente, es
# decir, es el que dira en que direccion se movera la snake
# dependiendo de la instruccion recibida.
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

# Funcion inside, verifica a traves de un valor booleano si
# la cabeza de la snake se encuentra dentro de los limites
# establecidos para su ejecucion.
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# Funcion move, menciona los posibles escenarios de la
# snake, en caso de que no haya comido, haya comido o
# se haya comido asi misma, respectivamente cambia su
# direccion, aumenta su tamaño o termina el programa.
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    
    for body in snake:
        square(body.x, body.y, 9, randsnake)

    square(food.x, food.y, 9, randfood)
    update()
    ontimer(move, 100)

# Se definen los valores default, como el color de la snake y de
# la comida que se utilizara por cada ejecucion del programa,
# ademas del tamaño de la ventana y las instrucciones para
# cambiar la direccion de la snake.
randfood = color()
randsnake = color()
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()