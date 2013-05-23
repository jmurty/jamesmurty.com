#!/bin/bash
# Generate site with *dev* settings
pelican content/ -o html -s pelicanconf.py --debug
