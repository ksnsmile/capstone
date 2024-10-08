import cv2

# 마우스 클릭 이벤트 처리 함수
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 버튼 클릭 이벤트
        print(f"Mouse clicked at: ({x}, {y})")

# 카메라 캡처 시작
cap = cv2.VideoCapture(1)  # 0은 기본 카메라를 의미, 다른 번호는 추가 카메라를 의미

# 윈도우에 마우스 콜백 함수 등록
cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", mouse_callback)

while True:
    # 카메라로부터 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture image")
        break

    # 화면에 프레임 출력
    cv2.imshow("Camera", frame)

    # 'ESC' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키
        break

# 종료 후 카메라와 윈도우 해제
cap.release()
cv2.destroyAllWindows()
