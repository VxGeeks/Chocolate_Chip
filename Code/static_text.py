#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-17 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Simple println capabilities.
"""

import os
import time
from demo_opts import get_device
from luma.core.render import canvas
from PIL import ImageFont


def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)


def main():
        for fontname, size in [("SourceCodePro-Regular.ttf", 24)]:
            font = make_font(fontname, size)

	text = "Tiny"
	with canvas(device) as draw:
		draw.rectangle(device.bounding_box,outline="white",fill="black")
		draw.text((2,2),text,font=font,fill="white")

	while 1:
		time.sleep(2)
if __name__ == "__main__":
    try:
        device = get_device()
	device.contrast(255)
        main()
    except KeyboardInterrupt:
        pass
