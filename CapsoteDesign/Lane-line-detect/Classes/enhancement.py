import cv2 as cv
import numpy as np


class Enhancement:
    def convert_gray(self):
        # Convert to grayscale, because one channel is enough to compute edges
        return cv.cvtColor(self, cv.COLOR_BGR2GRAY)

    def deNoise(self):
        # Apply 5x5 Gaussian blur
        return cv.GaussianBlur(self, (5, 5), 0)

    def do_canny(self):
        # Canny edge detector with threshold values 50 and 150
        return cv.Canny(self, 50, 150)

    def segment_mask(self, kernel):
        # Image filled with zero
        mask = np.zeros_like(self)
        # fill Mask with ones other areas with 0
        cv.fillPoly(mask, kernel, 255)

        return cv.bitwise_and(self, mask)
