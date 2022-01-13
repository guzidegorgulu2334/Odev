import detectation
import cv2





vc = cv2.VideoCapture(0)
while True:
    _, img = vc.read() 
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    img = detectation.detection(grayscale, img)
    
    
    cv2.imshow('img', img) 
     
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
vc.release() 
cv2.destroyAllWindows()
