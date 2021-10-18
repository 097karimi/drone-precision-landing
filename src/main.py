import cv2 as cv
import time
from vision import Vision
import time

vision = Vision(0)

while True:
    vision.detect_markers()
    x,y = vision.estimate_error()
    vision.show_text_on_screen({
        'Error x':x,
        'Error y': y
        })
    vision.show_window()
    if cv.waitKey(100) & 0xFF == ord('q'):
        del vision
        break