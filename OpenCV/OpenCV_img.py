import cv2
import numpy as np
from numpy.core.fromnumeric import shape

org = cv2.imread('./Capture/minion.jpg', cv2.IMREAD_REDUCED_COLOR_2) #color or 흑백 및 사이즈 조전 
cv2.imshow('Origin', org) #cv2 새창알림

gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY) #흑백

#h, w, c = org.shape
#cropped = gray[int(h/6):,int(w/5):int(w/2)] #이미지 자르기 [배열]
#cv2.imshow('Cropped', cropped) 

#print('Width:{0}, Height:{1}, Channel:{2}'.format(w, h, c))
#size_small = cv2.resize(gray, dsize=(w/2, h/2))
#cv2.imshow('Resize', size_small) #이미지 반으로 줄임

blur = cv2.blur(org,(10,10)) #2,2보다 10,10이 훨씬 흐릿
cv2.imshow('Blur', blur)

kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])
sharp = cv2.filter2D(org, -1, kernel)
cv2.imshow('Sharp', sharp)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제