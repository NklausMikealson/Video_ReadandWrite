import argparse
from img2video import img2video
from video2img import video2imgs

parser = argparse.ArgumentParser(description="It's a smart tool for video and image")
parser.add_argument('--options', default= 1, type=int,
                    help='choose your goals')
args = parser.parse_args()

if __name__ == "__main__":
    if args.options == 1:
        img2video(imgdir='./img', fps=24, img_size=(768, 576))

    if args.options == 2:
        video2imgs(video_path='./video/result.avi')
