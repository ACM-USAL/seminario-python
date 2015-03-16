#!/usr/bin/env python3
# -*- coding: utf-8 -*-

i = 7
def fibonacci(i):
  if i < 2:
    return i 
  return fibonacci(i-1) + fibonacci(i-2) 

print(fibonacci(i))
