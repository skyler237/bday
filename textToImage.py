import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pdb import set_trace

# Options
use_color = True
base_size = (3,2)

text = ""
if len(sys.argv) > 1:
	filename = sys.argv[1]
	with open(filename) as file:
		text = file.read()
else:
	print("Error: Missing required argument \"input_text_file\"")
	print("Usage: python textToImage.py input_text_file")
	sys.exit()

num_char = len(text)
base_area = base_size[0]*base_size[1]
if use_color:
	base_area *= 3
scale = np.ceil(np.sqrt(num_char / base_area))
width = int(scale*base_size[1])
height = int(scale*base_size[0])
if use_color:
	img = np.zeros((height, width, 3))
	num_channels = 3
else:
	img = np.zeros((height, width))
	num_channels = 1
# set_trace()

for i, ch in enumerate(text):
	row = int(np.floor(i / (num_channels*width)))
	col = int(np.floor(np.mod(i, (num_channels*width)) / 3))
	channel = int(np.mod(i, num_channels))
	# print("(", row, " ", col, " ", channel, ")")
	if use_color:
		img[row][col][channel] = ord(ch)
	else:
		img[row][col] = ord(ch)

cv2.imwrite('output_image.png', img)
plt.imshow(img, interpolation=None, filternorm=False)
plt.show()
