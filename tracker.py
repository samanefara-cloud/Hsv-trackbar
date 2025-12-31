import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# فقط image(1).jpg
img = cv2.imread('image(1).jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

fig, ax = plt.subplots(figsize=(15, 8))
plt.subplots_adjust(bottom=0.25)

# ۶ slider
slider_hmin = Slider(plt.axes([0.1, 0.15, 0.65, 0.03]), 'Hmin', 0, 179, valinit=0)
slider_smin = Slider(plt.axes([0.1, 0.12, 0.65, 0.03]), 'Smin', 0, 255, valinit=0)
slider_vmin = Slider(plt.axes([0.1, 0.09, 0.65, 0.03]), 'Vmin', 0, 255, valinit=0)
slider_hmax = Slider(plt.axes([0.1, 0.06, 0.65, 0.03]), 'Hmax', 0, 179, valinit=179)
slider_smax = Slider(plt.axes([0.1, 0.03, 0.65, 0.03]), 'Smax', 0, 255, valinit=255)
slider_vmax = Slider(plt.axes([0.1, 0.00, 0.65, 0.03]), 'Vmax', 0, 255, valinit=255)

image_display = ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax.set_title('Trackbar HSV')
ax.axis('off')

def update(val):
    lower = np.array([slider_hmin.val, slider_smin.val, slider_vmin.val])
    upper = np.array([slider_hmax.val, slider_smax.val, slider_vmax.val])
    
    mask = cv2.inRange(hsv, lower, upper)
    combined = np.hstack([cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 
                         cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)])
    
    image_display.set_data(combined)
    ax.set_title(f'lower={lower} upper={upper}')
    fig.canvas.draw()

# وصل کن
slider_hmin.on_changed(update)
slider_smin.on_changed(update)
slider_vmin.on_changed(update)
slider_hmax.on_changed(update)
slider_smax.on_changed(update)
slider_vmax.on_changed(update)

plt.show()
print("اسلایدر بکش → mask → اعداد title کپی!")
