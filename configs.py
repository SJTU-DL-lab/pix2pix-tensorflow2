import argparse

parser = argparse.ArgumentParser(description="args for pix2pix")
parser.add_argument('--output_channels', type=int, default=3)
parser.add_argument('--lbd', type=int, default=100)

args = parser.parse_args()
