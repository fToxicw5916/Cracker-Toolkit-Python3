'''
Identify faces in the images.
'''
# Import needed packages
from pprint import pprint
import cv2
import os

ROOT = '<Image directory here>'  # Directory for images
FACES = '<Output directory here>'  # Output directory
TRAIN = '<Train file directory here>'  # Directory for the training file


def detect(srcdir=ROOT, tgtdir=FACES, train_dir=TRAIN):
    '''
    Detector.
    '''
    for fname in os.listdir(srcdir):
        if not fname.upper().endswith('.JPG'):
            continue
        fullname = os.path.join(srcdir, fname)
        newname = os.path.join(tgtdir, fname)
        img = cv2.imread(fullname)
        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Read the training file
        training = os.path.join(train_dir, 'haarcascade_frontalface_alt.xml')
        cascade = cv2.CascadeClassifier(training)
        rects = cascade.detectMultiScale(gray, 1.3, 5)
        try:
            if rects.any():
                print('got a face')
                rects[:, 2:] += rects[:, :2]
        except AttributeError:
            print(f'No faces found in {fname}')
            continue
            # Highlight the faces in the image
        for x1, y1, x2, y2 in rects:
            cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
        cv2.imwrite(newname, img)


if __name__ == '__main__':
    detect()
