import cv2
import pytesseract

class preprocessing(object):
    def __init__(self):
        pass


    def preprocess_img(self, img):
        return img


    def run_tesseract(self, img):
        detected_text = pytesseract.image_to_string(img)
        return detected_text