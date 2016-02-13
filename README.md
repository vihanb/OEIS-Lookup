# OEIS Lookup
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
