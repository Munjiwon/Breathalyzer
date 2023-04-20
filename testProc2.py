from time import sleep
from multiprocessing import current_process

from procImpl import processImpl


class testProc2(processImpl):
    def __init__(self, name):
        super().__init__(name)

    def doProc(self):
        self._print('Start Process ------- %s' % self.name)
        n = 100
        while (n>70):
            print(current_process().pid, n, self.name)
            sleep(1)
            n -= 1

