#!/usr/bin/python
import sys, re
from urllib2 import*
from bs4 import BeautifulSoup

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
    }.get(nth, "OEIS does not have a number in the sequence at the given index")
  except HTTPError:
    print "Could not find sequence A%06d" % num
  except URLError:
    print "Could not connect to sources";
  except:
    print "Verify your numbers are correct"
    raise

if __name__ == '__main__':
  if len(sys.argv) > 1:
    execute(sys.argv[1], sys.argv[2])
  else:
    print """This is the OEIS lookup tool
You haven't entered the sequence""" % (LANGNAME)
