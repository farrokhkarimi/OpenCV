import numpy as np
import matplotlib.pyplot as plt

# installation: pip3 install arabic_reshaper
import arabic_reshaper

# installation: pip3 install python-bidi
from bidi.algorithm import get_display

from PIL import Image, ImageFont, ImageDraw

image = np.zeros((500,500,3), np.uint8)

text_to_be_reshaped = 'سلام من فرخ هستم'
reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
bidi_text = get_display(reshaped_text)
text = bidi_text.encode().decode('utf-8')
pil_image = Image.fromarray(image)
font = ImageFont.truetype("arial", 50, encoding='unic') # the font is read from the OS
draw = ImageDraw.Draw(pil_image)
draw.text((100,225), text, (0,255,0), font=font)

plt.imshow(pil_image)
plt.show()
