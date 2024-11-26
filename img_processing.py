"""
 * author: Ohidul Islam
 * created on 25-11-2024-16h-45m
 * copyright 2024
"""
import numpy as np
import cv2

###################################


def crop_image(image, top_left_corner=(), bottom_right_corner=()):

    x_start, y_start = top_left_corner
    x_end, y_end = bottom_right_corner

    cropped_img = image[y_start:y_end, x_start:x_end]

    return cropped_img


######################################
def load_image(path):
    '''
    @path: path of the image
    '''
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print("Error: Unable to load image. Check the file path.")

    else:
        print("Image loaded successfully!")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(
        img.shape) == 3 else img

    return img
