import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

if len(sys.argv) > 1:
	filename = sys.argv[1]
	img = np.array(cv2.imread(filename))
else:
	print("Error: Missing required argument \"input_image_file\"")
	print("Usage: python imageToText.py input_image_file")
	sys.exit()

img = img.reshape(-1)
img = list(img)
text = ""
for x in img:
	text += chr(x)

with open('output_file.txt', 'w') as file:
	file.write(text)
print(text)
