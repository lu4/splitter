#!/usr/bin/env python3

import os
import sys
from datetime import datetime

names = {}

prefix_a = 'a--->'
prefix_w = 'w--->'
prefix_s = 's--->'
prefix_A = 'A--->'
prefix_W = 'W--->'
prefix_S = 'S--->'

f = sys.stdout

for line in sys.stdin:
    name = None
    mode = None

    if line.startswith((prefix_a, prefix_w, prefix_s, prefix_A, prefix_W, prefix_S)):
      line_strip = line.strip(' \n')
      mode, name = line_strip.split('--->')
      name = name.strip(' ')

    if mode and name:
      if f != sys.stdout:
        f.close()

      if mode == 's' or mode == 'S':
        f = sys.stdout
      else:
        actual_name = names.get(name) if mode.islower() else name

        if not actual_name:
            actual_name = name + '.' + datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
            names[name] = actual_name

        if mode == 'w' and os.path.exists(actual_name):
          os.rename(actual_name, actual_name + '.dead-since.' + datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f'))

        f = open(actual_name, mode.lower() + '+')
    else:
      f.write(line)

    if f != sys.stdout:
      sys.stdout.write(line)

if f != sys.stdout:
  f.close()
