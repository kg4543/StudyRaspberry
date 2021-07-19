import cv2

cam = cv2.VideoCapture(0) #기본 캠
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID') #XVID 비디오 코덱사용
isRecord = False #녹화 상태

while True: 
    ret, frame = cam.read() # 웹캠 읽기

    if ret :
        cv2.imshow('CAM', frame) #카메라 영상을 CAM이라는 이름으로 창에 띄움

        key = cv2.waitKey(1)
        if key == ord('q'): #q를 입력받으면 종료
            break
        elif key == ord('c'): #c를 입력받으면 화면 캡쳐
            cv2.imwrite('./Capture/captured.jpg', frame) #캡쳐
            print('Complete Image Capture')
        elif key == ord('r') and isRecord == False: #r을 입력받으면 화면 녹화
            isRecord = True
            video = cv2.VideoWriter('./Capture/record.avi', fourcc, 20, (frame.shape[1], frame.shape[0])) #파일 위치, 코덱, 프레임 수
            print('Start Record')
        elif key == ord('r') and isRecord == True :
            isRecord = False
            video.release()
            print('Stop Record')
            
        if isRecord == True: #현재화면 녹화
            video.write(frame)
            
cam.release()
cv2.destroyAllWindows()