#!/usr/bin/env python3

import base64
import sys

powershell_launcher_string = "powershell.exe -version 2 -exec bypass -enc "
powershell_plain_string = sys.argv[1]

powershell_encoded_string = powershell_launcher_string + base64.b64encode(powershell_plain_string.encode("UTF-16LE")).decode("utf-8")

print(powershell_encoded_string)
