from api import *

def getMid(p1, p2):  # calculate mid point of a line between two points.
    return ((p1[0]+p2[0]) // 2, (p1[1] + p2[1]) // 2)


def calc_mid(p1, p2, origin):  # used to calculate the point on the arc of the circle
    # calculate mid point of line between p1 and p2
    mid_point = getMid(p1, p2)
    
    # generate vector from mid to center of circle
    vector = (mid_point[0] - origin[0], mid_point[1] - origin[1])
    
    norm = math.sqrt(vector[0]**2 + vector[1]**2)  # norm of the vector
    unit_vec = [vector[0]/norm, vector[1]/norm]  # turn into unit vector
    
    new_point = (int(origin[0] + origin[0]*unit_vec[0]),  # generate new point by scaling vector to r and adding center
                 int(origin[1] + origin[0]*unit_vec[1]))
    
    return new_point


def circle(radius, subdivs=0):
    subdivs += 1
    img = MyImage((radius*2*subdivs + 1, radius*2 + 1), 0, 1)

    img.fill((255, 255, 255, 255))  # fill the image with white background
    
    points = [(radius, 0), (0, radius), (radius, radius*2),
              (radius*2, radius)]  # initial points for diamond
    
    colors = [(255, 0, 0, 255), (255, 0, 0, 255),
              (255, 0, 0, 255), (255, 0, 0, 255)]  # initial colors for diamond
    
    draw_polygon_dda(img, points, colors)  # draw diamond
    
    for i in range(1, subdivs):  # loop over subdivs
        
        # array to store initail points + midpoints on the arc of circle (new points)
        npoints = []
        
        for j in range(len(points) - 1):  # loop over all points except last
            mid = calc_mid(
                points[j], points[j+1], (radius, radius))  # midpoint on the arc
            
            npoints.append(points[j])
            npoints.append(mid)
            npoints.append(points[j+1])
        
        # calculating mid from last to first point
        mid = calc_mid(
            points[-1], points[0], (radius, radius))
        
        npoints.append(points[-1])
        npoints.append(mid)
        npoints.append(points[0])

        # adjusted points to draw polygon after the old one (printing points)
        ppoints = []
        
        for x in range(len(npoints)):
            # adding radius*2 to adjust for new subdiv
            ppoints.append((npoints[x][0] + (radius*2*i), npoints[x][1]))
        
        for z in range(len(npoints) - len(colors)):  # compensating for colors
            colors.append((255, 0, 0, 255))
        
        draw_polygon_dda(img, ppoints, colors)  # drawing new polygon
        points = npoints  # changeing old points to new points
    
    return img


def sierpinski_level(img, level, points):  # recursive funtion to draw triangles
    if level == 1:  # only one triangle
        draw_polygon(img, points, ((0, 0, 0, 255),  # draw triangle
                     (0, 0, 0, 255), (0, 0, 0, 255)))
    
    else:
        # get mid points on the edges of the triangle
        mid1, mid2, mid3 = getMid(points[0], points[1]), getMid(
            points[1], points[2]), getMid(points[0], points[2])  
        
        # draw triangles using mid points
        sierpinski_level(img, level - 1, (points[0], mid1, mid3))
        sierpinski_level(img, level - 1, (mid1, points[1], mid2))
        sierpinski_level(img, level - 1, (mid3, mid2, points[2]))
    
    return img


def sierpinski(level):  # main function

    # dimension for each triangle (reduce it speed up the process, reducing will reduce the quality too)
    dimension = 500
    
    gap = 10  # gap between each triangle in pixels
    
    level += 1
    img = MyImage(((dimension*level) + (gap*level) + 1, dimension + 1), 0, 10)
    img.fill((255, 255, 255, 255))  # fill with white background
    
    # initial points for first triangle
    points = [(0, dimension), (dimension//2, 0), (dimension, dimension)]
    
    for i in range(1, level):
        sierpinski_level(img, i, points)  # call recursive function
        
        # adjust for next triangle
        points[0] = points[0][0] + dimension + gap, points[0][1]
        points[1] = points[1][0] + dimension + gap, points[1][1]
        points[2] = points[2][0] + dimension + gap, points[2][1]
    
    img = sierpinski_level(img, level, points)
    
    return img


def application_test():  # funct to test circle and sierpinski
    circle(100, 4).show()
    sierpinski(4).show()

if __name__ == '__main__':
    application_test()