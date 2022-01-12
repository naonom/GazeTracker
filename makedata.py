import csv
import subprocess
import os
import datetime

#setting data for txt
#pointing data for csv
class MakeData():
    header: list = ["time", "gaze_x", "gaze_y", "basepoint_x", "basepoint_y",  "showpoint_x", "showpoint_y", "pointing"]

    def __init__(self, filename: str):
        self.filename = filename
        if not os.path.exists("trackingData"):
            os.mkdir("trackingData")

    def makeFile(self):
        subprocess.call(["touch", "trackingData/" + self.filename + ".csv"])

    def openFile(self):
        self.f = open("trackingData/" + self.filename + ".csv", "w")
        self.writer = csv.writer(self.f, lineterminator='\n')
    
    def makeHeader(self):
        self.writer.writerow(self.header)

    def addData(self, gaze_x:float, gaze_y:float, basepoint_x:float, basepoint_y:float, showpoint_x:float, showpoint_y:float, pointing:bool):
        basetime = datetime.datetime.now()
        #basetext = str(basetime.strftime("%Y,%m,%d,%H,%M,%S") + (",") + str(basetime.microsecond) + (",") + str(gaze_x) + (",") + str(gaze_y) + (",") + str(basepoint_x) + (",") + str(basepoint_y) + (",") + str(showpoint_x) + (",") + str(showpoint_y) + (",") + str(int(pointing)) + "\n")

        baselist: list = []
        baselist.append(str(basetime.strftime("%m:%d:%H:%M:%S")) + ":" + str(basetime.microsecond))
        baselist.append(str(gaze_x))
        baselist.append(str(gaze_y))
        baselist.append(str(basepoint_x))
        baselist.append(str(basepoint_y))
        baselist.append(str(showpoint_x))
        baselist.append(str(showpoint_y))
        baselist.append(str(int(pointing)))
        
        self.writer.writerow(baselist)


    def closeFile(self):
        self.f.close()