from PIL.Image import register_decoder
from myimage import MyImage
from api_salman import *


def circle(radius: int, subdivisions_: int):
    img = MyImage(((radius * 2) * (subdivisions_ + 1), radius*2), 0, 1, 'RGBA')
    # img = MyImage((200, 200), 0, 1, 'RGBA')
    for subdivisions in range(subdivisions_+1):
        coordinates = [[], [], [], []]

        # Forming diamond
        coordinates[0].append((radius - 1, 0))  # Top 1
        coordinates[0].append((radius, 0))  # Top 2

        coordinates[1].append(((radius * 2) - 1, radius - 1))  # Right
        coordinates[1].append(((radius * 2) - 1, radius))  # Right 2

        coordinates[2].append((radius - 1, (radius * 2) - 1))  # Bottom
        coordinates[2].append((radius, (radius * 2) - 1))  # Bottom 2

        coordinates[3].append((0, radius - 1))  # Left
        coordinates[3].append((0, radius))  # Left 2

        coordinates[2] = coordinates[2][::-1]
        coordinates[3] = coordinates[3][::-1]

        # Subdivision
        if subdivisions >= 1:
            angle = -90
            for quadrant in range(len(coordinates)):
                for division in range(subdivisions):

                    angle += (90 / (subdivisions+1))

                    projection = (round((radius * math.cos(angle*(math.pi/180)))+radius),
                                  round((radius * math.sin(angle*(math.pi/180)))+radius))
                    print(angle)
                    # img.putpixel(projection, (255, 255, 255, 255))

                    coordinates[quadrant].append(projection)
                print("LOOP OVER")
                # angle = ((quadrant-1)*90) / (subdivisions+1)
                angle += (90 / (subdivisions+1))

        # Consolidate
        previous_point = coordinates[0][0]
        points = []
        colors = []
        for quadrant in coordinates:
            for coordinate in quadrant:

                # print(math.dist(previous_point, coordinate))
                previous_point = coordinate
                coordinate = (
                    coordinate[0] + (subdivisions*(radius*2)), coordinate[1])
                points.append(coordinate)
                colors.append((255, 0, 0, 255))

        # print(math.dist(previous_point, coordinates[0][0]))

        draw_polygon(img, points, colors, False)

    return img


def getMid(p1, p2):
    return ((p1[0]+p2[0]) // 2, (p1[1] + p2[1]) // 2)


def sierpinski_level(img, level, points):
    if level == 1:
        draw_polygon(img, points, ((0, 0, 0, 255),
                     (0, 0, 0, 255), (0, 0, 0, 255)))
    else:
        mid1, mid2, mid3 = getMid(points[0], points[1]), getMid(
            points[1], points[2]), getMid(points[0], points[2])
        sierpinski_level(img, level - 1, (points[0], mid1, mid3))
        sierpinski_level(img, level - 1, (mid1, points[1], mid2))
        sierpinski_level(img, level - 1, (mid3, mid2, points[2]))
    return img


def sierpinski(level):
    dimension = 1000
    gap = 10
    level += 1
    img = MyImage(((dimension*level) + (gap*level) + 1, dimension + 1), 0, 10)
    img.fill((255, 255, 255, 255))
    points = [(0, dimension), (dimension//2, 0), (dimension, dimension)]
    for i in range(1, level):
        sierpinski_level(img, i, points)
        points[0] = points[0][0] + dimension + gap, points[0][1]
        points[1] = points[1][0] + dimension + gap, points[1][1]
        points[2] = points[2][0] + dimension + gap, points[2][1]
    img = sierpinski_level(img, level, points)

    img.img.save("sierpinski.png")


# circle(50, 10).img.save("circle.png")
sierpinski(4)
