import time


def bubbleSort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                drawData(data)
                time.sleep(timeTick)
