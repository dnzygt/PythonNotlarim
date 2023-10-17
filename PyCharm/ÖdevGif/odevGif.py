

from PIL import Image

image_path_list = ["img.png","img_1.png"]
image_list = [Image.open(file)for file in image_path_list]
image_list[0].save(
    "animation.gif",
    save_all=True,
    append_images = image_list[:],
    duration = 100,
    loop = 0
)



