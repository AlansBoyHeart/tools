import cv2

class Enhance():

    def __init__(self):
        pass

    def enhance(self,path):
        image = cv2.imread(path)

    def flip_vertical(self,image):
        #image = cv2.flip(image,1) 1表示水平，0是垂直，-1是水平加垂直


    def flip_horizon(self):
        pass

    def flip_horizon_vertical(self):
        pass

    def resize(self,image,resize_rate = 0.1):
        r = resize_rate
        h, w = image.shape[:2]
        xmin, xmax = h*r, h-h*r
        ymin, ymax = w*r, w-w*r
        image_new = image[xmin:xmax, ymin:ymax]
        cv2.imwrite("aa",image_new)
        return image_new



