import cv2

cap=cv2.VideoCapture(r'C:\Users\DELL\Videos\abc.avi')

faceCascade=cv2.CascadeClassifier(r'C:\Users\DELL\Downloads\opencv\sources\data\haarcascades\haarcascades_fullbody.xml")

while True:
    success,frame=cap.read()
    
    imgGrey = cv2.cvtColor(frame,cv2.COLOR_RGBGRAY)
    
    faces = faceCascade.detectMultiScale(imgGrey,1,1,4)
    
    for(x,y,w,b) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv2.imgshow("Video",frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()