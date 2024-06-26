# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:56:38 2024

@author: sn714
"""
import cv2 
import numpy as np


class Node:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

def generate_zigzag_path(start, goal, width, height, steps):
    path = []
    x_step = width / steps
    y_step = height 
    
    current_position = np.array([start.x, start.y, start.z], dtype=float)
    path.append(Node(current_position[0], current_position[1], current_position[2]))
    
    for i in range(steps):
        # x 방향으로 이동
        current_position[0] += x_step
        
        if i % 2 == 0:
            # y 방향으로 위로 이동
            current_position[1] += y_step
        else:
            # y 방향으로 아래로 이동
            current_position[1] -= y_step
        
        path.append(Node(current_position[0], current_position[1], current_position[2]))

    path.append(goal)
    return path

def draw_zigzag_path(image, path_coords):
    x_vals, y_vals, _ = zip(*path_coords)
    for i in range(len(x_vals) - 1):
        cv2.line(image, (int(x_vals[i]), int(y_vals[i])), (int(x_vals[i+1]), int(y_vals[i+1])), (255, 0, 0), 2)
    for x, y in zip(x_vals, y_vals):
        cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)


