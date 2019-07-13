'''
    Get all regular files under certain directory
    07.12.2019
    @chenz
'''

import os
import re

# Input string of directory, returns all files under this directly as a list
def genAllFileDir(path):
    file_dirs = []
    for root, _, files in os.walk(path):
        for file in files:
            # root_dir = root
            file_dir = os.path.join(root,file)
            if file[0] != '.':
                file_dirs.append(file_dir)

    return file_dirs

# Input list of files, returns matched type files as a list
# All Images
def getPNG(files):
    items = []
    for item in files:
        if re.findall(r".png\b", item):
            items.append(item)
    return items


def getJPG(files):
    items = []
    for item in files:
        if re.findall(r".jpg\b", item) or \
            re.findall(r".jpeg\b", item):
            items.append(item)
    return items


def getImage(files):
    items = []
    for item in files:
        if re.findall(r".jpg\b", item) or \
            re.findall(r".jpeg\b", item) or \
            re.findall(r".png\b", item):
            items.append(item)
    return items

# All Videos
def getMP4(files):
    items = []
    for item in files:
        if re.findall(r".mp4\b", item):
            items.append(item)
    return items

def getAVI(files):
    items = []
    for item in files:
        if re.findall(r".avi\b", item):
            items.append(item)
    return items


def getMOV(files):
    items = []
    for item in files:
        if re.findall(r".mov\b", item):
            items.append(item)
    return items


def getMPEG(files):
    items = []
    for item in files:
        if re.findall(r".mpeg\b", item):
            items.append(item)
    return items


def getVideo(files):
    items = []
    for item in files:
        if re.findall(r".mp4\b", item) or \
            re.findall(r".avi\b", item) or \
            re.findall(r".mov\b", item) or \
            re.findall(r".mpeg\b", item):
            items.append(item)
    return items


# Get a random file from list:
# def getRandom(files):