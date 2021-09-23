from myimage import *
import random, math

# Generating random point in triangle
def randomPoint(p1: (int, int), p2: (int, int), p3: (int, int)) -> [int, int]:

    x, y = sorted([random.random(), random.random()])
    r1, r2, r3 = x, y - x, 1 - y
    return [r1 * p1[0] + r2 * p2[0] + r3 * p3[0], 
            r1 * p1[1] + r2 * p2[1] + r3 * p3[1]]

# Selecting color to use for plotting point
def select_color(current_pos: (int, int), p1: (int, int), p2: (int, int), p3: (int, int)) -> (int, int, int):
    dist = []
    dist.append(math.sqrt( ((current_pos[1] - p1[1])**2) + ((current_pos[0] - p1[0])**2) ))
    dist.append(math.sqrt( ((current_pos[1] - p2[1])**2) + ((current_pos[0] - p2[0])**2) ))
    dist.append(math.sqrt( ((current_pos[1] - p3[1])**2) + ((current_pos[0] - p3[0])**2) ))

    color = [0, 0, 0]
    color[dist.index(min(dist))] = 255
    return color


def sierpinski(img: MyImage, n: int, p1: (int, int), p2: (int, int), p3: (int, int)):
    current_pos = randomPoint(p1, p2, p3)
    
    for _ in range(n):
        vertex = random.choice([p1, p2, p3])
        current_pos[0] = (vertex[0]+current_pos[0])//2
        current_pos[1] = (vertex[1]+current_pos[1])//2

        color = select_color(current_pos, p1, p2, p3)

        img.putpixel(current_pos, (*color, 255))
    
    img.show()



# Size of image
image_size = (500, 500)

# Triangle vertices
p1 = (100, 400)
p2 = (400, 400)
p3 = (250, 100)

# Number of iterations
n = 5000

img = MyImage(image_size, 0, 1, 'RGBA')
# for i in range(500):
#     for j in range(500):
#         img.putpixel((i, j), (0, 0, 0, 100))

sierpinski(img, n, p1, p2, p3)

img.img.save("sierpenski.png")
# img.show()




