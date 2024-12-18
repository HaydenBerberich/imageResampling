usage: main.py [-h] [-s {1,2}] [-d DEPTH] [-i {1,2,3,4,5,6,7}] imagefile

Image Sampling and Quantization

positional arguments:
  imagefile             Path to the image file

options:
  -h, --help            show this help message and exit
  -s {1,2}, --sampling_method {1,2}
                        Sampling method; 1 for pixel deletion/replication, 2 for pixel averaging/interpolation
                        [default: 1]
  -d DEPTH, --depth DEPTH
                        Number of levels for downsampling [default: 1]
  -i {1,2,3,4,5,6,7}, --intensity {1,2,3,4,5,6,7}
                        Intensity levels, between 1 and 7 [default: 1]

Observations/Conclusions: Downsampling with pixel deletion and upsampling with pixel replication loses
quality with each subsequent downsample. This method creates blocky pixelated images. Downsampling with
pixel averaging and upsampling with interpolation gradually decreases the quality of the photo
with each downsample/upsample. This method creates a blurred image. In the photo of Michael Jordan
using method 1, you are able to notice the blocky pixelation at the first depth. On depth 5, the 
image is barely recognizable. In the photo of Michael Jordan using method 2, you can notice the 
blurring immediately at the first depth. On depth 5, the image is more recognizable than the method 1
but still very hard to makout. 
