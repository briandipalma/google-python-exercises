#!/usr/bin/env python

'''
Created on 24 Jun 2015

@author: brian
'''

import sys 

def repeat(s, exclaim):
  """
  Returns the string 's' repeated 3 times.
  If exclaim is true, add exclamation marks.
  """
  
  result = s + s + s
  
  if exclaim:
    result += "!!!"

  return result

def main():
  if len(sys.argv) >= 2:
    print "Hello,", sys.argv[1]
  else:
    print "Hello, there"
    print repeat("Hi", True)
    
    result = "Test"
    
    print result

if __name__ == "__main__":
  main()
