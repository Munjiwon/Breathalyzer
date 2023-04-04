from multiprocessing import current_process
from time import sleep

from main import processImpl


class cameraProc(processImpl):
    def __init__(self, name):
        super().__init__(name)

    def doProc(self):
        self._print('Start Process ------- %s' % self.name)
        import cv2
        import datetime

        duration = 300
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        filename = f"video_{current_time}.avi"

        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        fps = int(cap.get(5))

        out = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))

        start_time = datetime.datetime.now()
        while (datetime.datetime.now() - start_time).seconds < duration:
            ret, frame = cap.read()
            if ret == True:
                out.write(frame)
            else:
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
