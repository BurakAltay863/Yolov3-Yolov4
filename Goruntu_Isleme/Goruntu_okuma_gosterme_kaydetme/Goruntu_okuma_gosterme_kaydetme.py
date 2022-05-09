import cv2
#resmi okumak icin
#resmi gri tonlarda okutmak için ,
#img = cv2.imread("proje.png",cv2.IMREAD_GRAYSCALE) veya img = cv2.imread("proje.png",0)
img = cv2.imread("C:/Users/BurakPC/Desktop/Goruntu_Isleme/Goruntu_okuma_gosterme_kaydetme/aaa.jpg")
#print(img)
#pencereyi buyutup kucultmek ıcın
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
#resimleri gosterme ilk parametre resmi gosterilecek pencerenin adı
#ikinci parametre resmin tutuldugu degısken
cv2.imshow("image",img)
#resimleri kaydetme
cv2.imwrite("proje1.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
##Burak Altay

