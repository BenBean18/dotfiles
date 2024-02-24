#!/usr/bin/env python3
import subprocess

this_profile = subprocess.check_output(["powerprofilesctl", "get"])

this_profile = this_profile.decode("utf-8").replace("\n", "")

text = ""

if this_profile == "power-saver":
    text = "" # leaf
elif this_profile == "balanced":
    text = "" # balance
elif this_profile == "performance":
    text = "" # space shuttle :)
else:
    text = this_profile

j = "{" + f""""text": "{text}", "tooltip": "{this_profile}", "class": "{this_profile}", "percentage": 0.0""" + "}"

print(j)