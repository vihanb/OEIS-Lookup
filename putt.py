#!/usr/bin/python
import sys, re
from urllib2 import*
from bs4 import BeautifulSoup

LANGNAME = "Putt" # The language name

# TODO: Make experimental encoder

# Main logic
def execute(code, nth):
  # Decode input stuff
  num = int(code) # TODO: improve decoder
  try:
    f = urlopen("http://oeis.org/A%06d/list" % num)
    # global tree, data # Debugging
    # >:D I'm sorry but I have to use RegEx to parse HTML
    print {key: int(value) for key, value in
      re.findall( r'(\d+) (\d+)', re.sub(r'\D+', " ", re.sub(r'<[^>]+>', "",
        str(BeautifulSoup(f, "lxml").find(lambda tag:
          tag.name == "table" and # A table
          not tag.get('cellspacing') == "0" and # A table table
          len(tag.contents) > 1 # A two column table
        ))
      )) )
    }[nth]
  except HTTPError:
    print "Could not find sequence A%06d" % num
  except URLError:
    print "Could not connect to sources";
  except:
    print "Verify your numbers are correct"
    raise

# Determines what do with the source code
def determine(code, inpt):
  PYTHON_KEYWORD = "PYTHON" # To run code as Python
  if code.isdigit():
    execute(code, inpt);
  elif code.startswith(PYTHON_KEYWORD):
    exec(code[int(len(PYTHON_KEYWORD)):])
  else:
    raise ValueError('%s could not parse the input' % LANGNAME);

if __name__ == '__main__':
  if len(sys.argv) > 1:
    determine(sys.argv[1], sys.argv[2])
  else:
    print """This is the %s interpreter
You haven't entered any code.""" % (LANGNAME)
