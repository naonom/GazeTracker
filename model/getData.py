from sys import stdin

class CSV:
    beforeGazeAngle = [0.0, 0.0]
    
    def __init__(self):
        pass

    #get data row
    def Row(self):
        try:
            rowline = stdin.readline()
            row = rowline.split(',')
            print(row)
        except:
            print('row error')

    #get face data
    def gazeData(self):
        try:
            line = stdin.readline()
            baseData = line.split(',')
            if baseData[4] == '1': #get face data
                return baseData
            else:
                fake = []
                for i in range(497):
                    fake.append('0')
                return fake
        except:
            print('openface failure')
            fake = []
            for i in range(497):
                fake.append('0')
            return fake

    #get date from csv
        def getData(baseData):
            try:
                if baseData[4] == '1': #Openface success
                    return baseData
                else:
                    print('Openface failure')
                    return fakeData(497)
			        
            except:
                print('Can not get baseDate')
                return fakeData(497)

            def  fakeData(num):
                fake = []
                for i in range(num):
                    fake.append('0')
                return fake
		             