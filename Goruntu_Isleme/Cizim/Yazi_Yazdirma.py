import cv2
import numpy as np


canvas = np.zeros((512,521,3),dtype=np.uint8)+255

font1= cv2.FONT_HERSHEY_COMPLEX_SMALL

cv2.putText(canvas, "OpenCv", (20,150), font1, 5, (0,0,255),cv2.LINE_AA)


cv2.namedWindow("Canvas",cv2.WINDOW_NORMAL)
cv2.imshow("Canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()