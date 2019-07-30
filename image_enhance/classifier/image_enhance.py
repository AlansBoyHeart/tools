import cv2
import os
import numpy as np

class Enhance():

    def __init__(self):
        self.directory = None
        self.name = None
        self.suffix = None
        self.count = None

    def enhance(self,path):
        self.count = 0
        self.directory = os.path.dirname(path)
        picture_name = os.path.basename(path).split(".")
        self.name, self.suffix = picture_name[0], picture_name[-1]
        image = cv2.imread(path)

        image_center = self.center(image)
        self.flip_horizon_vertical(image)
        self.rotate(image)


    def flip_horizon_vertical(self,image):
        #image = cv2.flip(image,1) 1表示水平，0是垂直，-1是水平加垂直
        image_new0 = cv2.flip(image, 0)
        image_new1 = cv2.flip(image, 1)
        self._save(image_new0)
        self._save(image_new1)


    def center(self,image,resize_rate = 0.1):
        r = resize_rate
        h, w = image.shape[:2]
        xmin, xmax = int(h*r), int(h-h*r)
        ymin, ymax = int(w*r), int(w-w*r)
        image_new = image[xmin:xmax, ymin:ymax]
        self._save(image_new)
        return image_new

    def rotate(self,image):
        image_new1 = cv2.rotate(image, 0)  #0旋转90,1旋转180,2旋转270
        image_new2 = cv2.rotate(image, 1)
        image_new3 = cv2.rotate(image, 2)
        self._save(image_new1)
        self._save(image_new2)
        self._save(image_new3)

    def rotation(self,image, angle=[30,15,-15,-30]):
        for i in angle:
            image_new1 = self._rotation(image, i)
            self._save(image_new1)


    def _rotation(self, image, angle):
        # grab the dimensions of the image and then determine the
        # center
        (h, w) = image.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        # grab the rotation matrix (applying the negative of the
        # angle to rotate clockwise), then grab the sine and cosine
        # (i.e., the rotation components of the matrix)
        M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])

        # compute the new bounding dimensions of the image
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))

        # adjust the rotation matrix to take into account translation
        M[0, 2] += (nW / 2) - cX
        M[1, 2] += (nH / 2) - cY

        # perform the actual rotation and return the image
        return cv2.warpAffine(image, M, (nW, nH))


    def _save(self,image):
        if self.count != None:
            path = os.path.join(self.directory,self.name+"_"+str(self.count)+"."+self.suffix)
            cv2.imwrite(path,image)
            self.count += 1

def enhance(directory):
    enhan = Enhance()
    for i in os.listdir(directory):
        picture_name = os.path.join(directory, i)
        print(picture_name)
        try:
            enhan.enhance(picture_name)
        except Exception as e:
            print(e)


