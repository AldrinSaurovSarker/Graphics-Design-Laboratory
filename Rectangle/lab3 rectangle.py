import cv2
import numpy as np


def drawLine(image, start, end):
    x1, y1 = start
    x2, y2 = end

    try:
        m = (y2 - y1) / (x2 - x1)
        c = (x2 * y1 - x1 * y2) / (x2 - x1)
    except ZeroDivisionError:
        m, c = 0, 0

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)):
            image[x1][i] = 0
    else:
        for i in range(min(x1, x2), max(x1, x2)):
            image[i][int(m * i + c)] = 0


def drawRectangle(image, start, end):
    x1, y1 = start
    x2, y2 = end

    drawLine(image, (x1, y1), (x1, y2))
    drawLine(image, (x1, y1), (x2, y1))
    drawLine(image, (x2, y2), (x1, y2))
    drawLine(image, (x2, y2), (x2, y1))


img = np.ones((512, 512, 3))

print('Enter first point : ')
x1, y1 = map(int, input().split())
print('Enter second point : ')
x2, y2 = map(int, input().split())

drawRectangle(img, (x1, y1), (x2, y2))

cv2.imshow('Rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
