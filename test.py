from rename_filenames_by_quantity import rename_file
from image_enhance.classifier.image_enhance import enhance
from image_enhance.classifier.image_enhance import Enhance
import os


def rename():
    aaa = "E:\horrible_terrorist_classification\img2/natural"
    rename_file(aaa, flag=1)

def enhan():
    aaa = "E:\horrible_terrorist_classification\img2/natural"
    for i in os.listdir(aaa):
        dir_name = os.path.join(aaa, i)
        enhance(dir_name)

def revise():
    enh = Enhance()
    for i in range(190,201):
        picture_name = os.path.join("E:\horrible_terrorist_classification\img2/bloody", str(i)+".jpg")
        enh.enhance(picture_name)


def main():
    rename()

if __name__ == '__main__':
    main()


