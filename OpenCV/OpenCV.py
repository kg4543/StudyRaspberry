import cv2

cam = cv2.VideoCapture(0) #기본 캠
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True: 
    ret, frame = cam.read() # 웹캠 읽기

    if ret :
        cv2.imshow('CAM', frame) #카메라 영상을 CAM이라는 이름으로 창에 띄움

        key = cv2.waitKey(1)
        if key == ord('q'): #q를 입력받으면
            break

cam.release()
cv2.destroyAllWindows()