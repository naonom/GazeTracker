from typing import List
#import GetDataModel

class CSVPresenter():
    beforeGazeAngle: List[float] = [0.0, 0.0]
    isFaceSuccess: bool
    #model = GetDataModel.CSV()

    def __init__(self) -> None:
        ifFaceSuccess = False
        pass

    def pickFace(list):
        try:
            #date = model.gazeData()
            if list[4] == '1':
                isFaceSuccess = True
            else:
                isFaceSuccess = False
        except:
            print('openface failure')
            isFaceSuccess = False
    
    