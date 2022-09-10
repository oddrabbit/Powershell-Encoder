#!/usr/bin/env python3

import base64
import argparse

parser = argparse.ArgumentParser(description = "Script to create a base64 Powershell one-liner")
parser.add_argument("-c", type = str, required = True)
parser.add_argument("--command", type = str, required = True)
args = parser.parse_args()

powershell_launcher_string = "powershell.exe -version 2 -exec bypass -enc "

if args.c:
    powershell_encoded_string = powershell_launcher_string + base64.b64encode(args.c.encode("UTF-16LE")).decode("utf-8")
elif args.command:
    powershell_encoded_string = powershell_launcher_string + base64.b64encode(args.command.encode("UTF-16LE")).decode("utf-8")

print(powershell_encoded_string)
