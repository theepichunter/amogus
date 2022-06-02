import turtle
import random
import numpy as np
import Hutchisons as h

pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
turtle.tracer(False)


def collapse_to_leaf(currentFrac, points):
    for k in range(15000):
        x, y = points[k]
        r = random.random()
        pen.goto(65 * x * 1.5, 37 * y * 1.5 - 252)
        pen.pendown()
        pen.dot(1)
        pen.penup()
        l = 1
        a, b = points[k]
        x = (np.matmul(currentFrac.affineList[l - 1].contraction, [a, b]) + currentFrac.affineList[
                    l - 1].translate).item(0)
        y = (np.matmul(currentFrac.affineList[l - 1].contraction, [a, b]) + currentFrac.affineList[
                    l - 1].translate).item(1)


def main():
    x, y = 0, 0
    zoom = 1.5
    points = []
    currentFrac = h.presets.get('Barnsley')
    #h.shear(currentFrac, 0.9, 0, 1)

    #h.rotate(currentFrac, -0.1)
    #h.scale(currentFrac, 10)

    for n in range(15000):
        points.append([x, y])
        # print(("{} {}").format(x, y))
        pen.goto(65 * x * zoom, 37 * y * zoom - 252)  # scale the fern to fit nicely inside the window
        pen.pendown()
        pen.dot(1)
        pen.penup()
        r = random.random()

        for k in range(len(currentFrac.probVec) + 1):

            if r < currentFrac.getProbAcc()[k]:
                a, b = x, y
                x = (np.matmul(currentFrac.affineList[k - 1].contraction, [a, b]) + currentFrac.affineList[
                    k - 1].translate).item(0)
                y = (np.matmul(currentFrac.affineList[k - 1].contraction, [a, b]) + currentFrac.affineList[
                    k - 1].translate).item(1)
                break

    # pen.update()
    pen.color("orange")
    collapse_to_leaf(currentFrac, points)


if __name__ == '__main__':
    main()

turtle.done()
