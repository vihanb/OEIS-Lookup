# I suck at python big time.
# Please tell me if I can do this better

import urllib2
import sys

LANGNAME = "Putt" # The language name

def determine(code): # Determines what do with the source code
  pass

if __name__ == '__main__':
  if len(sys.argv) > 1:
    determine(code)
    else:
      print """This is the %s interpreter
You haven't entered any code.""" % (LANGNAME)