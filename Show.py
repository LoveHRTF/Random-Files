'''
    Randomly show files under path
    07.13.2019
    @chenz
'''

import random
import sys
import time

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.pyplot import figure

import os
import shlex
import platform


def showImage(fileList, iters=1, interval=0, sysImgApp=1):

    Block = True
    if interval > 0:
        Block = False        

    for _ in range(iters):
        # Random Pick
        idx = random.randint(0, len(fileList)-1)
        rand_file = fileList[idx]
        # Show File
        if sysImgApp == 1:
            # Open file using system application
            if platform.system() == 'Darwin':
                os.system("open " + shlex.quote(rand_file))
            elif platform.system() == 'Windows':
                os.system("start " + rand_file)
            time.sleep(interval)
        else:
            # Open file using matpolib
            img = mpimg.imread(rand_file)
            plt.title(rand_file)
            figure(dpi=200)
            plt.imshow(img)
            plt.show(block=Block)
            plt.pause(interval)
            plt.close()


def showVideo(fileList):

    idx = random.randint(0, len(fileList)-1)
    rand_file = fileList[idx]

    if platform.system() == 'Darwin':
        os.system("open " + shlex.quote(rand_file))
    elif platform.system() == 'Windows':
        os.system("start " + rand_file)
    else:
        print("ERROR -> Show.showVideo: Unknown System Type")

def openAny(fileList):

    idx = random.randint(0, len(fileList)-1)
    rand_file = fileList[idx]

    if platform.system() == 'Darwin':
        os.system("open " + shlex.quote(rand_file))
    elif platform.system() == 'Windows':
        os.system("start " + rand_file)
    else:
        print("ERROR -> Show.openAny: Unknown System Type")
