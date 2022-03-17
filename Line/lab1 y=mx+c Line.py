import cv2
import numpy as np


def rect(image, start, end):
    x1, y1 = start
    x2, y2 = end

    line(image, (x1, y1), (x1, y2))
    line(image, (x1, y1), (x2, y1))
    line(image, (x2, y2), (x1, y2))
    line(image, (x2, y2), (x2, y1))


def line(image, start, end):
    x1, y1 = start
    x2, y2 = end

    if x1 == x2:
        lower, upper = min(y1, y2), max(y1, y2)
        for x in range(lower, upper + 1):
            image[x1][x] = 0

    elif abs(x1-x2) < abs(y1-y2):
        lower, upper = min(y1, y2), max(y1, y2)
        m = (y2 - y1) / (x2 - x1)
        c = (x2 * y1 - x1 * y2) / (x2 - x1)

        for y in range(lower, upper+1):
            image[round((y-c)/m)][y] = 0

    else:
        lower, upper = min(x1, x2), max(x1, x2)
        m = (y2-y1)/(x2-x1)
        c = (x2*y1-x1*y2)/(x2-x1)

        for x in range(lower, upper+1):
            image[x][round(m*x+c)] = 0


img = np.ones([512, 512, 3])

P1 = map(int, input('Enter Point 1: ').split())
P2 = map(int, input('Enter Point 2: ').split())
line(img, P1, P2)

cv2.imshow('Input', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
