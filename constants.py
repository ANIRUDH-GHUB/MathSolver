import numpy as np

inputFilename = 'images/feed/matheq.jpg'
outputFilename = "images/output/symbol"
extension = ".jpg"

thresh = 127

kernel = np.ones((5,5), np.uint8)
