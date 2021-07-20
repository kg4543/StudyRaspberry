import cv2
import numpy as np
from numpy.core.fromnumeric import shape

org = cv2.imread('./Capture/minion.jpg', cv2.IMREAD_REDUCED_COLOR_2) #color or 흑백 및 사이즈 조전 
cv2.imshow('Origin', org)


h, w, c = org.shape
#noise = np.uint8(np.random.normal(loc=0, scale=80, size=[h, w, c]))
#noised_img = cv2.add(org, noise) # 원본 이미지에 노이즈 추가
#cv2.imshow('Noise', noised_img)

gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
#enhanced = cv2.equalizeHist(gray)
#cv2.imshow('Enhance', enhanced)

ret, bny = cv2.threshold(gray, 127, 255, 0)
cont, hirc = cv2.findContours(bny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cont2, hirc = cv2.findContours(bny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(org, cont2, 0, (0, 255, 0), 2)
cv2.imshow('Result', org)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제