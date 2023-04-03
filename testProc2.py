from time import sleep
from multiprocessing import current_process

from main import processImpl


class testProc2(processImpl):
    def __init__(self, name):
        super().__init__(name)

    def doProc(self):
        self._print('Start Process ------- %s' % self.name)
        n = 1
        while (True):
            print(current_process().pid, n, self.name)
            sleep(1)
            n += 1
            if n>15:
                print('finished', current_process().name)
                self.terminate()
