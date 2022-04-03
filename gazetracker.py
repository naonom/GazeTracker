import cv2
import GetAngle
import math
import os
import time

class GazeTrack():
    cap: cv2
    getAngle:GetAngle.OpenFaceAngle
    width: int
    height: int
    x: int
    y: int
    xCenter: int
    yCenter: int

    def __init__(self, cameraid: int):
        self.cap = cv2.VideoCapture(cameraid)
        self.getAngle = GetAngle.OpenFaceAngle()
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.x = 0
        self.y = 0
        self.w = self.width//5
        self.h = self.height//5
        self.xRectCenter = self.width//2 - self.width//10
        self.yRectCenter = self.height//2 - self.height//10
        #self.takePhoto()

        self.xCenter = 0
        self.yCenter = 0

    def toCenter(self):
        #self.xCenter = math.floor(self.getAngle.movePointData[0] + self.width//2 + self.w)
        #self.yCenter = math.floor(self.getAngle.movePointData[1] - self.height//2 + self.h//2)
        self.xCenter = math.floor(self.getAngle.movePointData[0])
        self.yCenter = math.floor(self.getAngle.movePointData[1])

    def tracking(self, height: int, width: int, dsize: int, distance: int ,xdis: float, ydis: float):
        ret, self.frame = self.cap.read()
        self.getAngle.getDataModel()
        self.getAngle.pickGazeAngleData()
        self.getAngle.AngleToPoint()
        self.getAngle.setupPoint(dis=distance, xdis=xdis, ydis=ydis)

        self.x = math.floor(self.getAngle.movePointData[0])
        self.y = math.floor(self.getAngle.movePointData[1])

        self.current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)

        self.norectframe = self.frame
        self.norectframe = cv2.cvtColor(self.norectframe, cv2.COLOR_BGR2RGB)

        self.xTrack: int = self.x - self.xCenter + self.xRectCenter
        self.yTrack: int = self.y - self.yCenter + self.yRectCenter
        xRect: int = self.xTrack + self.w
        yRect: int = self.yTrack + self.h
        #print(xTrack, yTrack, xRect, yRect)
        cv2.rectangle(self.frame, pt1=(self.xTrack, self.yTrack), pt2=(xRect, yRect), color=(0,0,255), thickness=4)
        self.outputframe = self.frame
        self.outputframe = cv2.cvtColor(self.outputframe, cv2.COLOR_BGR2RGB)

        self.frame = cv2.resize(self.frame, dsize=(dsize, int(dsize*int(height)/int(width))))
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)


    def endTracking(self):
        self.cap.release()
        cv2.destroyAllWindows()
