import cv2
#Goruntuyu alacagımız yere gore icerideki sayıyı degıstırırız
#eger hahazırda bir videomuz varsa o vıdeonun adresını yapıstırırız
#webcam
#cap = cv2.VideoCapture(0)
#video dosyası
cap = cv2.VideoCapture("Nargile.mp4")
#videoları bir butun olarak okuyup gostermek ıcın whıle dongusu kullanırız.
while True:
    
    ret, frame = cap.read()
    #2 degısken verıyoruz ret degerı dogruysa frameler dogru okunmustur
    #if ret ==0 videonun bıtımini ogrenmek için
    if ret == 0:
        break
    #frame= cv2.flip(frame, 1)
    #video fotograf yonunu degıstırme icin
    cv2.imshow("Nargile", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        #her bır framı 25 ms goster ve q ya basarsam cık
        break

cap.release() 
cv2.destroyAllWindows()   