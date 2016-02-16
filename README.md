# OEIS Lookup
[![Code Review](http://www.zomis.net/codereview/shield/?qid=120102)](http://codereview.stackexchange.com/q/120102/74474)  
A tool for looking up sequences in OEIS

## Notes

I'm so sorry, I'm using Regex to parse the html :'(  
I'm so sorry, I'm using Python 2

## Usage

```
python lookup.py <sequence id> <item>
```

Where `sequence id` is an integer representing the sequence's number and `item` represents the input

## Dependencies
This is written in Python, it requires:
 - `urllib2`
 - `lxml`
 - `beautifulsoup4`
