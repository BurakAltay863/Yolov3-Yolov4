# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:53:52 2022
@author: BurakPC
"""
#%% 1.Bolum
import  cv2
import numpy as np

img = cv2.imread("images/people.jpg")
#print(img)
# consolda img.shape resmin boyuntlarını bıze verır

img_width = img.shape[1]
img_height= img.shape[0]

#%% 2.Bolum
# blob işlemi yapıyoruz == resmi 4 boyutlu tensorlere cevırme:1/255 sabit sayı 
# blobun kaca kaclık olması gerektıgını gırıyoruz model nasıl egıtılmısse o deger gırılır
# swapRB resmi rgb formata donusturur
# crop kırma ıslemı
img_blob = cv2.dnn.blobFromImage(img,1/255,(416,416),swapRB=True,crop=False)

# tanınacak nesneler girilir
labels = ["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat",
                    "trafficlight","firehydrant","stopsign","parkingmeter","bench","bird","cat",
                    "dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack",
                    "umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sportsball",
                    "kite","baseballbat","baseballglove","skateboard","surfboard","tennisracket",
                    "bottle","wineglass","cup","fork","knife","spoon","bowl","banana","apple",
                    "sandwich","orange","broccoli","carrot","hotdog","pizza","donut","cake","chair",
                    "sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse",
                    "remote","keyboard","cellphone","microwave","oven","toaster","sink","refrigerator",
                    "book","clock","vase","scissors","teddybear","hairdrier","toothbrush"]
# her bir label icin renk tanımladık
colors = ["0,255,255","0,0,255","255,0,0","255,255,0","0,255,0"]
# tum renklerı dolasıp tek bır arrayde topladık
colors=[np.array(color.split(",")).astype("int")for color in colors ]
colors = np.array(colors)
# renk verimizi buyutmek icin
colors=np.tile(colors,(18,1))
#%% 3.Bolum
# modelimizi olusturduk
model = cv2.dnn.readNetFromDarknet("C:/Users/BurakPC/Desktop/YOLO/model_pretrained/yolov3.cfg","C:/Users/BurakPC/Desktop/YOLO/model_pretrained/yolov3.weights")
# model icindeki tum layerlerı cektık
layers = model.getLayerNames()
# output layerlerımızı belırlıyoruz.
output_layer = [layers[layer - 1] for layer in model.getUnconnectedOutLayers()]
# tensoru modele veriyoruz. 
model.setInput(img_blob)
# detection=tespit etme layersda outputlayerdekı sayıları ıncelıyoruz.
detection_layers = model.forward(output_layer)
#%% 4.Bolum
for detection_layers in detection_layers:
    for object_detection in detection_layers:
        
        scores = object_detection[5:]
        # predicted_id=tahmin edilen nesne
        predicted_id = np.argmax(scores)
        # confidence = guven skoru
        confidence = scores[predicted_id]
        
        if confidence > 0.20:
            label = labels[predicted_id]
            bounding_box=object_detection[0:4] * np.array([img_width,img_height,img_width,img_height])
            (box_center_x, box_center_y , box_width, box_height)= bounding_box.astype("int")
            # dikdortgenın baslancıg ve bıtıs noktalarını belırtıyoruz.
            start_x = int(box_center_x - (box_width/2))
            start_y = int(box_center_y - (box_height/2))
            
            end_x = start_x + box_width
            end_y = start_y + box_height
            
            box_color=colors[predicted_id]
            box_color=[int(each) for each in box_color]
            # degerlerı consoleda gormek ıcın
            label = "{}: {:.2f}%".format(label, confidence*100)
            print("predicted object {}".format(label))
            # bounding_box ı cızdırme
            cv2.rectangle(img, (start_x,start_y),(end_x,end_y) , box_color,1)
            # labelı yazdırma
            cv2.putText(img,label, (start_x,start_y-10), cv2.FONT_HERSHEY_SIMPLEX,0.5,box_color,1)
            
cv2.imshow("Detection Window", img)            
            
            
            