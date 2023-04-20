import time

from procImpl import processImpl


class testPublisher(processImpl):
    def __init__(self, name):
        super().__init__(name)

    def doProc(self):
        a = 0
        while True:
            self._SendtoAll(a)
            a+=1
            time.sleep(1)