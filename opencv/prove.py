import numpy as np

# 픽셀 좌표 하나만 설정
pixel_point = np.array([707.0, 345.0, 1.0])

# 로봇 좌표
robot_point = np.array([245, 335, 1])

# y축을 기준으로 x만 반전시킨것 
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

print(transformation_matrix)
# 테스트 수행
robot_point_transformed = transformation_matrix @ pixel_point

print(f"변환된 로봇 좌표 = {robot_point_transformed}, 실제 로봇 좌표 = {robot_point}")
