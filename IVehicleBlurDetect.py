import cv2
import numpy as np
import os

def blurDetect(im,mean_s=2.0,mean_l=3.5, mean_d = 38.0):
    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    im_sobel = cv2.Sobel(im_gray,cv2.CV_16U,1,1)
    mean_value_s = np.mean(im_sobel)
    print (mean_value_s)

    im_lapla = cv2.Laplacian(im_gray,cv2.CV_16U)
    mean_value_l = np.mean(im_lapla)
    # print (mean_value_l)

    res = cv2.meanStdDev(im_gray)
    # print(res)

    res = cv2.meanStdDev(im_lapla)
    # print(res)

    mean_gray = np.mean(im_gray)
    # print(mean_gray)

    if(mean_value_s<mean_s and mean_value_l<mean_l and mean_gray<mean_d):
        return 1
    else:
        return 0

def run():
    pic_dir = "/home/zqp/testimage/image"
    for pic_name in os.listdir(pic_dir):
        print(pic_name)
        im = cv2.imread("%s/%s"%(pic_dir,pic_name))
        res = blurDetect(im)
        print(res)

        cv2.imshow("im",im)
        cv2.waitKey(0)

if __name__=="__main__":
    run()