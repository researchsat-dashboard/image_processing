from PIL import Image

image1 = Image.open('image1.tiff')
image2 = Image.open('image2.tiff')
image3 = Image.open('image3.tiff')
image4 = Image.open('image4.tiff')
image5 = Image.open('image5.tiff')
image6 = Image.open('image6.tiff')

new_image_width = image1.width * 3
new_image_height = image1.height * 2

new_image = Image.new('RGB', (new_image_width, new_image_height))

new_image.paste(image1, (0,0))
new_image.paste(image2, (image1.width, 0))
new_image.paste(image3, (2 * image1.width, 0))
new_image.paste(image4, (0, image1.height))
new_image.paste(image5, (image1.width, image1.height))
new_image.paste(image6, (2 * image1.width, image1.height))

new_image.save('new_image.jpg')