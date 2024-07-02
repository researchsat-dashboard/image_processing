from PIL import Image

def image_stitch():
    image1 = Image.open('image1.jpg')
    image2 = Image.open('image2.jpg')
    image3 = Image.open('image3.jpg')
    image4 = Image.open('image4.jpg')
    image5 = Image.open('image5.jpg')
    image6 = Image.open('image6.jpg')
    image7 = Image.open('image7.jpg')
    image8 = Image.open('image8.jpg')
    image9 = Image.open('image9.jpg')

    collage_width = image1.width
    collage_height = image1.height

    smaller_size = (232, 173)
    smaller_image_width = 232
    smaller_image_height = 173

    new_image = Image.new('RGB', (696, 520))

    image1 = image1.resize(smaller_size)
    image2 = image2.resize(smaller_size)
    image3 = image3.resize(smaller_size)
    image4 = image4.resize(smaller_size)
    image5 = image5.resize(smaller_size)
    image6 = image6.resize(smaller_size)
    image7 = image7.resize(smaller_size)
    image8 = image8.resize(smaller_size)
    image9 = image9.resize(smaller_size)

    new_image.paste(image1, (0,0))
    new_image.paste(image2, (smaller_image_width, 0))
    new_image.paste(image3, (smaller_image_width * 2, 0))
    new_image.paste(image4, (0, smaller_image_height))
    new_image.paste(image5, (smaller_image_width, smaller_image_height))
    new_image.paste(image6, (smaller_image_width * 2, smaller_image_height))
    new_image.paste(image7, (0, smaller_image_height * 2))
    new_image.paste(image8, (smaller_image_width, smaller_image_height * 2))
    new_image.paste(image9, (smaller_image_width * 2, smaller_image_height * 2))

    new_image.save('collage.jpg')