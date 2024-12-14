from PIL import  Image
import numpy as np
import random


IMAGE_PATH = "./danger_zone.png"
img = Image.open(IMAGE_PATH)

pixel_array = np.array(img)
pixel_array = pixel_array.reshape(-1, 3)

image_pixels_num = len(pixel_array)

red = 0
blue = 0

print(pixel_array[0])
for _ in range(1_000_000):
    random_int = random.randint(0, image_pixels_num - 1)

    if pixel_array[random_int][0] == 255:
        red += 1
    elif pixel_array[random_int][2] == 255:
        blue += 1

ratio = red / (blue + red)

print("The area is: ", 42 * ratio)
