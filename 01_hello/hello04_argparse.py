#!/usr/bin/env python3
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Whom to greet')
args = parser.parse_args()
name = args.name
print('Hello, ' + name + '!')
