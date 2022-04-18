import PIL
import glob, os

from PIL import Image
#im = Image.open("0.png")

x=""
count=0
for infile in glob.glob("*.png"):
	print(infile)
	x=infile
	
	im = Image.open(x)

	width, height = im.size   # Get dimensions

	left = 60
	top = 0
	right = width
	bottom = height

	# Crop the center of the image
	im = im.crop((left, top, right, bottom))
	newsize = (640, 512)
	im =im.resize(newsize)
	new="%06d" % count
	count=count+1
	#im.show()
	newDir="/home/youssef/Desktop/cropImage/new/"+str(new)+".png"
	im.save(newDir)



