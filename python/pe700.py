#!/usr/bin/env python3
import argparse

from itertools import islice

def coins(a, b):
  n = 1
  while True:
    an = a*n % b
    # nlimit = find_smaller_an(a, b, n)
    yield an
    n += 1

def find_n(a, b, x):
  '''Find n s.t. an = x (mod b).'''
  return (pow(a, -1, b) * x) % b


if __name__ == '__main__':
  a = 1504170715041707
  b = 4503599627370517
