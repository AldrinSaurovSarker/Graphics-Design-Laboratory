import cv2
import numpy as np


def putPixel(image, x, y, color=(0, 0, 0)):
    image[x][y] = color


def rect(image, start, end):
    x1, y1 = start
    x2, y2 = end

    drawLine(image, (x1, y1), (x1, y2))
    drawLine(image, (x1, y1), (x2, y1))
    drawLine(image, (x2, y2), (x1, y2))
    drawLine(image, (x2, y2), (x2, y1))


def DDA(image, start, end):
    x1, y1 = start
    x2, y2 = end

    if x1 == x2:
        m = 1
    else:
        m = (y2 - y1) / (x2 - x1)

    if m < 1:
        y = y1
        for i in range(min(x1, x2), max(x1, x2)):
            putPixel(image, i, int(y + m), color=(0, 0, 255))
            y = y + m
    if m > 1:
        x = x1
        for i in range(min(y1, y2), max(y1, y2)):
            putPixel(image, int(x + (1 / m)), i, color=(0, 0, 255))
            x = x + (1 / m)
    if m == 1:
        for i, j in zip(range(min(x1, x2), max(x1, x2)), range(min(y1, y2), max(y1, y2))):
            putPixel(image, i, j, color=(0, 0, 255))


def drawLine(image, start, end):
    x1, y1 = start
    x2, y2 = end

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)):
            putPixel(image, x1, i, color=(255, 0, 0))
    else:
        m = (y2 - y1) / (x2 - x1)
        c = (x2 * y1 - x1 * y2) / (x2 - x1)

        for i in range(min(x1, x2), max(x1, x2)):
            putPixel(image, i, int(m * i + c), color=(255, 0, 0))


img1 = np.ones((512, 512, 3))
img2 = np.ones((512, 512, 3))
img3 = np.ones((512, 512, 3))

print('Enter first point : ')
x1, y1 = map(int, input().split())
print('Enter second point : ')
x2, y2 = map(int, input().split())

DDA(img1, (x1, y1), (x2, y2))
drawLine(img2, (x1, y1), (x2, y2))
DDA(img3, (x1, y1), (x2, y2))
drawLine(img3, (x1, y1), (x2, y2))

# rect(img3, (x1, y1), (x2, y2))

cv2.imshow('DDA', img1)
cv2.imshow('y=mx+c', img2)
cv2.imshow('Overlapped', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
