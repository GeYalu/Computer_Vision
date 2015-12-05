__author__ = 'geyalu'

import cv2
import os
""" Trans image to pixel data and saved in a txt  """


def list_dir(rootDir):
    """list all files in a direction and return img_path """
    img_path=[]
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        print path
        img_path.append(path)
        if os.path.isdir(path):
            list_dir(path)
    return img_path


def load_img(path):
    img = cv2.imread(path,0)
    #cv2.imshow('Image', img)
    #cv2.waitKey (0)
    #cv2.destroyAllWindows()
    return img


def img_to_list(img):
    """trans img to pixel data"""
    temp_data=[]
    height,width = img.shape
    for i in range(height):
        for j in range(width):
            temp=img[i,j]
            temp_data.append(str(temp))
    data_w=','.join(temp_data)
    return data_w


def inverse_color(image):

    height,width = image.shape
    img2 = image.copy()

    for i in range(height):
        for j in range(width):
            img2[i,j] = (255-image[i,j]) # For GRAY_SCALE image ;
                                         # for R.G.B image: img2[i,j] = (255-image[i,j][0],255-image[i,j][1],255-image[i,j][2])
    return img2


def resize(img,width,height):
    res=cv2.resize(img,(width,height),interpolation=cv2.INTER_CUBIC)
    return res



def main_resize_inverse():

    rootdir=r"F:\hand_number2"    #direction you want to traverse
    img_path=list_dir(rootdir)

    fp=open('hand_numbers2.txt','a') #results you want to save

    for i in img_path:
        img=load_img(i)
        img_res=resize(img,28,28)
        img_res_inverse=inverse_color(img_res)


        cv2.imshow('Image', img_res_inverse)
        cv2.waitKey (0)
        cv2.destroyAllWindows()

        img_data=img_to_list(img_res_inverse)

        fp.writelines(img_data)
        fp.write('\n')

    fp.close()


def main_only_Trans_to_txt():

    rootdir=r"F:\number9"    #direction you want to traverse
    img_path=list_dir(rootdir)

    fp=open('hand_numbers.txt','a') #results you want to save

    for i in img_path:
        img=load_img(i)
        img_data=img_to_list(img)

        fp.writelines(img_data)
        fp.write('\n')

    fp.close()


if __name__ == '__main__':
    """Choose main function
        main_resize_inverse()
        main_only_Trans_to_txt()
    """

    main_only_Trans_to_txt()

