import cv2
import numpy as np


def BresenhamLine(image, P1, P2):
    x1, y1 = P1
    x2, y2 = P2
    dx, dy = abs(x2 - x1), abs(y2 - y1)

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            image[x1][y] = 0
    else:
        if dx > dy:
            I1 = 2 * (dy - dx)
            I2 = 2 * dy
            P = 2 * dy - dx
            y = y1

            for x in range(min(x1, x2), max(x1, x2) + 1):
                if P >= 0:
                    P += I1
                    y += 1
                else:
                    P += I2
                image[x][y] = 0
        else:
            I1 = 2 * (dx - dy)
            I2 = 2 * dx
            P = 2 * dx - dy
            x = x1

            for y in range(min(y1, y2), max(y1, y2) + 1):
                if P >= 0:
                    P += I1
                    x += 1
                else:
                    P += I2
                image[x][y] = 0


img = np.ones([600, 600, 3])

print('Enter Point 1:')
X1, Y1 = map(int, input().split())
print('Enter Point 2:')
X2, Y2 = map(int, input().split())

BresenhamLine(img, (X1, Y1), (X2, Y2))

cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
