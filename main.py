import cv2
import numpy as np
import matplotlib.pyplot as plt

cell_image = cv2.imread("img.jpg", 0)
regular_cell_image = cell_image
cell_image = cv2.bitwise_not(cell_image)
blur = cv2.GaussianBlur(cell_image, (0,0), sigmaX=4.5, sigmaY=4.5)

thresh, bw = cv2.threshold(cell_image, 128, 255, cv2.THRESH_OTSU)

wb = cv2.bitwise_not(bw)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 0
params.maxThreshold = 255

params.filterByColor = True
params.blobColor = 0

params.filterByArea = True
params.minArea = 1 # increase to 500 to reduce detected cells

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(blur)

keypoint = cv2.drawKeypoints(wb, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Total Cell Count: " + str(len(keypoints))
cv2.putText(keypoint, text, (1550, 1700), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 2)

cv2.imwrite("cell_count.jpg", keypoint)
cv2.imwrite("blurred_cells.jpg", blur)
cv2.imwrite("white_cells.jpg", wb)
cv2.imwrite("black_cells.jpg", bw)

plt.imshow(keypoint, cmap="gray")
plt.show()