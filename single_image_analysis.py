import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

from datetime import datetime

def single_image_analysis():
    current_dt = datetime.now()
    timestamp_string = current_dt.strftime("%Y.%m.%d %H.%M.%S")
    current_dt_string = current_dt.strftime("%Y.%m.%d_%H.%M.%S.jpg")

    cell_image = cv2.imread("img.tiff", 0)
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

    keypoint = cv2.drawKeypoints(wb, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    number_of_blobs = len(keypoints)
    cell_count_text = "Cell Count: " + str(number_of_blobs)
    cell_type = "Yeast"
    cell_type_text = "Cell Type: " + cell_type
    experiment = "Cell Culture"
    experiment_text = "Experiment: " + experiment
    mission = "ADI-AMR"
    mission_text = "Mission: " + mission
    timestamp_text = "Timestamp: " + timestamp_string
    image_number = ""
    image_number_text = "Image Number: 1 of 1000"
    # cv2.putText(keypoint, cell_type_text, (400, 380), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 2)
    # cv2.putText(keypoint, cell_count_text, (400, 405), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 2)
    # cv2.putText(keypoint, experiment_text, (400, 430), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 2)
    # cv2.putText(keypoint, mission_text, (400, 455), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 2)
    # cv2.putText(keypoint, timestamp_text, (400, 480), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 2)
    # cv2.putText(keypoint, image_number_text, (400, 505), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 2)

    cv2.imwrite(current_dt_string, keypoint)
    cv2.imwrite("blurred_cells.jpg", blur)
    cv2.imwrite("white_cells.jpg", wb)
    cv2.imwrite("black_cells.jpg", bw)

    image = Image.open(current_dt_string)

    extra_height = 150
    font = ImageFont.truetype("FiraCode-Bold.ttf", size=16)

    new_image = Image.new("RGB", (image.width, image.height + extra_height))
    new_image.paste(image, (0,0))

    draw = ImageDraw.Draw(new_image)
    draw.text((400, 525), cell_type_text, font=font)
    draw.text((400, 550), cell_count_text, font=font)
    draw.text((400, 575), experiment_text, font=font)
    draw.text((400, 600), mission_text, font=font)
    draw.text((400, 625), timestamp_text, font=font)
    draw.text((400, 650), image_number_text, font=font)

    new_image.save("modified_image.jpg")

    plt.imshow(keypoint, cmap="gray")
    plt.show()

single_image_analysis()