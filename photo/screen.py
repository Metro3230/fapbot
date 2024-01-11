from PIL import Image

img = Image.open('test.jpg')
hand = Image.open('hand.png')

zeropoint = int(img.size[0] - hand.size[0])

img.paste(hand, (0, zeropoint),  hand)
img.save("img_with_hand.png") 


