import argparse
import tty, termios
import sys
import os
import time

from picamera import PiCamera

import ir_cut


def getch():
    """getch() -> key character

    Read a single keypress from stdin and return the resulting character.
    Nothing is echoed to the console. This call will block if a keypress
    is not already available, but will not wait for Enter to be pressed.

    If the pressed key was a modifier key, nothing will be detected; if
    it were a special function key, it may return the first character of
    of an escape sequence, leaving additional characters in the buffer.
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


class DatasetCreator:
    def __init__(self, dir, preview_capture=False):
        dir = 'data/{}'.format(dir)
        if os.path.isdir(dir):
            raise ValueError("Directory {} already exists. Exiting".format(dir))
        else:
            os.mkdir(dir)
        self.camera = PiCamera()
        self.dir = dir
        self.count = 0
        self.preview_capture = preview_capture

        
    def take_photo(self):
        self.camera.capture('{}/{}_normal.jpg'.format(self.dir, self.count))

        ir_cut.disable_filter()
        time.sleep(1)
        self.camera.capture('{}/{}_ir.jpg'.format(self.dir, self.count))

        ir_cut.enable_filter()

        self.count += 1

        
    def loop(self):
        ir_cut.enable_filter()
        while True:
            if self.preview_capture:
                self.camera.start_preview()
            print("hit space to take another shot, q to exit")
            keyboard_input = getch()
            print('input: "{}"'.format(keyboard_input))
            if keyboard_input == 'q':
                print("exiting")
                return
            if keyboard_input == ' ':
                if self.preview_capture:
                    self.camera.stop_preview()
                self.take_photo()


def main():
    parser = argparse.ArgumentParser(
        description='take a sequence of photo with ir filter on/off')
    parser.add_argument('dataset_dir', help='new dir for dataset')
    args = parser.parse_args()

    dir = args.dataset_dir

    dataset_creator = DatasetCreator(dir, preview_capture=True)
    dataset_creator.loop()

if __name__ == '__main__':
    main()
