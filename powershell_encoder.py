#!/usr/bin/env python3

import argparse
import base64
import sys

def argument_parser():
    parser = argparse.ArgumentParser(description = "Script to create a base64 Powershell one-liner")
    parser.add_argument("-h", type = str, required = False)
    parser.add_argument("--help", type = str, required = False)
    parser.add_argument("-c", type = str, required = False)
    parser.add_argument("--command", type = str, required = False)
    args = parser.parse_args()
    return args

def main():
    args = argument_parser()
    
    if args.h or args.help:
    print("Usage: <" + sys.argv[1] + " [Flags: -c | --command] [argument]")
    print("Flags and arguments:")
    print("-c, --command    : Plain text Powershell string to base64 encode.")
    print("-h, --help       : Print the help page")
    quit()
    
    powershell_launcher_string = "powershell.exe -version 2 -exec bypass -enc "

    if args.c or args.command:
        powershell_encoded_string = powershell_launcher_string + base64.b64encode(args.c.encode("UTF-16LE")).decode("utf-8")

    print(powershell_encoded_string)

if __name__ == "__main__":
    main()
