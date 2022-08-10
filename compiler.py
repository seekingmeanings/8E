#!/usr/bin/env python3
"""
THIS IS A DOCSTRING THAT MIGHT BE USEFULL IN THE FUTURE
"""
#NOTE: this is trash. all of it. srsly
#TODO: where version? docstring? 
import struct
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str,  help="RTFM")
parser.add_argument("-o",  "--output",  type=str,  help="RTFM")
#DOCU: explain encoding in docs
parser.add_argument("-e",  "--encoding",  type=str, default="ASCII", help="RTFM")
#TODO: Pass super-char as hex (easier for some)
#DOCU: define super-keys in docs
parser.add_argument("-c",  "--superchar",  type=str,  default="E",  help="RTFM")
args=parser.parse_args()

#TODO: Implement other encodings
if not args.superchar.isascii() and args.encoding != "ASCII":
    raise RuntimeError("only ASCII super-characters and ASCII encoding works")

"""
Analyze source code and compile
"""
c=0
with open(args.input,  mode='rt',  encoding=args.encoding) as src_f:
    for line in src_f:
        c += line.count(args.superchar)

"""
Build the compiled output file
"""
#WARNING: no owerwrite protection
with open(args.output,  mode='wb') as out_f:
    out_f.write(c)
