# This file is used to randomly layout the competition feild.
# Author : fanghao_w
#  DATE  : 2021.07.23
import numpy as np
import matplotlib.pyplot as plt
import cv2

"""
yellow -> 黄基座 * 3  -> (255,255,0)
empty  -> 种子盘 * 3  -> (255,255,255)
green  -> 绿基座 * 18 -> (0,255,0)
"""

layout = 3 * ["yellow"] + 3 * ["empty"] + 18 * ["green"]
np.random.shuffle(layout)
print("The 1st row layout : ",layout[:12])
print("The 2nd row layout : ",layout[12:])

# Find yellow and empty random result
layout = np.reshape(np.array(layout),(2,12))
yellow_coordinates = np.argwhere(layout == "yellow")
empty_coordinates = np.argwhere(layout == "empty")

# Configuration
background_color = np.reshape(np.array([210,105,30],dtype="uint8"),(1,1,3))
img = np.tile(background_color,(500,1200,1))
yellow_color = (255,255,0)
empty_color = (255,255,255)
green_color = (0,255,0)
original_coordinates = (160,150)
x_step = 80
y_step = 200

def draw_circle(image, center_coordinates, color=green_color):
    radius = 20
    thickness = -1 
    image = cv2.circle(image, center_coordinates, radius, color, thickness) 
    return image

def main(img):
    # Draw green circles
    for i in range(12):
        for j in range(2):
            img = draw_circle(img,(original_coordinates[0]+x_step*i, \
                    original_coordinates[1]+y_step*j))

    # Draw yellow and empty circles
    for i in range(3):
        x_index,y_index = yellow_coordinates[i,1],yellow_coordinates[i,0]
        img = draw_circle(img,(original_coordinates[0]+x_step*x_index, \
                    original_coordinates[1]+y_step*y_index), color=yellow_color)
        
        x_index,y_index = empty_coordinates[i,1],empty_coordinates[i,0]
        img = draw_circle(img,(original_coordinates[0]+x_step*x_index, \
                    original_coordinates[1]+y_step*y_index), color=empty_color)

    # Start area and End area
    img = cv2.rectangle(img,(0,0),(100,100),(0,0,150),-1)
    img = cv2.rectangle(img,(0,400),(100,500),(200,0,0),-1)
    # Electronic line
    img = cv2.rectangle(img,(50,50),(1150,450),(255,255,255),10)
    img = cv2.line(img,(50,230),(1150,230),(255,255,255),10)
    img = cv2.line(img,(50,270),(1150,270),(255,255,255),10)
    # Middle line
    img = cv2.line(img,(600,0),(600,500),(255,0,0),3)

    plt.imshow(img)
    plt.title("Competition Random Layout"),plt.xticks([]),plt.yticks([])
    plt.ylabel("Start - - - - - - - - - - - - - - End")
    plt.show()

if __name__ == "__main__":
    main(img)