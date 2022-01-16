#!/usr/bin/env python3.8

import subprocess

list_files = subprocess.run(["ping", "-c 4", "8.8.8.8"])
print("The exit code was: %d" % list_files.returncode)








