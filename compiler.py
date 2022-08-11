#!/usr/bin/env python3
"""
THIS IS A DOCSTRING THAT MIGHT BE USEFULL IN THE FUTURE
"""
#NOTE: this is trash. all of it. srsly
#TODO: where version? docstring? 

def str_to_int(s:str): #TODO: delete it, STUPID–ME, USE INT()
    """
    Very slow way of converting the a string that represents
    a binary number into the actual binary number, but wfm
    """
    byte=0
    for b in s:
        byte = byte << 1
        if b == "1":
            byte+=1
    return byte



#TODO: make this function usefull without globals
def compile():
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
        #calculate the binary representation of the number
        binary_char_count_str = bin(c)[2:]
        #split the binary number in bytes for bytearray
        binary_cc_str_array = [binary_char_count_str[i:i+8] for i in range(0, len(binary_char_count_str),  8)]
        #FIXME: last byte gets cut off
        #convert the strings to integers that represent a byte each
        binary_array = [int(e,  2) for e in binary_cc_str_array]
        #write the array to the output file
        bt_a = bytearray(binary_array)
        out_f.write(bt_a)
 
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str,  help="RTFM")
    parser.add_argument("-o",  "--output",  type=str,  help="RTFM")
    #DOCU: explain encoding in docs
    parser.add_argument("-e",  "--encoding",  type=str, default="ASCII", help="RTFM")
    #TODO: Pass super-char as hex (easier for some) (optional)
    #DOCU: define super-keys in docs
    parser.add_argument("-c",  "--superchar",  type=str,  default="E",  help="RTFM")
    args=parser.parse_args()

    compile()
