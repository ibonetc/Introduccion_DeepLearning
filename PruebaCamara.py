# -*- coding: utf-8 -*-


#conda install -c menpo opencv
#pip install opencv-python

import cv2 # opencv

########Probar cámara
video_capture = cv2.VideoCapture(0)
while(True):
    ret, frame = video_capture.read()
    cv2.imshow('frame', frame)  # Mostrar el frame capturado con la cámara
    if cv2.waitKey(1) & 0xFF == 27: #detener con tecla Esc
        break
video_capture.release()
cv2.destroyAllWindows()

