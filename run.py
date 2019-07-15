'''
    Randomly show files under specific path
    07.12.2019
    @chenz
'''
import FileDirectory as fd
import Show as sh

import random
import sys
import argparse

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def main():
    # Process Parameters
    parser = argparse.ArgumentParser(description='Setup Parameters')
    parser.add_argument('--iters',      default=1,      type=int,   help='Number of files to show')
    parser.add_argument('--interval',   default=0,      type=float, help='Show time for each file')
    parser.add_argument('--path',       default='',     type=str,   help='Path for searching files')
    parser.add_argument('--type',       default='IMG',  type=str,   help='Type of file for search, currently spports IMG, JPG/JPEG, PNG')
    parser.add_argument('--sysImgApp',  default=0,   type=int,  help='Selection for use system application to open image or matplotlib')
    args = parser.parse_args()

    if args.path:
        
        file_list = fd.genAllFileDir(args.path)

        if args.type == 'IMG':
            file_list = fd.getImage(file_list)
            sh.showImage(file_list, iters=args.iters, interval=args.interval, sysImgApp=args.sysImgApp)

        elif args.type == 'JPG' or args.type == 'JPEG':
            file_list = fd.getJPG(file_list)
            sh.showImage(file_list, iters=args.iters, interval=args.interval, sysImgApp=args.sysImgApp)

        elif args.type == 'PNG':
            file_list = fd.getPNG(file_list)
            sh.showImage(file_list, iters=args.iters, interval=args.interval, sysImgApp=args.sysImgApp)

        elif args.type == 'Video':
            file_list = fd.getVideo(file_list)
            sh.showVideo(file_list)

        elif args.type == 'Any':
            sh.openAny(file_list)

        else:
            print('TODO')
            # TODO


if __name__ == "__main__":
    main()
