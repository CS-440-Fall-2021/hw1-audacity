from myimage import *
import math, numpy

def draw_line_dda(img: MyImage, P: (int, int), Q: (int, int)):
    img.putpixel(P, (255, 255, 255, 255))

    if (P[0] == Q[0]):
        gradient = Q[1] - P[1]
        offset = 0
    else:
        gradient = (Q[1] - P[1])/(Q[0] - P[0])
        offset = 1 if (Q[0] - P[0]) >= 1 else -1

    if Q[0] < P[0]: gradient *= -1

    current_pos = list(P)
    actual_y = current_pos[1]


    while current_pos != list(Q):
        print(current_pos, actual_y)
        current_pos[0] += offset
        actual_y += min(1, gradient)
        current_pos[1] = round(actual_y)

        img.putpixel(current_pos, (255, 0, 0, 255))

    img.putpixel(Q, (255, 255, 255, 255))
    

# Size of image
image_size = (20, 10)

# Starting and Ending points
P = (0, 1)
Q = (8, 0)
 

img = MyImage(image_size, 3, 10, 'RGBA')

draw_line_dda(img, P, Q)

img.show()
img.img.save("draw_line_dda.png")