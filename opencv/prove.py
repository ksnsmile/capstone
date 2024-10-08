import cv2
import numpy as np

# 입력 변수
robot_points = [
    np.array([245, 335, 1]),
    np.array([53, 330, 1]),
    np.array([224, 248, 1]),
    np.array([-45, 250, 1]),
    np.array([142, 180, 1])
]

pixel_points = [
    np.array([207, 345, 1]),
    np.array([371, 318, 1]),
    np.array([237, 269, 1]),
    np.array([443, 259, 1]),
    np.array([311, 215, 1])
]


# 반시계방향 180도 회전 행렬 생성
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

# 테스트 수행
for i, pixel_point in enumerate(pixel_points):
    robot_point_transformed = transformation_matrix @ pixel_point
    print(f"실험 {i+1}: 변환된 로봇 좌표 = {robot_point_transformed}, 실제 로봇 좌표 = {robot_points[i]}")
