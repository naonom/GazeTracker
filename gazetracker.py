import cv2
import GetAngle
import math

class GazeTrack():
    cap: cv2
    getAngle:GetAngle.OpenFaceAngle
    width: int
    height: int
    x: int
    y: int

    def __init__(self):
        self.cap = cv2.VideoCapture(1)
        self.getAngle = GetAngle.OpenFaceAngle()
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.x = self.width//2 - self.width//8
        self.y = self.height//2 - self.height//8

        self.w = self.width//4
        self.h = self.height//4

    def tracking(self, height: int, width: int, dsize: int):
        ret, self.frame = self.cap.read()
        self.getAngle.getDataModel()
        self.getAngle.pickGazeAngleData()
        self.getAngle.AngleToPoint(50)
        self.getAngle.setupPoint()

        self.x = math.floor(self.getAngle.movePointData[0])
        self.y = math.floor(self.getAngle.movePointData[1])

        self.current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)

        cv2.rectangle(self.frame, pt1=(self.x, self.y), pt2=(self.x+self.w,self.y+self.h), color=(0,0,255), thickness=4)

        self.frame = cv2.resize(self.frame, dsize=(dsize, int(600*int(height)/int(width))))
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        #cv2.imshow('frame', frame)

    def endTracking(self):
        self.cap.release()
        cv2.destroyAllWindows()
