#!/usr/bin/env python3

import argparse

'''
This program is free software: you can redistribute it and/or modify it under the terms of the 
GNU General Public License as published by the Free Software Foundation, version 2 of the 
License.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>. 
'''

def argument_parser():
    parser = argparse.ArgumentParser(description = "Creates a base64 Powershell one-liner given plaintext input")
    parser.add_argument("-c", type = str, help = "Plaintext command to base64 encode", required = False)
    parser.add_argument("--command", type = str, help = "Plaintext command to base64 encode", required = False)
    parser.add_argument("-f", type = str, help = "File including command to base64 encode", required = False)
    parser.add_argument("--file", type = str, help = "File including command to base64 encode", required = False)
    args = parser.parse_args()
    return args

def main():
    args = argument_parser()

    powershell_launcher_string = "powershell.exe -version 2 -exec bypass -enc "

    if args.c or args.command:
        powershell_encoded_string = powershell_launcher_string + base64.b64encode(args.c.encode("UTF-16LE")).decode("utf-8")
        print(powershell_encoded_string)
        quit()

    if args.f:
        file_handler = open(args.f, "r")
        file_handler_content = file_handler.readlines()
        file_handler_content = "\n".join(str(i) for i in file_handler_content)
        powershell_encoded_string = powershell_launcher_string + base64.b64encode(file_handler_content.encode("UTF-16LE")).decode("utf-8")
        print(powershell_encoded_string)
    elif args.file:
        file_handler = open(args.file, "r")
        file_handler_content = file_handler.readlines()
        file_handler_content = "\n".join(str(i) for i in file_handler_content)
        powershell_encoded_string = powershell_launcher_string + base64.b64encode(file_handler_content.encode("UTF-16LE")).decode("utf-8")
        print(powershell_encoded_string)

if __name__ == "__main__":
    main()
