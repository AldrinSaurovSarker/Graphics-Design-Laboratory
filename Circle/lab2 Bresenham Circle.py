import cv2
import numpy as np


def BresenhamCircle(image, xc, yc, r):
    d = 3 - 2 * r
    x = 0
    y = r

    while y >= x:
        image[xc + x][yc + y] = 0
        image[xc + x][yc - y] = 0
        image[xc - x][yc + y] = 0
        image[xc - x][yc - y] = 0
        image[xc + y][yc + x] = 0
        image[xc + y][yc - x] = 0
        image[xc - y][yc + x] = 0
        image[xc - y][yc - x] = 0

        if d <= 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1


img = np.ones([600, 600, 3])

print('Enter Center Point:')
Xc, Yc = map(int, input().split())
print('Enter Radius:')
R = int(input())
BresenhamCircle(img, Xc, Yc, R)

cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
