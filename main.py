from moviepy.editor import *
from skimage.filters import gaussian

def blur(image):
    return gaussian(image.astype(float), sigma=0.5)

clip = VideoFileClip('myvideo.mp4').subclip(30, 35)

clip_blurred = clip.fl_image(blur)

clip_blurred.write_gif('mygif.gif')