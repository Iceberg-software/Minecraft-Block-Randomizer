import argparse
from GenerateBlock import CreateNewBlock

parser = argparse.ArgumentParser(description="Generate new minecraft content")
parser.add_argument("cycles", metavar='N', type=int, help="Amount of blocks to create")
args = parser.parse_args()

CreateNewBlock(args.cycles)

