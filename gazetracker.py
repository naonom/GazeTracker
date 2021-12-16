import cv2
import GetAngle
import math

def main():
    cap=cv2.VideoCapture(2)
    getAngle = GetAngle.OpenFaceAngle()
    print("main")
    width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    x:int = width//2 - width//8
    y:int = height//2 - height//8

    w = width//4
    h = height//4

    while True:
        ret, frame = cap.read()
        updata(getAngle = getAngle)
        x += math.floor(getAngle.movePointData[0])
        y += math.floor(getAngle.movePointData[1])
        cv2.rectangle(frame, (x,y), (x+w, y+h), color=(0,0,255),thickness= 4)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def updata(getAngle: GetAngle.OpenFaceAngle()):
    getAngle.getDataModel()
    getAngle.pickGazeAngleData()
    getAngle.AngleToPoint(50)
    getAngle.setupPoint()
    #getAngle.movePointLimit()
    #print(getAngle.movePointData[0])

if __name__ == "__main__":
    main()