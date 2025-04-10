import multiprocessing as mp
import multiprocessing.context
import multiprocessing.managers
import os
from abc import *
from queue import Queue

class processImpl(metaclass=ABCMeta):
    def __init__(self,name):
        self.msgQueueList: dict[str, Queue] = dict()
        self.aggQueue: Queue = None
        self.name = name
        self.process = None

    def start(self, proc:multiprocessing.context.Process):
        self.process = proc
        self.process.start()
        self._print('Process started')

    def is_alive(self):
        if self.process is None:
            return False
        else:
            return self.process.is_alive()

    def join(self):
        self.process.join()

    def terminate(self):
        self.process.terminate()

    def run(self):
        self.doProc()
        self.join()
        self.__done()

    def __done(self):
        self._print('Finished Process')

    def getPID(self):
        if self.process is None:
            return os.getpid()
        else:
            return self.process.pid

    def addSubscriber(self, toProc, manager):
        tqueue = manager.Queue()
        self.msgQueueList[toProc.name] = tqueue
        toProc.__addPublisher(self, tqueue)

    def __addPublisher(self, fromProc, queue:Queue):
        self.aggQueue = queue

    def _SendtoAll(self, data):
        for q in self.msgQueueList.values():
            q.put(data)

    def _print(self, data):
        print('[%d-%s] - %s'%(self.getPID(), self.name, data))

    @abstractmethod
    def doProc(self):
        pass