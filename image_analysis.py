import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from time import sleep

from datetime import datetime

def main():
    out_path = ""
    path = ""

    for image_path in os.listdir(path):
        input_path = os.path.join(path, image_path)
        print(input_path)
        current_dt = datetime.now()
        current_dt_string = current_dt.strftime("%Y.%m.%d_%H.%M.%S.jpg")

        cell_image = cv2.imread(input_path, 0)
        regular_cell_image = cell_image
        cell_image = cv2.bitwise_not(cell_image)
        blur = cv2.GaussianBlur(cell_image, (0,0), sigmaX=3.5, sigmaY=3.5)

        thresh, bw = cv2.threshold(cell_image, 1, 255, cv2.THRESH_OTSU)

        wb = cv2.bitwise_not(bw)

        params = cv2.SimpleBlobDetector_Params()

        params.minThreshold = 0
        params.maxThreshold = 255

        params.filterByColor = True
        params.blobColor = 0

        params.filterByArea = True
        params.minArea = 25

        params.filterByCircularity = True
        params.minCircularity = 0.2

        params.filterByConvexity = True
        params.minConvexity = 0.2

        params.filterByInertia = True
        params.minInertiaRatio = 0.2

        params.minDistBetweenBlobs = 30

        detector = cv2.SimpleBlobDetector_create(params)

        keypoints = detector.detect(blur)

        keypoint = cv2.drawKeypoints(bw, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        number_of_blobs = len(keypoints)
        text = "Total Cell Count: " + str(len(keypoints))
        cv2.putText(keypoint, text, (360, 490), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

        cv2.imwrite(os.path.join(out_path , current_dt_string), keypoint)
        sleep(2)

if __name__ == '__main__':
    main()