#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cv2

def capture_img(path_back):
    cam = cv2.VideoCapture(0) # 0 means the 1st camera
    image_count = 0 #counter in case of several times capturing Pic/Img
    img_save = '' #save image variable

    while True:
        #capture frame by frame
        ret, frame = cam.read()

        #Display frame
        cv2.imshow("Frame", frame)

        wk = cv2.waitKey(1)

        if (wk%256 == 27): #Press Escape
            cam.release()
            cv2.destroyAllWindows()
            break

        elif (wk%256 == 32): #Press Space
            img_save = "img_{}.png".format(image_count)
            cv2.imwrite(img_save, frame)
            image_count +=1  


    #Read Images
    image = cv2.imread(img_save)
    image_back = cv2.imread(path_back)

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #convert to gray desired image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.1, 4)

    #convert to gray background image
    gray_back = cv2.cvtColor(image_back, cv2.COLOR_BGR2GRAY)
    face_back = face_cascade.detectMultiScale(gray_back, 1.1, 4)

    #Identify Face in Image
    for (x, y, w, h) in face:
        cv2.rectangle(image, (x, y),(x+w, y+h),(), 1)
        a, b, c, d = x, x+w, y, y+h

    #Identify Face in Backround
    for (x, y, weight, height) in face_back:
        cv2.rectangle(image_back, (x, y),(x+weight, y+height),(), 1)
        i, j, k, l = x, x+weight, y, y+height

    #Crop Face
    face_crop = image[c:d, a:b]

    #Resize Face and fit backround img
    resize_face = cv2.resize(face_crop, (weight, height))
    w, h, c = resize_face.shape
    image_back[k:l, i:j] = resize_face

    #Display Image
    cv2.imshow("Image", image_back)
    
    # destroy windows if any key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return True


# In[ ]:




