refreshTime = 0.2

dataSaved = 0

x = 1 / refreshTime # 5 datos que conforman un segundo

data_prom = 0
data_sum = 0

YES = []
data = 1

calculando = True
while True:
    if calculando:
        if dataSaved < x:
            data = input()
            dataSaved = dataSaved+1
            data_sum = data_sum + int(data)
        else:
            calculando = False
    else:
        data_prom = data_sum/x
        YES.append(data_prom)
        dataSaved=0
        data_sum = 0
        calculando = True
        print(YES)




xMinAccelerationGraph = 0
        xMaxAccelerationGraph = SamplesAcceleration - 1
        yMinAccelerationGraph = limitsAccelerationMin
        yMaxAccelerationGraph = limitsAccelerationMax

self.accelerationGraph = plt.figure()
        self.accelerationAxes = plt.axes(xlim=(xMinAccelerationGraph, xMaxAccelerationGraph),
                                         ylim=(yMinAccelerationGraph, yMaxAccelerationGraph))

[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0]