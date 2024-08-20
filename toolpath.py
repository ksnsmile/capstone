# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:58:23 2024

@author: sn714
"""
import cv2
import numpy as np
import pandas as pd

class Node:
    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z

def tool_path_1(start_1,start_2 ,radius_1,raidus_2, width, steps,height):
    path = []
    width_step = width / steps 
    height_step= height/steps
    if width>height:
        current_position = np.array([start_1.x, start_1.y, start_1.z], dtype=float)
        path.append(Node(current_position[0], current_position[1], current_position[2]))

        for i in range(steps):
            # 각도에 따라 x, y 좌표 이동
            A=[0,1,2,3,4,20,21,22,23,24,40,41,42,43,44] 
            B=[5,6,7,8,9,25,26,27,28,29,45,46,47,48,49] 
            C=[10,11,12,13,14,30,31,32,33,34] 
            
            if i in A:
                
                if i % 5 == 0:
                    
                    for a in range(5):
                        current_position[0] += width_step
                        current_position[1] += radius_1/5
                        current_position[2] = radius_1*np.cos(-(a+1)*(np.pi/10))
                        path.append(Node(current_position[0], current_position[1], current_position[2]))
            
            elif i in B: 
                
                if i % 5 == 0:
                    
                    for a in range(5):
                        current_position[0] += width_step
                        current_position[1] -= radius_1/5
                        current_position[2] = radius_1*np.cos(-(4-a)*(np.pi/10))
                        path.append(Node(current_position[0], current_position[1], current_position[2]))
                        
                        
            elif i in C:
                
                if i % 5 == 0:
                    
                    for a in range(5):
                        current_position[0] += width_step 
                        current_position[1] -= radius_1/5
                        current_position[2] = radius_1*np.cos((a+1)*(np.pi/10))
                        path.append(Node(current_position[0], current_position[1], current_position[2]))
                        
            else :
                
                if i % 5 == 0:
                    
                    for a in range(5):
                        current_position[0] += width_step 
                        current_position[1] += radius_1/5
                        current_position[2] = radius_1*np.cos((4-a)*(np.pi/10))
                        path.append(Node(current_position[0], current_position[1], current_position[2]))

    else: 

        current_position = np.array([start_2.x, start_2.y, start_2.z], dtype=float)
        path.append(Node(current_position[0], current_position[1], current_position[2]))

        for i in range(steps):
            A = [0, 1, 2, 3, 4, 20, 21, 22, 23, 24, 40, 41, 42, 43, 44]
            B = [5, 6, 7, 8, 9, 25, 26, 27, 28, 29, 45, 46, 47, 48, 49]
            C = [10, 11, 12, 13, 14, 30, 31, 32, 33, 34]


            if i in A:
                    
                    if i % 5 == 0:
                        
                        for a in range(5):
                            current_position[0] += raidus_2/5
                            current_position[1] += height_step
                            current_position[2] = raidus_2*np.cos((a+1)*(np.pi/10))
                            path.append(Node(current_position[0], current_position[1], current_position[2]))
                
            elif i in B: 
                    
                    if i % 5 == 0:
                        
                        for a in range(5):
                            current_position[0] -= raidus_2/5
                            current_position[1] += height_step
                            current_position[2] = raidus_2*np.cos((4-a)*(np.pi/10))
                            path.append(Node(current_position[0], current_position[1], current_position[2]))
                            
                            
            elif i in C:
                    
                    if i % 5 == 0:
                        
                        for a in range(5):
                            current_position[0] -= raidus_2/5 
                            current_position[1] += height_step
                            current_position[2] = raidus_2*np.cos(-(a+1)*(np.pi/10))
                            path.append(Node(current_position[0], current_position[1], current_position[2]))
                            
            else :
                    
                    if i % 5 == 0:
                        
                        for a in range(5):
                            current_position[0] += raidus_2/5 
                            current_position[1] += height_step
                            current_position[2] = raidus_2*np.cos(-(4-a)*(np.pi/10))
                            path.append(Node(current_position[0], current_position[1], current_position[2]))
                        
            

    
    return path 

def tool_path_2(start,goal):

    path = []
    width_step = width / steps 
    height_step= height/steps

    
    for i in range(3):

        current_position = np.array([start.x, start.y, start.z], dtype=float)
        path.append(Node(current_position[0], current_position[1], current_position[2]))

        current_position = np.array([goal.x, goal.y, goal.z], dtype=float)
        path.append(Node(current_position[0], current_position[1], current_position[2])) 

    return path




def draw_tool_path(image, path_coords):
    x_vals, y_vals, z_vals = zip(*path_coords)
    
    # 경로 그리기
    for i in range(len(x_vals) - 1):
        cv2.line(image, (int(x_vals[i]), int(y_vals[i])), (int(x_vals[i+1]), int(y_vals[i+1])), (255, 0, 0), 2)
        
    for x, y, z in zip(x_vals, y_vals, z_vals):
        cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)


def write_csv(path_coords, class_name):
    # 데이터프레임 생성
    df = pd.DataFrame(path_coords, columns=['x', 'y', 'z'])
    # 파일명을 클래스 이름으로 설정하여 저장
    filename = f"{class_name}.csv"
    df.to_csv(filename, index=False)
    

  









 




