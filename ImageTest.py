import  PIL as pillow
from collections import defaultdict
from PIL import Image

def fillImage():
		# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
	img = Image.new( 'RGB', (250,250), "black") # create a new black image
	pixels = img.load() # create the pixel map

	for i in range(img.size[0]):    # for every col:
	    for j in range(img.size[1]):    # For every row
	        pixels[i,j] = (i, j, 100) # set the colour accordingly

	img.show()




def getImage(name):

	img = Image.open(name)
	by_color = defaultdict(int)
	imgColor = Image.new( 'RGB', (250,250), "black") # create a new black image
	major=0;
	for pixel in img.getdata():
		by_color[pixel] +=1
	all_keys = list(by_color.keys())
	all_colors = list(by_color.values())
	for i in range(1,len(all_colors)):
		print(all_colors[i])
		if(all_colors[i] > major):
			major = all_colors[i]
			color = all_keys[i]

	pixelImage = imgColor.load()

	for i in range(imgColor.size[0]):    # for every col:
	    for j in range(imgColor.size[1]):    # For every row
	        pixelImage[i,j] = color # set the colour accordingly
	imgColor.show()


def main():
	getImage('yolo.jpg')
	return 0


if __name__ ==  '__main__':
	main()