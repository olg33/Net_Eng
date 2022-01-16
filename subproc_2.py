#!/usr/bin/env python3.8

import subprocess

list_files = subprocess.run(["ping", "-c 4", "8.8.8.8"], stdout=subprocess.PIPE, text=True)
print(list_files.stdout)








