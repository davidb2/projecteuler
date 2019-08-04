#!/usr/bin/env
import itertools

def tts(n):
  x = list(itertools.product(0, 1), repeat=n)
  for result in x:
    for i in range(len(result)):
      x[i] == result[i]:
