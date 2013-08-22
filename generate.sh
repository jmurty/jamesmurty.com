#!/bin/bash
# Generate site with *production* settings
pelican content/ -o html -s publishconf.py
