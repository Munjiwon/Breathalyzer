from multiprocessing import current_process
from time import sleep

from procImpl import processImpl


class testProc1(processImpl):
    def __init__(self, name):
        super().__init__(name)

    def doProc(self):
        self._print('Start Process ------- %s' %self.name)
        n = 1
        while (n<30):
            print(current_process().pid, n, self.name)
            sleep(1)
            n += 1
