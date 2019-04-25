import cv2
import os
import glob
from ProcessingBar import ShowProcess

def img2video(imgdir, fps=24, img_size=(768, 576)):
    imgs_dir = imgdir;
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    save_name = './result.avi'
    video_writer = cv2.VideoWriter(save_name, fourcc, fps, img_size)
    # no glob, need number-index increasing
    imgs = glob.glob(os.path.join(imgs_dir, '*.jpg'))
    print("There are {:d} pictures in your folders".format(len(imgs)))

    # 进度条显示
    max_steps = len(imgs)
    process_bar = ShowProcess(max_steps)

    for i in range(1, len(imgs)+1):
        imgname = os.path.join(imgs_dir, '{:06d}.jpg'.format(i))
        frame = cv2.imread(imgname)
        video_writer.write(frame)
        process_bar.show_process()

    process_bar.close()
    video_writer.release()
