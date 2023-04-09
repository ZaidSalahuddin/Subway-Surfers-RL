import os
from os import listdir
import cv2

directory = r"C:\Users\Zaid Salahuddin\Documents\Snek Schizms\Subway Surfers RL\Game States\screenshots"

# get the path/directory
for images in os.listdir(directory):
    print(images)
    image = cv2.imread(directory+'\\'+images)
    cropped_image = image[0:1200, 0:650]
    cv2.imwrite(os.path.join(directory , images),cropped_image)