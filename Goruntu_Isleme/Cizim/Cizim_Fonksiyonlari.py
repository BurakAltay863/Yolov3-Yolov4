import cv2
import numpy as np

#ekranı full beyaz yapmak ıcın
#♠canvas tual olusturmak ıcın kullanılır
canvas = np.zeros((512,521,3),dtype=np.uint8)+255

#çizgi cizmek icin
cv2.line(canvas, (50,50),(512,512), (255,0,0) , thickness=5 )
cv2.line(canvas, (100,50),(200,2500), (0,0,255) , thickness=7 )

#dikdortgen cizmek için 
#ici dolu dıkdortgen icin thıcknes degeri -1
cv2.rectangle(canvas,(20,20), (50,50), (0,255,0),thickness=3)
cv2.rectangle(canvas,(50,50), (150,150), (0,0,255),thickness=-1)

#cember cizme
cv2.circle(canvas,(250,250),100,(0,0,255),-1)

#ücgen cızme
p1=(100,200)
p2=(50,50)
p3=(300,100)

cv2.line(canvas, p1, p2, (0,0,0),4)
cv2.line(canvas, p2, p3, (0,0,0),4)
cv2.line(canvas, p3, p1, (0,0,0),4)

#♦dıger geometrık sekıller ıcın
points= np.array([[[110,200],[300,200],[290,220],[220,250]]],np.int32)

cv2.polylines(canvas,[points],True,(0,0,100),5)

#elips çizmek icin

cv2.ellipse(canvas, (300,300), (80,20), 10, 90, 360, (255,255,0),-1)
cv2.namedWindow("Canvas",cv2.WINDOW_NORMAL)
cv2.imshow("Canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()

#ekranı full sıyah yapmak ıcın
"""canvas = np.zeros((512,521,3),dtype=np.uint8)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()"""