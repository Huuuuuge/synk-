import cv2
import mediapipe as mp
import math

class poseDetector() :
    
    def __init__(self, mode=False, complexity=1, smooth_landmarks=True,
                 enable_segmentation=False, smooth_segmentation=True,
                 detectionCon=0.5, trackCon=0.5):
        
        self.mode = mode 
        self.complexity = complexity
        self.smooth_landmarks = smooth_landmarks
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complexity, self.smooth_landmarks,
                                     self.enable_segmentation, self.smooth_segmentation,
                                     self.detectionCon, self.trackCon)
        
        
    def findPose (self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        return img
    
    def findPosition(self, img):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                #finding height, width of the image printed
                h, w, c = img.shape
                #Determining the pixels of the landmarks
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
        return self.lmList
        
    def findAngle(self, img, p1, p2, p3):   
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        angle = math.degrees(math.atan2(y3-y2, x3-x2) - 
                             math.atan2(y1-y2, x1-x2))
        if angle < 0:
            angle += 360
            if angle > 180:
                angle = 360 - angle
        elif angle > 180:
            angle = 360 - angle
        return angle
        

def main():
    detector = poseDetector()
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, img = cap.read()
        if ret:    
            img = detector.findPose(img)
            cv2.imshow('Pose Detection', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()