import multiprocessing as mp
import time
from multiprocessing import current_process

import self as self

from procImpl import processImpl
from proc_FaceRecognition import faceProc
from proc_camera import cameraProc
from proc_testProc import testProc
from proc_testPub import testPublisher
from testProc1 import testProc1
from testProc2 import testProc2


class SystemManager(processImpl):
    def __init__(self, manager, isDebug=False):
        super().__init__('SystemManager')
        self.DebugMode = isDebug
        self.dataManager = manager
        self.processItems: dict[str, processImpl] = dict()

        self.constructProcess()


    def constructProcess(self):
        if self.DebugMode is True:
            self._print('Debug Mode has been started..')
            # create processes
            test_proc = testProc1('test1')
            test2_proc = testProc2('test2')

            # add process
            self.addProcess(test_proc)
            self.addProcess(test2_proc)

            # pub_proc = testPublisher('testPublisher')
            # subtest_proc = testProc('test1')
            # subtest2_proc = testProc('test2')
            #
            # # process aggregation
            # pub_proc.addSubscriber(test_proc, self.dataManager)
            # pub_proc.addSubscriber(test2_proc, self.dataManager)
            # print(pub_proc.msgQueueList)
            #
            # self.addProcess(pub_proc)
            # self.addProcess(subtest_proc)
            # self.addProcess(subtest2_proc)


        else:
            camera_proc = cameraProc('Camera')
            face_proc = faceProc('Face')

            self.addProcess(camera_proc)
            self.addProcess(face_proc)

    def doProc(self):
        self.__startChildProcess()

        loop_f = True
        while loop_f:
            try:
                time.sleep(5)
            except KeyboardInterrupt:
                print('?????')
                loop_f = False
            self._print('checking Process alive test')
            self.printProcessStatus()
            self.__startChildProcess()


    def __startChildProcess(self):
        # process start
        self._print('Starting Child Processes')
        for val in self.processItems.values():
            if val.is_alive() is False:
                p = mp.Process(target=val.run, name=val.name)
                val.start(p)

    def __restartAllChildProcesses(self):
        #delete all process list
        self.terminateAllProcess()
        time.sleep(1)
        self.__startChildProcess()

    def getProcess(self):
        return self.processItems

    def addProcess(self, proc:processImpl):
        self.processItems[proc.name] = proc

    def terminateAllProcess(self):
        for val in self.processItems.values():
            val.terminate()
            self._print('%15s(%5d) has been terminated' % (val.name, val.getPID()))

    def printProcessStatus(self):
        for key, val in self.processItems.items():
            self._print("[key : %15s] [pid : %5d] [status : %5s]"%(key, val.getPID(), val.is_alive()))

if __name__ == '__main__':
    sm = SystemManager(mp.Manager(), isDebug=True)
    sm.run()