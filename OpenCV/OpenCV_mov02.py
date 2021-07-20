import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw

#카메라 기본 프레임
cam = cv2.VideoCapture(0) # cam 열기, 번호 0 ~ 
cam.set(cv2.CAP_PROP_FRAME_WIDTH,640) # 크기 조절
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while True:
    ret, frame = cam.read() # 카메라 현재 영상 로드, frame에 저장, ret True/False
    
    if ret != True: break #ret이 False일 경우

    frame = cv2.flip(frame, 0)
    cv2.imshow('Real Time',frame) # frame 영상 보여주기
    
    if cv2.waitKey(1) == ord('q'): break #'q' 입력 시 while문 종료
        
cam.release() #cam 해제
cv2.destroyAllWindows()