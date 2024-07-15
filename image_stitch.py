from PIL import Image
from datetime import datetime

def image_stitch():

    current_dt = datetime.now()
    current_dt_string = current_dt.strftime("%Y.%m.%d_%H.%M.%S-collage.jpg")

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

    new_image = Image.new('RGB', (2088, 2010))

    new_image.paste(image1, (0,0))
    new_image.paste(image2, (collage_width, 0))
    new_image.paste(image3, (collage_width * 2, 0))
    new_image.paste(image4, (0, collage_height))
    new_image.paste(image5, (collage_width, collage_height))
    new_image.paste(image6, (collage_width * 2, collage_height))
    new_image.paste(image7, (0, collage_height * 2))
    new_image.paste(image8, (collage_width, collage_height * 2))
    new_image.paste(image9, (collage_width * 2, collage_height * 2))

    new_image.save(current_dt_string)