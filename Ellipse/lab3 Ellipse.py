import cv2
import numpy as np


def MidpointEllipse(image, X, Y, a, b):
    x = 0
    y = b
    aa = a*a
    bb = b*b
    aa2 = aa*2
    bb2 = bb*2
    fx = 0
    fy = aa2*b
    p = bb-aa*b + 0.25*aa

    while fx < fy:
        image[X + x][Y + y] = 0
        image[X + x][Y - y] = 0
        image[X - x][Y + y] = 0
        image[X - x][Y - y] = 0

        x += 1
        fx = fx+bb2

        if p < 0:
            p = p+fx + bb
        else:
            y -= 1
            fy = fy-aa2
            p = p+fx+bb-fy
    image[X + x][Y + y] = 0
    image[X + x][Y - y] = 0
    image[X - x][Y + y] = 0
    image[X - x][Y - y] = 0

    p = bb*(x+0.5)*(x+0.5) + aa*(y-1)*(y-1) - aa*bb

    while y > 0:
        y -= 1
        fy = fy - aa2
        if p >= 0:
            p = p - fy + aa
        else:
            x += 1
            fx = fx + bb2
            p = p + fx - fy + aa
        image[X + x][Y + y] = 0
        image[X + x][Y - y] = 0
        image[X - x][Y + y] = 0
        image[X - x][Y - y] = 0


img = np.ones([600, 600, 3])

print('Enter Center Point:')
Xc, Yc = map(int, input().split())
print('Enter major axis and minor axis:')
A, B = map(int, input().split())
MidpointEllipse(img, Xc, Yc, A, B)

cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
