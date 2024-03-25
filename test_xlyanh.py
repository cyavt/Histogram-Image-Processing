import cv2
import numpy as np

w, h = 600, 600
colors = {
    'blue': (255, 0, 0),
    'green': (0, 255, 0),
    'red': (0,0, 255),
    'yellow': (0,255,255),
    'magenta': (255,0,255),
    'cyan': (255,255,0),
    'white': (255,255,255),
    'black': (0,0,0),
    'gray': (125,125,125),
    'dark_gray': (50,50,50),
    'light_gray': (220,220,220),
}

img = np.ones((w,h,3), dtype=np.uint8) * 255
cv2.imwrite("white_bg.png", img)

(b, g, r) = cv2.split(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if b[i, j] == 255 and g[i, j] == 255 and r[i, j] == 255:
                 img[i, j] = colors['light_gray']


img1 = cv2.line(img, (300, 600), (600, 300), colors['blue'], 1)
img2 = cv2.rectangle(img1, (450, 450), (597, 597), colors['black'], 4)
img3 = cv2.rectangle(img2, (150, 0), (300, 600), colors['magenta'], 4)
img4 = cv2.rectangle(img3, (0, 150), (600, 300), colors['red'], 4)
img5 = cv2.circle(img4, (225, 225), 75, colors['green'], 4)

# 2 hình ellipses
img6 = cv2.ellipse(img5, (450, 225), (150, 75), 0, 0, 360, colors['black'], 4)
img7 = cv2.ellipse(img6, (225, 450), (75, 150), 0, 0, 360, colors['black'], 4)

# hình đa giac
pts1 = np.array([[225, 300], [300, 450], [225, 600], [150, 450]], np.int32)
pts2 = np.array([[300, 225], [450, 150], [600, 225], [450, 300]], np.int32)
pts3 = np.array([[300, 450], [450, 450], [450, 300]], np.int32)

img8 = cv2.polylines(img7, [pts1], True, colors['red'], 2)
img9 = cv2.polylines(img8, [pts2], True, colors['red'], 2)
img10 = cv2.polylines(img9, [pts3], True, colors['yellow'], 4)

cv2.imshow("logo1", img10)
cv2.waitKey(0)
cv2.destroyAllWindows()
