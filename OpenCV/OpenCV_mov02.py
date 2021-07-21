import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

#카메라 기본 프레임
cam = cv2.VideoCapture(0) # cam 열기, 번호 0 ~ 
cam.set(cv2.CAP_PROP_FRAME_WIDTH,640) # 크기 조절
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

#나눔고딕볼트 로드
font = ImageFont.truetype('./Fonts/NanumGothicBold.ttf', 20)
# 영상 저장 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
is_record = False

while True:
    ret, frame = cam.read() # 카메라 현재 영상 로드, frame에 저장, ret True/False
    frame = cv2.flip(frame, 0)
    h, w, _ = frame.shape #width, Channel은 불필요
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDateTime = now.strftime('%Y%m%d_%H%M%S') #20210720_164725

    if ret != True: break #ret이 False일 경우

    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10,(h-40)), text='실시간 웹캠: {0}'.format(currDateTime), font = font, fill =(0, 0, 255))
    frame = np.array(frame)

    key = cv2.waitKey(1)
    if key == ord('q'): break #'q' 입력 시 while문 종료
    elif key == ord('c'): #'c' 입력 시 화면캡쳐
        cv2.imwrite('./Capture/img_{0}.png'.format(fileDateTime), frame)
        print('이미지 저장 완료')
    elif key == ord('r') and is_record == False:
        is_record = True
        video = cv2.VideoWriter('./Capture/Record_{0}.avi'.format(fileDateTime), fourcc, 20, (w, h))
        print('녹화 시작')
    elif key == ord('r') and is_record == True:
        is_record = False
        video.release() #객체 해제
        print('녹화 완료')

    if  is_record:
        video.write(frame)
        cv2.circle(img=frame, center=(620,15), radius=5, color=(0, 0, 255), thickness=5)

    cv2.imshow('Real Time',frame) # frame 영상 보여주기

cam.release() #cam 해제
cv2.destroyAllWindows()