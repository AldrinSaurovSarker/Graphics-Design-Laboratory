import cv2
import numpy as np


def MidpointEllipse(img, X, Y, a, b):
    a, b = b, a
    x, y = 0, b
    aa, bb = a * a, b * b
    aa2, bb2 = aa * 2, bb * 2
    fx, fy = 0, aa2 * b
    p = bb - (aa * b) + (0.25 * aa)

    while fx < fy:
        img[X + x][Y + y] = 0
        img[X + x][Y - y] = 0
        img[X - x][Y + y] = 0
        img[X - x][Y - y] = 0
        x += 1
        fx = fx + bb2

        if p < 0:
            p = p + fx + bb
        else:
            y -= 1
            fy = fy - aa2
            p = p + fx + bb - fy
    img[X + x][Y + y] = 0
    img[X + x][Y - y] = 0
    img[X - x][Y + y] = 0
    img[X - x][Y - y] = 0

    p = bb * (x + 0.5) * (x + 0.5) + aa * (y - 1) * (y - 1) - aa * bb

    while y > 0:
        y -= 1
        fy = fy - aa2
        if p >= 0:
            p = p - fy + aa
        else:
            x += 1
            fx = fx + bb2
            p = p + fx - fy + aa
        img[X + x][Y + y] = 0
        img[X + x][Y - y] = 0
        img[X - x][Y + y] = 0
        img[X - x][Y - y] = 0


image = np.ones([600, 600, 3])
Xc, Yc = map(int, input('Enter Center Point : ').split())
A, B = map(int, input('Enter Major and Minor axes : ').split())

MidpointEllipse(image, Xc, Yc, A, B)
cv2.imshow('Output', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
