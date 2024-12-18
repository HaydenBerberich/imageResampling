import argparse

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Image Sampling and Quantization')
    parser.add_argument('-s', '--sampling_method', type=int, choices=[1, 2], default=1, help='Sampling method; 1 for pixel deletion/replication, 2 for pixel averaging/interpolation [default: 1]')
    parser.add_argument('-d', '--depth', type=int, default=1, help='Number of levels for downsampling [default: 1]')
    parser.add_argument('-i', '--intensity', type=int, choices=range(1, 8), default=1, help='Intensity levels, between 1 and 7 [default: 1]')
    parser.add_argument('imagefile', type=str, help='Path to the image file')
    return parser.parse_args()