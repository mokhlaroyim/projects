import cv2 as cv
import numpy as np

"""
:param old_left gives the old value of the left line, helps to get more optimized lines
:param old_Right gives the old value of the Right line, helps to get more optimized lines

"""
old_Left = None
old_Right = None


class Lines:

    def apply_houghlines(self):
        # Hough lines takes frame, distance resolution of accumulator(larger => less precision),
        # Angle resolution (larger => less precision),
        # Threshold of minimum number of intersection,
        # Min and Max distance between disconnected lines
        hough = cv.HoughLinesP(self, 2, np.pi / 100, 100, np.array([]), minLineLength = 100, maxLineGap = 150)
        return hough

    def calculate_cord(self, lines):
        slope, intercept = lines
        # Sets beginning y as height
        y1 = self.shape[0]
        # Sets finishing y as 150 above the bottom
        y2 = int(y1 - 150)
        # Sets beginning x as (y1 - b) / m, because y1 = mx1 + b
        x1 = int((y1 - intercept) / slope)
        # Sets finishing x as (y2 - b) / m, because y2 = mx2 + b
        x2 = int((y2 - intercept) / slope)
        result = np.array([x1, y1, x2, y2])
        return result



    def calculate_lines(self, lines):
        # Arrays to store left and right coordinates
        left = []
        right = []
        global old_Left
        global old_Right

        # Loop through every line
        if lines is not None:
            for line in lines:
                # To reshape from 2D to 1D
                x1, y1, x2, y2 = line.reshape(4)
                # To fit polynomial to the x and y coordinates and return vector
                parameters = np.polyfit((x1, x2), (y1, y2), 1)

                slope = parameters[0]
                y_intercept = parameters[1]
                # If negative, the line is on the left side, if positive it is right
                if slope < 0:
                    left.append((slope, y_intercept))
                else:
                    right.append((slope, y_intercept))

                # Part for getting the direction of lines
                if 0.9 < slope < 1.15:
                    cv.putText(self, "Smooth Right ", (10, 120), cv.FONT_HERSHEY_COMPLEX, 1, (128, 0, 128, 255), 3)
                elif 0.2 < slope < 0.595:
                    cv.putText(self, "Smooth Left: ", (10, 120), cv.FONT_HERSHEY_COMPLEX, 1, (128, 0, 128, 255), 3)

        # Averages all values into a single slope and y-intercept value for each line
        left_avg = np.average(left, axis = 0)
        right_avg = np.average(right, axis = 0)

        # Calculates the coordinates for the lines
        left_l = None if not left else Lines.calculate_cord(self, left_avg)
        right_l = None if not right else Lines.calculate_cord(self, right_avg)

        # Below code is made to optimize lines
        if left_l is not None:
            old_Left = left_l
        else:
            left_l = old_Left

        if right_l is not None:
            old_Right = right_l
        else:
            right_l = old_Right

        # Puts everything into one array
        l_result = np.array([left_l, right_l])
        return l_result

    def visualize_lines(self, lines):
        # Creates an image with zeros with the same dimensions as the frame
        visualize = np.zeros_like(self)

        if lines[0] is not None and lines[1] is not None:
            for x1, y1, x2, y2 in lines:
                # Draws lines
                cv.line(visualize, (x1, y1), (x2, y2), (128, 0, 128), 8)
        return visualize
