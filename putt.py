import urllib2
import sys

LANGNAME = "Putt" # The language name

# Determines what do with the source code
def determine(code):
  PYTHON_KEYWORD = "PYTHON" # To run code as Python
  if code.isdigit():
    execute(code);
  elif code.startswith(PYTHON_KEYWORD):
    exec(code[int(len(PYTHON_KEYWORD)):])
  else:
    raise ValueError('%s could not parse the input' % LANGNAME)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    determine(sys.argv[1])
  else:
    print """This is the %s interpreter
    You haven't entered any code.""" % (LANGNAME)
