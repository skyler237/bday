import cv2
import numpy as np
from matplotlib import pyplot as plt
from pdb import set_trace

img = cv2.imread('test.jpg',0)

# dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
# dft_shift = np.fft.fftshift(dft)
# dft_img = np.dstack((dft_shift, np.zeros((dft_shift.shape[0], dft_shift.shape[1]))))
# plt.imshow(dft_img)
# plt.show()
# cv2.imwrite('fshift.jpg', dft_img)
dft_img = cv2.imread('fshift.jpg')
dft_shift_in = dft_img[:,:,:2]
f_ishift = np.fft.ifftshift(dft_shift_in)
img_back = cv2.idft(np.float32(f_ishift))
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])


# f = np.fft.fft2(img)
# fshift = np.fft.fftshift(f)
# # fshift = np.abs(fshift)
# set_trace()
# magnitude_spectrum = 20*np.log(np.abs(fshift))
# cv2.imwrite('fshift.jpg', fshift)
# f_ishift = np.fft.ifftshift(fshift)
# img_back = np.fft.ifft2(f_ishift)
# img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(dft_img, cmap = 'gray')
plt.title('fshift'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
plt.title('Image back'), plt.xticks([]), plt.yticks([])
plt.show()
