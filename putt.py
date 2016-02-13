import urllib2
import sys

LANGNAME = "Putt" # The language name

# TODO: Make experimental encoder

# Main logic
def execute(code):
  # Decode input stuff
  num = int(code) # TODO: improve decoder
  try:
    url = urllib2.urlopen("http://oeis.org/A%06d/list" % num);
    data = url.read()
    url.close()
    print data
  except urllib2.HTTPError:
    print "Could not find sequence A%06d" % num
  except urllib2.URLError:
    print "Could not connect to sources";
  except:
    print "Verify your numbers are correct"
    url.close()

# Determines what do with the source code
def determine(code):
  PYTHON_KEYWORD = "PYTHON" # To run code as Python
  if code.isdigit():
    execute(code);
  elif code.startswith(PYTHON_KEYWORD):
    exec(code[int(len(PYTHON_KEYWORD)):])
  else:
    raise ValueError('%s could not parse the input' % LANGNAME);

if __name__ == '__main__':
  if len(sys.argv) > 1:
    determine(sys.argv[1])
  else:
    print """This is the %s interpreter
You haven't entered any code.""" % (LANGNAME)
