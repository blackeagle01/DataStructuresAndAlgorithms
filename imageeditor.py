from PIL import Image,ImageFilter
im=Image.open('abc1.jpg')
im1=im.filter(ImageFilter.MedianFilter(3))
im1.show()