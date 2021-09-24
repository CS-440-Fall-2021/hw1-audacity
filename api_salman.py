from myimage import *
import math
import numpy


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
    points = []
    colors = []
    points.append(P)
    colors.append(P_color)

    img.putpixel(P, P_color)

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

        points.append(current_pos)
        colors.append(tuple(current_color))

    img.putpixel(Q, Q_color)
    points.append(Q)
    colors.append(Q_color)

    return points, colors


def draw_polygon_dda(img, points, colors):
    try:
        bpoints = []
        bcolors = []
        for i in range(len(points) - 1):
            p, c = draw_line(
                img, points[i], points[i+1], colors[i], colors[i+1])
            bpoints.extend(p)
            bcolors.extend(c)
        p, c = draw_line(img, points[-1], points[0],
                         colors[-1], colors[0])
        bpoints.extend(p)
        bcolors.extend(c)
        return bpoints, bcolors
    except:
        img.putpixel(points, colors)


def draw_polygon(img, points, colors, fill=True):
    bpoints, bcolors = draw_polygon_dda(img, points, colors)
    if fill:
        for i in range(len(bpoints)):
            for j in range(len(bpoints)):
                if bpoints[i][0] != bpoints[j][0] and bpoints[i][1] == bpoints[j][1]:
                    draw_line(img, bpoints[i], bpoints[j],
                              bcolors[i], bcolors[j])


# Size of image
image_size = (200, 200)

# Starting and Ending points
P = (3, 8)
Q = (18, 2)

# Color of points
P_color = (255, 0, 0, 255)
Q_color = (0, 0, 255, 255)

# points = ((0, 10), (0, 0), (19, 0), (19, 10))
points = ((50, 100), (100, 0), (150, 100))
colors = ((255, 0, 0, 255), (0, 255, 0, 255),
          (0, 0, 255, 255))

img = MyImage(image_size, 3, 10, 'RGBA')

# draw_line_dda(img, P, Q)
# draw_line(img, P, Q, P_color, Q_color)

# draw_polygon_dda(img, points, colors)
draw_polygon(img, points, colors)

img.show()
img.img.save("draw_line_dda.png")
