import cv2
import numpy as np
#from skimage.measure import compare_ssim as ssim

base = cv2.imread("~/MotionPi3/MotionPi/base.jpg", 0)
imgSaved = cv2.imread("/MotionPi3/MotionPi/some1.jpg", 0)
#open_door = cv2.imread("/MotionPi3/MotionPi/openDoor.jpg", 0)


def img_2_gray_scale(_img):
    # Create a CLAHE (Contrast Limited Adaptive Histogram Equalization)
    contrast_it = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = contrast_it.apply(_img)

    return gray


def compare(_base, _img):
    """ Mean square error of both images"""
    diff = np.sum((_base.astype("float") - _img.astype("float"))**2)
    diff /= float(_base.shape[0] * _img.shape[1])
    return diff

def detected_something():
 #   sim = ssim(gray_base, gray_img)
    
    new_base = img_2_gray_scale(base)
    new_img = img_2_gray_scale(imgSaved)
    
    front_face_detector = cv2.CascadeClassifier("face_detector.xml")
    faces = front_face_detector.detectMultiScale(new_img, 1.3, 5)

    if len(faces) >= 1:
        print "Face Detected"
        return 1 # If a face is detected

    sim = compare(new_img, new_base) 
    if sim <= 16000:
        return 1 # If similarity is < 60%
    else:
        return 0

print(detected_something())
