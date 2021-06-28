from collections import deque
import cv2
import numpy as np
from constants import *


def display():
    cv2.imshow("img", img_gray)
    cv2.imshow("imageArray", imageArray)
    cv2.imshow("black", whiteImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def isValid(row, col):
    if (row<0 or col<0 or row>=n or col>=m):
        return False
    if imageArray[row][col] >=thresh:
        return False
    return True

def bfs(row, col):
        queue = deque()
        queue.append((row, col))    
        imageArray[row][col] = 255
        whiteImage[row][col] = 0
        dROW = [-1,0,1,0]
        dCOL = [0,1,0,-1]
        while queue:
            row, col = queue.popleft()
            for i in range(len(dROW)):
                newROW = row + dROW[i]
                newCOL = col + dCOL[i]
                if isValid(newROW, newCOL) and imageArray[newROW][newCOL] != 255:
                    queue.append((newROW, newCOL))
                    imageArray[newROW][newCOL] = 255
                    whiteImage[newROW][newCOL] = 0


#main method
img = cv2.imread(inputFilename)
n, m, ch = img.shape
#removing noice
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
#converting to gray
img_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
#conveting to binary
img_bw = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)[1]
#creating empty white board
white = np.zeros(img.shape, dtype = "uint8")
white.fill(255)

imageArray = img_bw.copy()
imgNum = 0

for i in range(m):
    for j in range(n):
        if imageArray[j][i] == 0:
            imgNum+=1
            whiteImage = white.copy()
            bfs(j, i)
            #increasing symbol width
            b = cv2.erode(whiteImage, kernel, iterations=1)
            #saving symbol
            cv2.imwrite(outputFilename+str(imgNum)+extension, b)
            
