from myimage import *
import math
import numpy

# Calculate gradients of line


def calc_gradient(P: (int, int), Q: (int, int)):
    dy = Q[1] - P[1]
    dx = Q[0] - P[0]

    max_dist = max(abs(dy), abs(dx))

    dx /= (max_dist+1)
    dy /= (max_dist+1)

    return dx, dy, max_dist

# Draws a line using the DDA Algo


def draw_line_dda(img: MyImage, P: (int, int), Q: (int, int)):
    if (P == Q):
        return

    img.putpixel(P, (255, 255, 255, 255))

    gradient_x, gradient_y, max_dist = calc_gradient(P, Q)

    current_pos = P
    actual_x, actual_y = current_pos

    # Updates x and y coordinates to plot the line
    for _ in range(max_dist):
        actual_x += gradient_x
        actual_y += gradient_y

        current_pos = (round(actual_x), round(actual_y))
        img.putpixel(current_pos, (255, 0, 0, 255))

    img.putpixel(Q, (255, 255, 255, 255))


# Draws a line with a color gradient
def draw_line(img: MyImage, P: (int, int), Q: (int, int),
              P_color: (int,)*4, Q_color: (int,)*4) -> ((int,)*3, (int,)*4):

    point_color = []  # Stores (coordinates, color) pairs of pixels in line

    img.putpixel(P, P_color)
    point_color.append((P, P_color))

    if (P == Q):
        return []

    gradient_x, gradient_y, max_dist = calc_gradient(P, Q)

    current_pos = P
    actual_x, actual_y = current_pos

    current_color = list(P_color)[:]
    actual_color = current_color[:]

    # Calculating the color channel gradients
    gradient_color = []
    for i in range(4):
        gradient_color.append((Q_color[i] - P_color[i]) / (max_dist+1))

    # Updates x, y coordinates and color channels to plot the line
    for _ in range(max_dist+1):
        actual_x += gradient_x
        actual_y += gradient_y

        current_pos = (round(actual_x), round(actual_y))

        for i in range(4):
            actual_color[i] += gradient_color[i]

            current_color[i] = round(actual_color[i])

        img.putpixel(current_pos, (tuple(current_color)))
        point_color.append((current_pos, tuple(current_color)))

    img.putpixel(Q, Q_color)
    point_color.append((Q, Q_color))

    return point_color

# Draws a polygon by connecting successive points


def draw_polygon_dda(img: MyImage, points: [(int, int), ...], colors: [(int, int, int, int), ...]):

    for i in range(1, len(points)):
        draw_line(img, P=points[i-1], Q=points[i],
                  P_color=colors[i-1], Q_color=colors[i])

    if len(points) > 2:
        draw_line(img, P=points[0], Q=points[-1],
                  P_color=colors[0], Q_color=colors[-1])
    else:
        img.putpixel(points[0], colors[0])


# Draws a polygon by connecting successive points and fills it
def draw_polygon(img: MyImage, points: [(int, int), ...], colors: [(int, int, int, int), ...], fill: bool = True):
    point_color = []  # Stores (coordinates, color) pairs

    for i in range(1, len(points)):
        point_color += draw_line(img, P=points[i-1], Q=points[i],
                                 P_color=colors[i-1], Q_color=colors[i])

    if len(points) > 2:
        point_color += draw_line(img, P=points[0], Q=points[-1],
                                 P_color=colors[0], Q_color=colors[-1])
    else:
        img.putpixel(points[0], colors[0])

    lines_drawn = 0

    if fill:
        row_separated = {}  # Separates each row for filling

        for i in point_color:
            if i[0][1] not in row_separated:
                row_separated[i[0][1]] = {}
            row_separated[i[0][1]][i[0][0]] = i[1]

        for row in row_separated:
            row_ = list(row_separated[row].items())
            row_.sort(key=lambda x: x[0])

            for k in range(1, len(row_)):
                draw_line(img, P=(row_[k-1][0], row), Q=(row_[k][0],
                          row), P_color=row_[k-1][1], Q_color=row_[k][1])
                lines_drawn += 1


def api_test():
    # Size of image
    image_size_line = (20, 10)
    image_size_polygon = (110, 110)

    # Starting and Ending points for draw_line
    P = (0, 4)
    Q = (9, 0)

    # Color of points
    P_color = (255, 0, 0, 255)
    Q_color = (0, 0, 255, 255)

    # List of points for polygon
    points = [(0, 100), (50, 0), (100, 100)]
    # points = [(1, 1), (1, 9), (18, 9), (18, 1)]
    # points = [(1, 8), (10, 1), (18, 8)]
    # points = [(5,5), (10, 9)]

    # List of colors for polygon
    colors = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)]
    # colors = [(0, 255, 0, 255), (255, 0, 0, 255), (255, 255, 255, 255), (0, 0, 255, 255)]
    # colors = [(255, 0, 0, 255), (0, 255, 0 ,255), (0, 0, 255, 255)]
    # colors = [(255, 0, 0, 255), (0, 255, 0, 255)]

    img_line = MyImage(image_size_line, 3, 10, 'RGBA')
    img_polygon = MyImage(image_size_polygon, 3, 10, 'RGBA')

    draw_line(img_line, P, Q, P_color, Q_color)
    draw_polygon(img_polygon, points, colors, True)

    img_line.show()
    img_polygon.show()


if __name__ == '__main__':
    api_test()
