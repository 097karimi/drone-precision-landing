import cv2 as cv
import time
from func import *

cap = cv.VideoCapture(0)

while cap.isOpened():
    tmp = time.time()

    _, frame = cap.read()

    (corners, ids, rejected_area) = cv.aruco.detectMarkers(
        frame,
        cv.aruco.Dictionary_get(cv.aruco.DICT_ARUCO_ORIGINAL),
        parameters=cv.aruco.DetectorParameters_create()
        )

    cv.aruco.drawDetectedMarkers(frame, corners, borderColor=(0, 0, 255))
    
    if len(corners) >0:
        one, two, three, four = points_for_draw(corners)
        coloring(frame, one, two, three, four)
    
    error_x, error_y = estimate_error(*center_of_aruco(corners), *center_of_camera(cap))
    
    show_on_screen(
        frame,
        {
            'Error-X': error_x,
            'Error-Y': error_y,
        }
    )

    cv.circle(frame, center_of_aruco(corners), 7, (0, 255, 0), -1)
    cv.circle(frame, center_of_camera(cap), 7, (0, 0, 0), -1)
    

    show_on_screen(
        frame,
        {
            'TPF : ': time.time() - tmp,
        },
        120
    )

    
    cv.namedWindow("ArUco", cv.WINDOW_GUI_NORMAL)
    cv.imshow("ArUco", frame)

    if cv.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
