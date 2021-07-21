#영상 움직임 감지
import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image
from numpy.core.fromnumeric import shape

## 함수 선언
## 영상 간의 차이나는 부분 표시이미지, 차이나는 픽셀 갯수 리턴함수

def get_diff_image(frame_a,frame_b,frame_c,threshold):
    #세개 모든 프레임을 회색으로 전환
    frame_a_gray = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    frame_b_gray = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    frame_c_gray = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

    # a/b 사이 영상 차이값, b/c 사이 영상 차이 값 구함
    diff_ab = cv2.absdiff(frame_a_gray, frame_b_gray) # None
    diff_bc = cv2.absdiff(frame_b_gray, frame_c_gray) # 차이값 발생 or None

    # 영상 차이값이 40이상이면 값을 흰색으로 바꿔줌
    ret, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)
    ret, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)

    # 두 영상에서 공통된 부분은 1로 만듬
    diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)
    # 영상에서 1이 된 부분 확장 (mirphology)
    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

    diff_cnt =cv2.countNonZero(diff)

    return diff, diff_cnt


#카메라 기본 프레임
cam = cv2.VideoCapture(0) # cam 열기, 번호 0 ~ 
cam.set(cv2.CAP_PROP_FRAME_WIDTH,640) # 크기 조절
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

#나눔고딕볼트 로드
font = ImageFont.truetype('./Fonts/NanumGothicBold.ttf', 20)
# 영상 저장 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
is_record = False

threshold = 40 # 영상 차이가 나는 threshold 설정
diff_max = 10 # 영상 차이가 나는 최대 픽셀 수

#초기 프레임
ret, frame_a = cam.read()
frame_a = cv2.flip(frame_a, 0)
ret, frame_b = cam.read()
frame_b = cv2.flip(frame_b, 0)

while True:
    # 현재 시간
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDateTime = now.strftime('%Y%m%d_%H%M%S') #20210720_164725
    
    # 카메라 현재 영상 로드
    ret, frame = cam.read()
    frame = cv2.flip(frame, 0)
    h, w, _ = frame.shape #width, Channel은 불필요

    if ret != True: break #ret이 False일 경우

    #현재 영상과 초기영상 비교
    diff, diff_cnt = get_diff_image(frame_a = frame_a, frame_b = frame_b, frame_c = frame, threshold = threshold)

    # 차이가나는 이미지 갯수가 10개 이상이면 움직임 발생했다고 판단
    if (diff_cnt > diff_max):
        #cv2.imwrite('./Capture/img_{0}.png'.format(fileDateTime), frame)
        print('움직임 발생 : 캡쳐 완료')

    # 움직임 결과 영상
    cv2.imshow('Diff Result', diff)

    frame_a = np.array(frame_b) #이전 화면 이전
    frame_b = np.array(frame) #현재 화면 이전

    #화면에 시간 출력
    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10,(h-40)), text='실시간 웹캠: {0}'.format(currDateTime), font = font, fill =(0, 0, 255))
    frame = np.array(frame) # 원상태 복귀

    key = cv2.waitKey(1)
    if key == ord('q'): break #'q' 입력 시 while문 종료
    
    cv2.imshow('Real Time',frame) # frame 영상 보여주기

cam.release() #cam 해제
cv2.destroyAllWindows()