from PIL import Image

def resizing_image(image):
    with Image.open(image) as im:

        # Provide the target width and height of the image
        (width, height) = (im.width * 2, im.height * 2)
        im_resized = im.resize((width, height))

        return  im_resized.save('cafe.png')

link_to_image = 'cafe.png'
resizing_image(link_to_image)