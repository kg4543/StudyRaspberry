import cv2
import numpy as np

org = cv2.imread('./Capture/minion.jpg')
#org = cv2.imread('./Capture/minion.jpg', cv2.IMREAD_GRAYSCALE) #흑백사진
dst = cv2.resize(org, dsize=(480,240))

center = [255, 50] # x,y
color = (0,0,255) #red

cv2.circle(dst, tuple(center), 45, color)
cv2.rectangle(dst, (120,50),(210,130), (255,0,0))

cv2.imshow("origin", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()