import cv2 as cv


class Vision:
    def __init__(self,cam=0):
        self.__cam = cam
        self.__cap = cv.VideoCapture(self.__cam)

    def __del__(self):
        self.__cap.release()
        cv.destroyAllWindows()

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__cam})'

    def detect_markers(self ,cam=0):
        if self.__cap.isOpened():

            _, self.__frame = self.__cap.read()

            (self.__corners, self.__ids, self.__rejected_area) = cv.aruco.detectMarkers(
                self.__frame,
                cv.aruco.Dictionary_get(cv.aruco.DICT_ARUCO_ORIGINAL),
                parameters=cv.aruco.DetectorParameters_create()
                )

            cv.aruco.drawDetectedMarkers(self.__frame, self.__corners, borderColor=(0, 0, 255))


    def center_of_aruco(self):
        if self.__corners == []:
            return (0,0)
        for corner in self.__corners:
            x = (corner[0][0][0] + corner[0][1][0] + corner[0][2][0] + corner[0][3][0]) / 4
            y = (corner[0][0][1] + corner[0][1][1] + corner[0][2][1] + corner[0][3][1]) / 4
        return (int(x), int(y))


    def center_of_camera(self):
        x = int(self.__cap.get(cv.CAP_PROP_FRAME_WIDTH)/2)
        y = int(self.__cap.get(cv.CAP_PROP_FRAME_HEIGHT)/2)
        return (x, y)

    def cam_resolution(self):
        x = int(self.__cap.get(cv.CAP_PROP_FRAME_WIDTH))
        y = int(self.__cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        return (x, y)


    def estimate_error(self):
        ar_x, ar_y = self.center_of_aruco()
        cam_x, cam_y = self.center_of_camera()
        x = int(ar_x) - cam_x
        y = (int(ar_y) - cam_y) * -1
        return (x, y)


    def show_text_on_screen(self, lable_text_dict, axix_y=20):
        for k, v in lable_text_dict.items():
            cv.putText(self.__frame, str(k), (10, axix_y),
            cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            cv.putText(self.__frame, str(v), (90, axix_y),
            cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            axix_y += 20

    def draw_circle(self, x,y):
        cv.circle(self.__frame, (x, y), 7, (0, 255, 0), -1)


    def show_window(self):
        cv.namedWindow("ArUco", cv.WINDOW_GUI_NORMAL)
        cv.imshow("ArUco", self.__frame)
        
    

        

