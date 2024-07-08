import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def single_image_analysis():
    current_dt = datetime.now()
    timestamp_string = current_dt.strftime("%Y/%m/%d %H:%M:%S")
    current_dt_string = current_dt.strftime("%Y.%m.%d_%H.%M.%S.jpg")

    regular_image = cv2.imread("img.tiff")
    cell_image = cv2.imread("img.tiff", 0)
    cell_image = cv2.bitwise_not(cell_image)
    blur = cv2.GaussianBlur(cell_image, (0,0), sigmaX=3.5, sigmaY=3.5)

    _, bw = cv2.threshold(cell_image, 1, 255, cv2.THRESH_OTSU)

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

    keypoint = cv2.drawKeypoints(regular_image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cell_count = len(keypoints)
    cell_count_text = "Cell Count: "
    cell_type = "Yeast"
    cell_type_text = "Cell Type: "
    experiment = "Cell Culture"
    experiment_text = "Experiment: "
    mission = "ADI-AMR"
    mission_text = "Mission: "
    timestamp_text = "Timestamp: "
    image_number = "1 of 1000"
    image_number_text = "Image Number: "

    cv2.imwrite(current_dt_string, keypoint)
    cv2.imwrite("blurred_cells.jpg", blur)
    cv2.imwrite("white_cells.jpg", wb)
    cv2.imwrite("black_cells.jpg", bw)

    image = Image.open(current_dt_string)
    rs_logo = Image.open("rs-logo.png")

    extra_height = 150
    new_logo_size = 354.9, 74.1
    rs_logo.thumbnail(new_logo_size)
    regular_font = ImageFont.truetype("FiraCode-Retina.ttf", size=16)
    bold_font = ImageFont.truetype("FiraCode-Bold.ttf", size=16)

    new_image = Image.new("RGB", (image.width, image.height + extra_height), color=(23, 36, 45))
    new_image.paste(image, (0,0))
    new_image.paste(rs_logo, (20, 560), mask=rs_logo)

    draw = ImageDraw.Draw(new_image)
    draw.text((400, 525), cell_type_text, font=bold_font)
    cell_type_text_width = bold_font.getlength(cell_type_text)
    draw.text((400 + cell_type_text_width, 525), cell_type, font=regular_font)

    draw.text((400, 550), cell_count_text, font=bold_font)
    cell_count_text_width = bold_font.getlength(cell_count_text)
    draw.text((400 + cell_count_text_width, 550), str(cell_count), font=regular_font)

    draw.text((400, 575), experiment_text, font=bold_font)
    experiment_text_width = bold_font.getlength(experiment_text)
    draw.text((400 + experiment_text_width, 575), experiment, font=regular_font)

    draw.text((400, 600), mission_text, font=bold_font)
    mission_text_width = bold_font.getlength(mission_text)
    draw.text((400 + mission_text_width, 600), mission, font=regular_font)

    draw.text((400, 625), timestamp_text, font=bold_font)
    timestamp_text_width = bold_font.getlength(timestamp_text)
    draw.text((400 + timestamp_text_width, 625), timestamp_string, font=regular_font)

    draw.text((400, 650), image_number_text, font=bold_font)
    image_number_text_width = bold_font.getlength(image_number_text)
    draw.text((400 + image_number_text_width, 650), image_number, font=regular_font)

    new_image.save("modified_image.jpg")

    plt.imshow(keypoint, cmap="gray")
    plt.show()

single_image_analysis()