import cv2
import numpy as np

#canvas yerine img de yazabılırdık
#siyah beyyaz yapmak ıcın
canvas = np.zeros((10,10),np.uint8)
canvas[0,0]= 255
canvas[0,1]= 200
canvas[0,2]= 100
canvas[0,3]= 50
canvas[0,9]=58
#renkli bir tablo olustuurup kendımız renklerı eklemek ıcın


"""
img = np.zeros((10,10,3),np.uint8)

canvas[0,0]= (255,255,50)
canvas[0,1]= (255,255,100)
canvas[0,2]= (255,255,150)
canvas[0,3]= (255,255,200)"""
#tablomuzun boyunu buyultmek ıcın
canvas = cv2.resize(canvas, (1000,1000), interpolation=cv2.INTER_AREA)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()