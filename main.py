import cv2
import numpy as np
import matplotlib.pyplot as plt

cell_image = cv2.imread("img.jpg", 0)
regular_cell_image = cell_image
cell_image = cv2.bitwise_not(cell_image)
blur = cv2.GaussianBlur(cell_image, (0,0), sigmaX=35, sigmaY=35)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 60
params.maxThreshold = 255

params.filterByColor = True
params.blobColor = 0

params.filterByArea = True
params.minArea = 30

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(blur)

keypoint = cv2.drawKeypoints(regular_cell_image, keypoints, np.array([]), (255,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Total Cell Count: " + str(len(keypoints))
cv2.putText(keypoint, text, (20, 1600), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)

cv2.imwrite("test_cell_count.jpg", keypoint)

plt.imshow(keypoint, cmap="gray")
plt.show()
