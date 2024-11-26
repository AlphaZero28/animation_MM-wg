"""
 * author: Ohidul Islam
 * created on 26-11-2024-15h-49m
 * copyright 2024
"""
from csv2img import csv_load, create_image_from_data
import matplotlib.pyplot as plt
import os
from img_processing import load_image, crop_image
from matplotlib.animation import FuncAnimation, FFMpegWriter
plt.rcParams.update({"font.family": "Times New Roman", "font.size": 18})
plt.rcParams["animation.ffmpeg_path"] = "C:/Program Files/ffmpeg/bin/ffmpeg.exe"


PROPAGATION_DIRECTION = 'backward'  # 'forward' or 'backward'
##########################################################
# image creation from csv file
#############################################################
N_images = 6
N = 2**12
img_folder = 'images/field profile'

for i in range(1, N_images+1):

    # CSV FILE load
    if PROPAGATION_DIRECTION == 'forward':
        csv_path = f"data\ewfd_Hz_data_ExcitedPort{i}.csv"
        img_filename = f'{img_folder}/forward_port{i}.png'

    elif PROPAGATION_DIRECTION == 'backward':
        csv_path = f"data\ewfd_Hz_data_back_prop_port{i}.csv"
        img_filename = f'{img_folder}/backward_port{i}.png'

    if not os.path.exists(img_filename):
        [x, y, abs_hz] = csv_load(path=csv_path)

        # image creation
        create_image_from_data(
            points=N, x=x, y=y, data=abs_hz, filename=img_filename)
        print(f"image created \t {i}\{N_images}")

    else:
        print(f"Image already exists: {i}/{N_images}")

###############################################################
# making animation
###############################################################

####################### load images ############################
images = []
title = ''
for i in range(N_images):

    if PROPAGATION_DIRECTION == 'foward':
        img_path = f"{img_folder}/forward_port{i+1}.png"
        title = "Propagation: left to right"

    elif PROPAGATION_DIRECTION == 'backward':
        img_path = f"{img_folder}/backward_port{i+1}.png"
        title = "Propagation: right to left"

    img = load_image(path=img_path)

    img = crop_image(image=img, top_left_corner=(
        0, 0), bottom_right_corner=(2500, 1400))

    images.append(img)

    # Display the image
    # plt.imshow(img, cmap="jet", interpolation='bilinear')

fig, ax = plt.subplots()
im = ax.imshow(images[0], cmap='hot', interpolation='bilinear')
ax.set_axis_off()

ax.set_title(title)
plt.tight_layout()


# Animation update function
def update(frame):
    im.set_data(images[frame])
    return [im]


# Create the animation
anim = FuncAnimation(
    fig=fig, func=update, frames=6, interval=1000
)
metadata = dict(title="Multimode Waveguide", artist="forward propagation")
writer = FFMpegWriter(fps=1, metadata=metadata)

anim.save(f"images/{PROPAGATION_DIRECTION}_prop.mp4", writer=writer, dpi=300)


plt.show()
