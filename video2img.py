import cv2
import os

def video2imgs(video_path, save_path='./tempimg'):
    vc = cv2.VideoCapture(video_path) #读入视频文件
    c = 0
    rval = vc.isOpened()

    while rval:   #循环读取视频帧
        c = c + 1
        rval, frame = vc.read()
        pic_path = save_path + '/'
        if rval:
            img_save_path = os.path.join(pic_path, '{:06d}.jpg'.format(c))
            cv2.imwrite(img_save_path, frame) #存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
            cv2.waitKey(1)
        else:
            break
    vc.release()
    print('save_success')