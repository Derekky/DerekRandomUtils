# Script to test the argparse module
# Very useful for command line arguments

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--append", action= "store_true", help= "appends instead of writing over output file", default=False)
parser.add_argument("inputs", type=argparse.FileType('r'), nargs="+", help="one or more input text files, example: log-1.txt log-2.log")
args = parser.parse_args()

print("test...")
if(args.append):
    print("Appending...")

for inputs in args.inputs:
    print(inputs)