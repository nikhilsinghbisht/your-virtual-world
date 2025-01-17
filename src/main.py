import cv2
import mediapipe as mp
import time
import subprocess
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    time.sleep(5)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for L_id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) 
        print("Person with hands!")
        cap.release()
        cv2.destroyAllWindows()
        subprocess.run(["python","gp.py"])
        break
          
        
    else:
        print("Person without hands!")
        cap.release()
        cv2.destroyAllWindows()
        subprocess.run(["python","Nova.py"])
        
        
    #cTime = time.time()
    #fps = 1 / (cTime - pTime)
    #pTime = cTime
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()