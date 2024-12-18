import numpy as np

# Function to downsample the image by removing alternate rows and columns
def downsample_pixel_deletion(image):
    return image[::2, ::2]

# Function to upsample the image by replicating pixels
def upsample_pixel_replication(image):
    height, width = image.shape[:2]
    channels = 1 if len(image.shape) == 2 else image.shape[2]
    
    # Create an empty image of size (2 * height, 2 * width)
    if channels == 1:
        upsampled_image = np.zeros((2 * height, 2 * width), dtype=image.dtype)
    else:
        upsampled_image = np.zeros((2 * height, 2 * width, channels), dtype=image.dtype)
    
    # Copy each pixel to the corresponding four pixels in the upsampled image
    for x in range(height):
        for y in range(width):
            if channels == 1:
                upsampled_image[2 * x, 2 * y] = image[x, y]
                upsampled_image[2 * x + 1, 2 * y] = image[x, y]
                upsampled_image[2 * x, 2 * y + 1] = image[x, y]
                upsampled_image[2 * x + 1, 2 * y + 1] = image[x, y]
            else:
                for c in range(channels):
                    upsampled_image[2 * x, 2 * y, c] = image[x, y, c]
                    upsampled_image[2 * x + 1, 2 * y, c] = image[x, y, c]
                    upsampled_image[2 * x, 2 * y + 1, c] = image[x, y, c]
                    upsampled_image[2 * x + 1, 2 * y + 1, c] = image[x, y, c]
    
    return upsampled_image

# Function to downsample the image by averaging pixels
def downsample_pixel_averaging(image):
    height, width = image.shape[:2]
    channels = 1 if len(image.shape) == 2 else image.shape[2]
    
    # Create an empty image of size (height // 2, width // 2)
    downsampled_image = np.zeros((height // 2, width // 2, channels), dtype=image.dtype)
    
    # Calculate the average of each 2x2 block of pixels
    for x in range(0, height, 2):
        for y in range(0, width, 2):
            block_sum = image[x, y].astype(np.float32)
            count = 1
            
            if x + 1 < height:
                block_sum += image[x + 1, y].astype(np.float32)
                count += 1
            if y + 1 < width:
                block_sum += image[x, y + 1].astype(np.float32)
                count += 1
            if x + 1 < height and y + 1 < width:
                block_sum += image[x + 1, y + 1].astype(np.float32)
                count += 1
            
            downsampled_image[x // 2, y // 2] = (block_sum / count).astype(image.dtype)
    
    # If the image is grayscale, remove the last dimension
    if channels == 1:
        downsampled_image = downsampled_image[:, :, 0]
    
    return downsampled_image

# Function to upsample the image by interpolation
def upsample_interpolation(image):
    height, width = image.shape[:2]
    channels = 1 if len(image.shape) == 2 else image.shape[2]
    
    # Create an empty image of size (2 * height, 2 * width)
    upsampled_image = np.zeros((2 * height, 2 * width, channels), dtype=image.dtype)
    
    # Interpolate pixel values
    for x in range(height):
        for y in range(width):
            upsampled_image[2 * x, 2 * y] = image[x, y]
            
            if x + 1 < height:
                upsampled_image[2 * x + 1, 2 * y] = ((image[x, y].astype(np.float32) + image[x + 1, y].astype(np.float32)) / 2).astype(image.dtype)
            if y + 1 < width:
                upsampled_image[2 * x, 2 * y + 1] = ((image[x, y].astype(np.float32) + image[x, y + 1].astype(np.float32)) / 2).astype(image.dtype)
            if x + 1 < height and y + 1 < width:
                upsampled_image[2 * x + 1, 2 * y + 1] = ((image[x, y].astype(np.float32) + image[x + 1, y].astype(np.float32) + image[x, y + 1].astype(np.float32) + image[x + 1, y + 1].astype(np.float32)) / 4).astype(image.dtype)
    
    # If the image is grayscale, remove the last dimension
    if channels == 1:
        upsampled_image = upsampled_image[:, :, 0]
    
    return upsampled_image

# Function to reduce the intensity resolution of the image
def intensity_downsampling(image, n):
    return (image >> n) << n