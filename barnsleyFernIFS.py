import turtle
import random
import numpy as np
import Hutchisons as h

pen = turtle.Turtle()
pen.speed(1)
pen.color("pink")
pen.penup()
turtle.tracer(False)


def collapse_to_leaf(currentFrac, points):
    for k in range(15000):
        x, y = points[k]
        r = random.random()
        pen.goto(x,y)
        # pen.goto(65 * x * 1.5, 37 * y * 1.5 - 252)
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
    zoom = 4
    points = []
    currentFrac = h.presets.get('Tree2')
    # points.append([50,0])
    # points.append([-50,0])
    # points.append([0,87])
    #
    # for (x, y) in points:
    #     pen.goto(65 * x * zoom, 37 * y * zoom - 252)
    #     pen.pendown()
    #     pen.dot(10)
    #     pen.penup()
    #h.shear(currentFrac, 1.1, 0, 1)

    #h.rotate(currentFrac, -0.1, 0, 1)
    #h.scale(currentFrac, 0.8, 0, 1)

    for n in range(30000):
        points.append([x, y])
        # print(("{} {}").format(x, y))
        pen.goto(65 * x * zoom-200, 37 * y * zoom - 100)  # scale the fern to fit nicely inside the window
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
    # print(points)
    # pen.update()
    # pen.color("orange")
    # collapse_to_leaf(currentFrac, points)

    #print(np.linalg.inv(np.identity(2) - currentFrac.affineList[0].contraction))
    #print(currentFrac.affineList[1].translate)

    # print out large orange dot for end behavior of single affine transformation
    for i in range(len(currentFrac.affineList)):
        c_a = i # current affine transformation in Hutchison
        x = np.matmul( np.linalg.inv(np.identity(2) - currentFrac.affineList[c_a].contraction), np.transpose(currentFrac.affineList[c_a].translate)).item(0)
        y = np.matmul( np.linalg.inv(np.identity(2) - currentFrac.affineList[c_a].contraction), np.transpose(currentFrac.affineList[c_a].translate)).item(1)
        pen.goto(65 * x * zoom-200, 37 * y * zoom - 100)  # scale the fern to fit nicely inside the window
        pen.color("orange")
        pen.dot(10)

if __name__ == '__main__':
    main()

turtle.done()
