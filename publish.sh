#!/bin/bash
# Generate site with *publish* settings, then upload generated site to S3
pelican content/ -o html -s publishconf.py --debug \
    && sh ~/jets3t/bin/synchronize.sh UP --acl public_read james.murty.co html/*
