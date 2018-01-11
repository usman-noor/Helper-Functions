# https://www.youtube.com/watch?v=K8L6KVGG-7o

import re 

MetaCharacters (Need to be escaped for literal matches):
.[{()\^$|?*+

text_to_search = 'abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
Ha HaHa
coreyms.com
321-555-4321
123.555.1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T'   
   
#raw string 
print (r'\tTab') # will print the string as it is 

pattern = re.compile(r'abc') 


matches = pattern.finditer(text_to_search) # will create an iterable of all the matches 

for match in matches:
  print (match)
  
# span shows where the match was found(0:3) 

pattern = re.compile(r'coreyms\.com')  # to escape the dot character 

'''
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

Anchors:find invisible positions before or after 
\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
'''

pattern = re.compile(r'\bHA') 

# it will match two HA one at the start of string other after the space "HA HAHA" 
pattern = re.compile(r'\bHA') 
# it will match one HA with no word boundry at index 5 and 6 "HA HAHA" 

'%[^0-9a-zA-Z,.]%'   

