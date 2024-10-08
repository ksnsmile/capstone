# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:58:23 2024

@author: sn714
"""
import cv2
import numpy as np
import pandas as pd
import csv

class Node:
    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z

# 시계방향 180도 회전 행렬 생성
rotation_matrix = np.array([[-1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]])

# 스케일링 행렬 (x에 1.25, y에 1.4 적용)
scaling_matrix = np.array([[1.25, 0, 0],
                           [0, 1.4, 0],
                           [0, 0, 1]])

# 이동 행렬 (카메라 좌표계의 이동 위치)
translation_matrix = np.array([[1, 0, 500.25],
                               [0, 1, -132],
                               [0, 0, 1]])

# 전체 변환 행렬 계산 (스케일링 → 회전 → 이동)
transformation_matrix = translation_matrix @ rotation_matrix @ scaling_matrix

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
    


def convert_to_robot_coords(path, a):
    robot_path = []
    for node in path:
        # 3D 좌표를 4D 동차 좌표로 변환
        xyz = np.array([node.x, node.y, node.z])
        
        # 변환 행렬 a를 사용해 로봇 좌표계로 변환
        robot_coords = transformation_matrix @ xyz
        
        # 변환된 좌표를 새로운 Node로 추가
        robot_path.append(Node(robot_coords[0], robot_coords[1], robot_coords[2]))
    
    return robot_path


def draw_tool_path(image, path_coords):
    x_vals, y_vals, z_vals = zip(*path_coords)
    
    # 경로 그리기
    for i in range(len(x_vals) - 1):
        cv2.line(image, (int(x_vals[i]), int(y_vals[i])), (int(x_vals[i+1]), int(y_vals[i+1])), (255, 0, 0), 2)
        


def write_csv(robot_path):
    # CSV 파일을 쓰기 모드로 열기
    f = open('C:/Users/ksn71/OneDrive/바탕 화면/git/capstone_git/yolov5/Var_P.csv', 'w', newline='')  
    csv_writer = csv.writer(f)  # CSV 작성기 객체 생성

    # 메타데이터 작성
    csv_writer.writerow(['===== Export Data Var P ====='])  
    csv_writer.writerow(['RobotTypeName :', 'VP-5243'])
    csv_writer.writerow(['RobotTypeID :', '65', '0'])
    csv_writer.writerow(['File Version :', '2'])
    csv_writer.writerow(['[No.]', '[X]', '[Y]', '[Z]', '[RX]', '[RY]', '[RZ]', '[FIG]', '[using]', '[macro name]'])

    # robot_path의 각 점에 대해 CSV 파일에 작성
    for k, robotPt in enumerate(robot_path):
        # robotPt는 Node 객체이므로 속성을 사용하여 값을 추출
        csv_writer.writerow([k, robotPt.x, robotPt.y, 183.63, 180, 0, 0, '13 - Lefty | Above | NonFlip | J6Double | J4Single | J1Single'])

    # 파일 닫기
    f.close()

  









 




