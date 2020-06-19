import cv2 as cv
import numpy as np
import time
from Classes.enhancement import Enhancement as en
from Classes.lines import Lines


# Function to get initial mask values for different screen sizes
def get_maskvalues(y1, x1, y2, x2, y3, x3):
    return np.array([
        [(y1, x1), (y2, x2), (y3, x3)]
    ])


# Function to show FPS and Time on the screen
def show_fps(frame):
    cv.putText(frame, "FPS: " + str(last_fps), (10, 40), cv.FONT_HERSHEY_COMPLEX, 1, (128, 0, 128, 255), 3)
    cv.putText(frame, "Time: " + str(t_time), (10, 80), cv.FONT_HERSHEY_COMPLEX, 1, (128, 0, 128, 255), 3)


# Function to resize video
def v_resize(frame, width, height):
    frame = cv.resize(frame, (width, height), fx=0, fy=0, interpolation=cv.INTER_CUBIC)
    return frame


if __name__ == "__main__":

    # Initialize the video name, use default if you are not changing the name.
    vName = "Videos/Texas1.mp4"
    # The video is read in as a VideoCapture object
    cap = cv.VideoCapture(vName)

    # Initialize values for FPS
    t_time, fps, last_fps = 0, 0, 0
    s_time = time.time()
    while cap.isOpened():
        # param: ret a boolean value from the frame
        # param: frame gives current frame
        ret, frame = cap.read()
        if not ret:
            break

        # Gives the height and weight of the frame
        h, w, c = frame.shape
        # # Kernel for default video size
        kernel = get_maskvalues(int(h * 0.9), int(w / 2.75), int(h / 2.25), h, int(w * 0.8), h)

        # Uncomment for different frame sizes!

        # Resize for 1024 x 768!
        # frame = v_resize(frame, 1024, 768)
        # h, w, c = frame.shape
        # kernel = get_maskvalues(int(h * 0.75), int(w / 2.55), int(h / 2.25), h, int(w * 0.85), h)

        # Resize for 800 x 600!
        # frame = v_resize(frame, 800, 600)
        # h, w, c = frame.shape
        # kernel = get_maskvalues(int(h * 0.68), int(w / 2.1), int(h / 2.8), h, int(w * 0.8), h)

        # Resize for 640 x 480!
        # frame = v_resize(frame, 640, 480)
        # h, w, c = frame.shape
        # kernel = get_maskvalues(int(h * 0.68), int(w / 2.1), int(h / 2.55), h, int(w * 0.8), h)

        # # Resize for 400 x 300!
        # frame = v_resize(frame, 400, 300)
        # h, w, c = frame.shape
        # kernel = get_maskvalues(int(h * 0.68),q int(w / 2.15), int(h / 2.55), h, int(w * 0.8), h)

        # First mission convert to gray
        gray = en.convert_gray(frame)
        # Denoise
        blur = en.deNoise(gray)

        # do Canny
        canny = en.do_canny(blur)

        # Segment the mask
        mask = en.segment_mask(canny, kernel)
        cv.imshow("Result", mask)
        # Apply hough lines
        hough = Lines.apply_houghlines(mask)
        # Averages all lines from hough into one line
        lines = Lines.calculate_lines(frame, hough)

        # Visualizes the lines
        visualize = Lines.visualize_lines(frame, lines)

        # Overlays lines on frame by taking their weighted sums and adding scalar value of 1 as the
        result = cv.addWeighted(frame, 0.9, visualize, 1, 1)

        # Part for FPS
        show_fps(result)
        fps += 1
        c_time = time.time() - s_time
        if c_time - t_time >= 1:
            t_time += 1
            last_fps = fps
            fps = 0
        # # Saves video

        # Opens a new window and displays the result
        cv.imshow("Resulted Video", result)
        # cv.imshow('Video', mask)

        if cv.waitKey(15) & 0xFF == ord('q'):
            break
    else:
        print("Error opening")
    # below lines Free up memory and close windows
    cap.release()
    cv.destroyAllWindows()
