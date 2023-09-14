from PIL import Image

image_path_list = ["stickman1.jpg", "stickman2.jpg", "stickman3.jpg", "stickman4.jpg"]
image_list = [Image.open(file) for file in image_path_list]
image_list[0].save(
            'animation.gif',
            save_all=True,
            append_images=image_list[1:],
            duration=240,
            loop=999)
