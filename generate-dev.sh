#!/bin/bash
# Generate site with *dev* settings
pelican content/ -o html-dev -s pelicanconf.py --debug
