import cv2
import numpy as np

w, h = 600, 600

img = np.ones((w,h,3), dtype=np.uint8) * 255
cv2.imwrite("white_bg.png", img)
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

colorX = {
    1: 'blue',
    2: 'green',
    3: 'red',
    4: 'yellow',
    5: 'magenta',
    6: 'cyan',
    7: 'white',
    8: 'black',
    9: 'gray',
    10: 'dark_gray',
    11: 'light_gray',
}


txt = "bo mon co dien tu - ute"

for i in range(8):
    cv2.putText(img, text=txt.upper(), org=(0, (70*i)+30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=colors[colorX[i+1]])
    cv2.putText(img, text=txt, org=(0, (70*i)+60), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=colors[colorX[i+1]])

cv2.imshow("logo1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
