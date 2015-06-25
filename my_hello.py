#!/usr/bin/env python

'''
Created on 24 Jun 2015

@author: brian
'''

import sys 

def main():
  if len(sys.argv) > 2:
    print "Hello", sys.argv[1]
  else:
    print "Hello, there"

if __name__ == "__main__":
  main()