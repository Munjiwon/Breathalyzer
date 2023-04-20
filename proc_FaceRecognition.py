from procImpl import processImpl


class faceProc(processImpl):
    def __init__(self, name):
        super().__init__(name)

    def doProc(self):
        self._print('Start Process ------- %s' % self.name)
        import cv2
        import time
        import face_recognition

        def capture_image(filename, delay=2):
            cap = cv2.VideoCapture(0)
            time.sleep(delay)
            ret, frame = cap.read()

            if ret:
                cv2.imwrite(filename, frame)

            cap.release()

        capture_image('image1.jpg')
        time.sleep(30)
        capture_image('image2.jpg')

        # 얼굴이 탐지된 경우 첫 번째 이미지를 로드하고 얼굴 인코딩을 가져온다
        image1 = face_recognition.load_image_file("image1.jpg")
        face_encodings1 = face_recognition.face_encodings(image1)

        if face_encodings1:
            face_encoding1 = face_encodings1[0]
        else:
            print("No face detected in image1.jpg")
            exit()
        
        # 얼굴이 탐지된 경우 두 번째 이미지를 로드하고 얼굴 인코딩을 가져온다
        image2 = face_recognition.load_image_file("image2.jpg")
        face_encodings2 = face_recognition.face_encodings(image2)

        if face_encodings2:
            face_encoding2 = face_encodings2[0]
        else:
            print("No face detected in image2.jpg")
            exit()

        # 얼굴 인코딩을 비교하고 동일한 사람인지 확인
        result = face_recognition.compare_faces([face_encoding1], face_encoding2)

        if result[0]:
            print("True")
        else:
            print("False")