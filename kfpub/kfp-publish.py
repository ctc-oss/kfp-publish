#!/usr/bin/env python

import configargparse as argparse

import kfp

parser = argparse.ArgumentParser()
parser.add_argument('name', help='Pipeline name')
parser.add_argument('file', type=str, help='Path to pipeline file')
args = parser.parse_args()

kfp.Client().upload_pipeline(args.file, args.name)
