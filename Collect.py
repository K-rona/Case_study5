import turtle
from math import sqrt


def square(x0, y0, angle, size):

    turtle.speed(100)
    turtle.seth(angle)

    x1 = x0 - size / 2
    y1 = y0 + size / 2
    turtle.goto(x1, y1)
    turtle.pd()

    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)

    turtle.pu()
    turtle.goto(x0, y0)

    if size >= 25:

        angle -= 5
        size -= 5
        square(x0, y0, angle, size)


def main1():

    turtle.pu()
    square(0, 0, 0, 100)
    turtle.done()


def color_branch(order, size):

    turtle.colormode(255)
    red = 79
    green = 48
    blue = 2
    turtle.color(red, green, blue)

    if order == 0:
        turtle.color(red * ((order + 1) % 255), green * 2 * ((order + 1) % 255), blue * (order + 1))
        turtle.lt(180)
        return

    x = size/(order + 1)

    for i in range(order):

        turtle.fd(x)
        turtle.lt(45)
        color_branch(order - i - 1, 0.5 * x * (order - i - 1))
        turtle.lt(90)
        color_branch(order - i - 1, 0.5 * x * (order - i - 1))
        turtle.rt(135)

    turtle.fd(x)
    turtle.lt(180)
    turtle.fd(size)


def main3():

    turtle.tracer(0)
    turtle.pu()
    turtle.goto(0, -100)
    turtle.lt(90)
    turtle.pd()

    color_branch(5, 2000)
    turtle.done()



def curve_Minkovskiy(order, size):

    turtle.speed(0)

    if order == 0:
        turtle.fd(size)

    else:

        curve_Minkovskiy(order - 1, size / order)
        turtle.lt(90)
        curve_Minkovskiy(order - 1, size / order)
        turtle.rt(90)
        curve_Minkovskiy(order - 1, size / order)
        turtle.rt(90)
        curve_Minkovskiy(order - 1, size / order)
        curve_Minkovskiy(order - 1, size / order)
        turtle.lt(90)
        curve_Minkovskiy(order - 1, size / order)
        turtle.lt(90)
        curve_Minkovskiy(order - 1, size / order)
        turtle.rt(90)
        curve_Minkovskiy(order - 1, size / order)


def main6():

    turtle.pu()
    turtle.goto(-200, 0)
    turtle.pd()

    n = int(input('Глубина рекурсии: '))
    a = int(input('Длина стороны: '))
    curve_Minkovskiy(n, a)
    turtle.done()


def ice_fractal2(order, size):

    turtle.speed(100)

    if order == 0:
        turtle.fd(size)

    else:
        ice_fractal2(order - 1, size/2)
        turtle.lt(120)
        ice_fractal2(order - 1, size/4)
        turtle.rt(180)
        ice_fractal2(order - 1, size / 4)
        turtle.lt(120)
        ice_fractal2(order - 1, size / 4)
        turtle.rt(180)
        ice_fractal2(order - 1, size / 4)
        turtle.lt(120)
        ice_fractal2(order - 1, size / 2)


def main8():

    turtle.pu()
    turtle.goto(-200, 0)
    turtle.pd()

    n = int(input('Глубина рекурсии: '))
    a = int(input('Длина стороны: '))
    ice_fractal2(n, a)

    turtle.done()


def vertushka(order, size):

    if order == 0:
        turtle.fd(size)

    else:

        vertushka(order - 1, size)
        turtle.lt(135)
        vertushka(order - 1, sqrt(size ** 2 + size ** 2))
        turtle.rt(135)
        vertushka(order - 1, size)
        turtle.rt(135)
        vertushka(order - 1, sqrt(size ** 2 + size ** 2))


def main10():

    turtle.tracer(0)
    turtle.seth(270)
    turtle.pu()
    turtle.goto(-200, 0)
    turtle.pd()

    n = int(input('Глубина рекурсии: '))
    a = int(input('Длина стороны: '))
    vertushka(n, a)

    turtle.done()


def main():

    print('Меню\n'
          '1 - Убегающий квадрат\n'
          '3 - Фрактал "Ветка"\n'
          '6 - Кривая Минковского\n'
          '8 - Ледяной фрактал 2\n'
          '10 - Фрактал "Вертушка"')

    number = int(input("Пожалуйста выберите число: "))

    if number == 1:
        main1()

    elif number == 3:
        main3()

    elif number == 6:
        main6()

    elif number == 8:
        main8()

    elif number == 10:
        main10()


if __name__ == '__main__':
    main()
