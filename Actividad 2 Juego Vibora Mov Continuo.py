# Actividad 2 - Juego Vibora.
# Autores: Leonardo Delgado Rios-A00827915, Saul Jimenez Torres-A01283849.
# Aplicacion que desarrolla el minijuego de la vibora 
# Fecha de ultima modificacion: 10/28/2020.
# Se importan las librerias que se utilizaran para el correcto desarrollo de
# la aplicación.
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Funcion color, devuelve un color al azar de los establecidos
def color():
    colors = ['green', 'blue', 'pink', 'yellow', 'gray']
    return colors[randrange(0,len(colors))]

# Funcion change, cambia las coordenadas de la serpiente, es decir, es el que
# dira en que direccion se movera la snake dependiendo de la instruccion dada.
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

# Funcion inside, verifica a traves de un valor booleano si la cabeza de la
# snake se encuentra dentro de los limites establecidos para su ejecucion.
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# Funcion control, verifica la posibilidad de movimiento de la comida dentro de
# la ventana, debido a la precondicion dada, se analizan 8 posibles movimientos
# que podria tener (derecha, izquierda, arriba, abajo, derecha-arriba,
# derecha-abajo, izquierda-arriba e izquierda-abajo). Anexa las combinaciones a
# una lista donde se utilizara dentro de los mov posibles un valor random para
# seleccionar el movimiento a realizar de la comida.
def control(food):
    #Establecer el valor de las variables a utilizar
    l1 = []
    ax = food.x
    ay = food.y
    b = -200
    f = 190
    for i in range(0,8):
        #Evalua si puede moverse a la derecha
        if((ax+10) in range(b,f) and ay in range(b,f) and len(l1)==0):
            l1.append([food.x+10,food.y])
        #Evalua si puede moverse a la izquierda
        elif((ax-10) in range(b,f) and ay in range(b,f) and len(l1)<=1):
            l1.append([food.x-10,food.y])
        #Evalua si puede moverse arriba
        elif(ax in range(b,f) and (ay+10) in range(b,f) and len(l1)<=2):
            l1.append([food.x,food.y+10])
        #Evalua si puede moverse abajo
        elif(ax in range(b,f) and (ay-10) in range(b,f) and len(l1)<=3):
            l1.append([food.x,food.y-10])
        #Evalua si puede moverse a la derecha y arriba
        elif((ax+10) in range(b,f) and (ay+10) in range(b,f) and len(l1)<=4):
            l1.append([food.x+10,food.y+10])
        #Evalua si puede moverse a la derecha y abajo
        elif((ax+10) in range(b,f) and (ay-10) in range(b,f) and len(l1)<=5):
            l1.append([food.x+10,food.y-10])
        #Evalua si puede moverse a la izquierda y arriba
        elif((ax-10) in range(b,f) and (ay+10) in range(b,f) and len(l1)<=6):
            l1.append([food.x-10,food.y+10])
        #Evalua si puede moverse a la izquierda y abajo
        elif((ax-10) in range(b,f) and (ay-10) in range(b,f) and len(l1)<=7):
            l1.append([food.x-10,food.y-10])
    return l1

# Funcion move, menciona los posibles escenarios de la snake, en caso de que
# no haya comido/haya comido/se haya comido a si misma, respectivamente cambia
# su direccion, aumenta su tamaño o termina el programa.
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    ltmp = control(food)
    aux = ltmp[randrange(0,len(ltmp))]
    food.x = aux[0]
    food.y = aux[1]
    
    if head == food:
        print('Snake:', len(snake))
        print(food)
    else:
        snake.pop(0)

    clear()
    
    for body in snake:
        square(body.x, body.y, 9, randsnake)

    square(food.x, food.y, 9, randfood)
    update()
    ontimer(move, 100)

# Se definen los valores default, como el color de la snake y de la comida que
# se utilizara por cada ejecucion del programa, ademas del tamaño de la ventana
# y las instrucciones para cambiar la direccion de la snake.
randfood = color()
randsnake = color()
while randfood == randsnake:
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