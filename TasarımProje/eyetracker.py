import cv2
cascade_face = cv2.CascadeClassifier('D:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
cascade_eye =  cv2.CascadeClassifier('D:\opencv\sources\data\haarcascades\haarcascade_eye.xml')
cascade_smile = cv2.CascadeClassifier('D:\opencv\sources\data\haarcascades\haarcascade_smile.xml')

def eyetrack(grayscale,img):
    face= cascade_face.detectMultiScale(grayscale, 1.3, 5)
    for(x_face, y_face, w_face, h_face) in face:
        ri_grayscale = grayscale[y_face:y_face+h_face, x_face:x_face+w_face]
        eye = cascade_eye.detectMultiScale(ri_grayscale, 1.2, 18) 
        for (x_eye, y_eye, w_eye, h_eye) in eye:
            roi=img[x_eye:x_eye+w_eye , y_eye:y_eye+h_eye]    
            rows, cols,_= roi.shape   
            gray_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
            gray_roi = cv2.GaussianBlur(gray_roi,(7,7),0)
            _, threshold = cv2.threshold(gray_roi, 5, 255, cv2.THRESH_BINARY_INV)
            contours,hierachy=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            for cnt in contours:
             (x, y ,w ,h) = cv2.boundingRect(cnt)
    
             #cv2.drawContours(img, [cnt], -1,(0,0,255),3) #yuvarlak
             #cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)#göz bebeğğine dikdörtgen mavi
             #cv2.line(img, (x+ int(w/2),0),(x+ int(w/2),rows),(0,255,0),2) #ekran ortasından çizgi
             #cv2.line(img,(0, y+ int(h/2)),(cols,y+ int(h/2)),(0,255,0),2)# ekran yatay çizgi
             #cv2.imshow("Threshold",threshold)
             #cv2.imshow("gray_roi",gray_roi)
             #cv2.imshow("Roi",roi)
             # aldığımı odaklama problemlerinden ötürü göz takip sisteminde sorunu çözemedik o yüzden şuan temelde çalışsa da maalesef sorunlu bu kısım
    return contours            
             
    
    



