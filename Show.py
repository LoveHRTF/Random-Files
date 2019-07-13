'''
    Randomly show files under path
    07.13.2019
    @chenz
'''

import random
import sys

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def showImage(fileList, iters=1, interval=0):

    Block = True
    if interval > 0:
        Block = False        

    for _ in range(iters):
        # Random Pick
        idx = random.randint(0, len(fileList)-1)
        rand_file = fileList[idx]
        # Show File
        img = mpimg.imread(rand_file)
        plt.title(rand_file)
        plt.imshow(img)
        plt.show(block=Block)
        plt.pause(interval)
        plt.close()


def showVideo(fileList):
    # TODO
    pass