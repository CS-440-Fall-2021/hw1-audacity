from myimage import *
import math, numpy

def calc_gradient(P: (int, int), Q: (int, int)):
    dy = Q[1] - P[1]
    dx = Q[0] - P[0]

    max_dist = max(abs(dy), abs(dx))

    dx /= max_dist
    dy /= max_dist

    return dx, dy, max_dist

def draw_line_dda(img: MyImage, P: (int, int), Q: (int, int)):
    img.putpixel(P, (255, 255, 255, 255))
    
    gradient_x, gradient_y, max_dist = calc_gradient(P, Q)

    current_pos = P
    actual_x, actual_y = current_pos

    for _ in range(max_dist):
        actual_x += gradient_x
        actual_y += gradient_y

        current_pos = (round(actual_x), round(actual_y))
        img.putpixel(current_pos, (255, 0, 0, 255))

    img.putpixel(Q, (255, 255, 255, 255))


def draw_line(img: MyImage, P: (int, int), Q: (int, int), P_color: (int,)*4, Q_color: (int,)*4):
    img.putpixel(P, (255, 255, 255, 255))
    
    gradient_x, gradient_y, max_dist = calc_gradient(P, Q)

    current_pos = P
    actual_x, actual_y = current_pos
    
    current_color = list(P_color)
    actual_color = current_color


    gradient_color = []
    for i in range(4):
        gradient_color.append((Q_color[i] - P_color[i]) / max_dist)
    
    for _ in range(max_dist):
        actual_x += gradient_x
        actual_y += gradient_y
        
        current_pos = (round(actual_x), round(actual_y))
        
        for i in range(4):
            actual_color[i] += gradient_color[i]
            current_color[i] = round(actual_color[i])
        
        img.putpixel(current_pos, tuple(current_color))

    img.putpixel(Q, (255, 255, 255, 255))


# Size of image
image_size = (20, 10)

# Starting and Ending points
P = (0, 4)
Q = (9, 0)
 
# Color of points
P_color = (255, 0, 0, 255)
Q_color = (0, 0, 255, 255)

img = MyImage(image_size, 3, 10, 'RGBA')

# draw_line_dda(img, P, Q)
draw_line(img, P, Q, P_color, Q_color)

img.show()
img.img.save("draw_line_dda.png")