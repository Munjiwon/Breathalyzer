from multiprocessing import current_process
from time import sleep

from main import processImpl


class nameProc(processImpl): #name은 프로세스 이름넣을것
    def __init__(self, name):
        super().__init__(name)

    def doProc(self):
        #이 부분에 코드 작성하면 됨