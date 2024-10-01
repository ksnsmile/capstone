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

def tool_path(start, goal, width, height, steps, num_loops=3):
    path = []
    x_step = width / steps
    y_step = height  # y 값 고정
    z_value = start.z  # z 값 고정
    
    current_position = np.array([start.x, start.y, start.z], dtype=float)
    path.append(Node(current_position[0], current_position[1], current_position[2]))
    
    for _ in range(num_loops):  # 왕복을 num_loops 횟수만큼 반복
        # 시작 지점에서 목표 지점으로 이동
        for i in range(steps):
            current_position[0] += x_step  # x 방향으로 이동
            path.append(Node(current_position[0], current_position[1], current_position[2]))

        # 목표 지점에서 시작 지점으로 되돌아감
        for i in range(steps):
            current_position[0] -= x_step  # x 방향으로 역이동
            path.append(Node(current_position[0], current_position[1], current_position[2]))

    return path


def draw_tool_path(image, path_coords):
    x_vals, y_vals, z_vals = zip(*path_coords)
    
    # 경로 그리기
    for i in range(len(x_vals) - 1):
        cv2.line(image, (int(x_vals[i]), int(y_vals[i])), (int(x_vals[i+1]), int(y_vals[i+1])), (255, 0, 0), 2)
        


def write_csv(path_coords, class_name):
    # 데이터프레임 생성
    df = pd.DataFrame(path_coords, columns=['x', 'y', 'z'])
    # 파일명을 클래스 이름으로 설정하여 저장
    filename = f"{class_name}.csv"
    df.to_csv(filename, index=False)






  









 




