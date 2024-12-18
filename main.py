# Hayden Berberich
# 10/9/2024

import cv2
from utils import parse_arguments
from image_processing import (
    downsample_pixel_deletion,
    upsample_pixel_replication,
    downsample_pixel_averaging,
    upsample_interpolation,
    intensity_downsampling
)

def main():
    args = parse_arguments()
    
    try:
        # Load the image
        image = cv2.imread(args.imagefile, cv2.IMREAD_UNCHANGED)
        if image is None:
            raise ValueError("Image not found or unable to load.")
        
        # If depth is 0, perform intensity downsampling if specified
        if args.depth == 0:
            image = intensity_downsampling(image, args.intensity)
            cv2.imshow('Intensity Downsampled Image', image)
            cv2.waitKey(0)
        else:
            # Downsample the image for the specified number of times
            for i in range(args.depth):
                # Apply downsampling
                if args.sampling_method == 1:
                    image = downsample_pixel_deletion(image)
                elif args.sampling_method == 2:
                    image = downsample_pixel_averaging(image)
                
                # Apply intensity downsampling
                image = intensity_downsampling(image, args.intensity)
                
                # Display the downsampled image
                cv2.imshow(f'Downsampled Level {i+1}', image)
                cv2.waitKey(0)
            
            # Upsample the image and display at each depth
            for i in range(args.depth):
                if args.sampling_method == 1:
                    image = upsample_pixel_replication(image)
                elif args.sampling_method == 2:
                    image = upsample_interpolation(image)
                
                # Display the upsampled image
                cv2.imshow(f'Upsampled Level {i+1}', image)
                cv2.waitKey(0)
        
        # Close all OpenCV windows
        cv2.destroyAllWindows()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()