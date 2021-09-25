from myimage import MyImage
from api_salman import *

def circle(radius: int, subdivisions_: int):
    img = MyImage(((radius * 2) * (subdivisions_ + 1), radius*2), 0, 1, 'RGBA')
    # img = MyImage((200, 200), 0, 1, 'RGBA')
    for subdivisions in range(subdivisions_+1):
        coordinates = [[], [], [], []]

        # Forming diamond
        coordinates[0].append((radius - 1, 0)) # Top 1
        coordinates[0].append((radius, 0)) # Top 2

        coordinates[1].append(((radius * 2) - 1, radius - 1)) # Right
        coordinates[1].append(((radius * 2) - 1, radius)) # Right 2
        
        coordinates[2].append((radius - 1, (radius * 2) - 1)) # Bottom
        coordinates[2].append((radius, (radius * 2) - 1)) # Bottom 2
        
        coordinates[3].append((0, radius - 1)) # Left
        coordinates[3].append((0, radius)) # Left 2


        coordinates[2] = coordinates[2][::-1]
        coordinates[3] = coordinates[3][::-1]



        # Subdivision
        if subdivisions >= 1:
            angle = -90
            for quadrant in range(len(coordinates)):
                for division in range(subdivisions):

                    angle += ( 90 / (subdivisions+1) )
                    
                    projection = (round(( radius * math.cos(angle*(math.pi/180)) )+radius), round(( radius * math.sin(angle*(math.pi/180)) )+radius))
                    print(angle)
                    # img.putpixel(projection, (255, 255, 255, 255))
                    
                    coordinates[quadrant].append(projection)
                print("LOOP OVER")
                # angle = ((quadrant-1)*90) / (subdivisions+1)
                angle += ( 90 / (subdivisions+1) )



        # Consolidate 
        previous_point = coordinates[0][0] 
        points = []
        colors = []
        for quadrant in coordinates:
            for coordinate in quadrant:

                # print(math.dist(previous_point, coordinate))
                previous_point = coordinate
                coordinate = (coordinate[0] + (subdivisions*(radius*2)), coordinate[1])
                points.append(coordinate)
                colors.append((255, 0, 0, 255))

        # print(math.dist(previous_point, coordinates[0][0]))

        draw_polygon(img, points, colors, False)
        

    return img

circle(50, 10).img.save("circle.png")
