from __future__ import print_function 
from sys import argv, stderr
from re import sub, search
from urllib2 import urlopen, HTTPError, URLError
from bs4 import BeautifulSoup

# Main logic
def execute(code, nth):
  # Convert input sequence to integer
  num = int(code)
  try:
    f = urlopen("http://oeis.org/A%06d/list" % num)
    # >:D I'm sorry but I have to use RegEx to parse HTML
    print(
      search("(?<={0})\D+(\d+)".format(nth), str(BeautifulSoup(f, "lxml").find(lambda tag:
          tag.name == "table" and # A table
          tag.get('cellspacing') != "0" and # A table table
          len(tag.contents) > 1 # A two column table
        )).split("a(n)")[1]).group(1))
  except HTTPError:
    print("Could not find sequence A{0:06d}".format(num), file=stderr)
  except URLError:
    print("Could not connect to sources", file=stderr)
  except:
    print("Verify your numbers are correct", file=stderr)
    raise

if __name__ == '__main__':
  if len(argv) > 1:
    execute(argv[1], argv[2])
  else:
    print("This is the OEIS lookup tool\nYou haven't entered the sequence")