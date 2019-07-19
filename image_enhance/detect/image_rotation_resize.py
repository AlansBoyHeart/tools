import cv2
import numpy as np
import random


class Graphics():
    def __init__(self):
        pass

    @classmethod
    def rotation(cls, image):
        # grab the dimensions of the image and then determine the
        # center
        (h, w) = image.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        random_num = np.random.random()*180 - 90
        angle = int(random_num)
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

    @classmethod
    def resize(cls,image):
        """
        不同的插值（interpolation）方法，缩小时使用cv2.INTER_AREA，扩大时推荐使用cv2.INTER_CUBIC和cv2.INTER_LINEAR
        cv2.INTER_LINEAR犹豫算法的特性，扩大时最大只能扩大两倍。
        :param image: a picture
        :return:
        """
        rows, colums = image.shape[:2]
        print(rows, colums)
        random_num = np.random.random()
        if random_num > 0.5:
            random_big = np.random.random()*0.6 + 1.2
            hight = int(rows*random_big)
            width = int(colums*random_big)
            image = cv2.resize(image, (width, hight), interpolation=cv2.INTER_LINEAR)
            print(image.shape)
            return image
        else:
            random_small = np.random.random()*0.4+0.5
            # random_small = 0.5
            hight = int(rows * random_small)
            width = int(colums * random_small)
            image = cv2.resize(image, (width, hight), interpolation=cv2.INTER_AREA)
            print(image.shape)
            return image

    @classmethod
    def concat(cls, image, object):
        (hight , width) = object.shape[:2]
        (hight_image, width_image) = image.shape[:2]
        if hight>hight_image or width>width_image:
            return None
        range_X = hight_image - hight
        range_Y = width_image - width
        nX = random.randint(0,range_X)
        nY = random.randint(0,range_Y)
        xmin = nX
        ymin = nY
        xmax = nX+hight
        ymax = nY+width
        tmp = image[nX:nX+hight,nY:nY+width]
        tmp[object>0] = 0
        tmp = tmp + object
        image[nX:nX + hight, nY:nY + width] = tmp
        return (image,xmin,ymin,xmax,ymax)


object=cv2.imread('./222.jpg')
image = cv2.imread("./111.jpg")
object=Graphics.resize(object)   #resize the object
object = Graphics.rotation(object)  #rotate the object

#the object need smaller than image
result = Graphics.concat(image,object)  #paste the object on image
if result == None:
    print("object is bigger than image")
else:
    image, xmin, ymin, xmax, ymax = result
print(xmin,ymin,xmax,ymax)

# play the image
cv2.namedWindow("kuku",cv2.WINDOW_NORMAL)
cv2.imshow('kuku',image)
cv2.waitKey()
cv2.destroyAllWindows()




