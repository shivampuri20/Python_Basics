import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890


Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat 
mat
pat 
'''


sentence ='Start a sentence and then bring it t an end '

#pattern=re.compile(r'abc')    #for special characters we use \  i.e '\.' 
#pattern=re.compile(r'\W')
#pattern=re.compile(r'\bHa')
pattern=re.compile(r'^Start')  #in sentence
#pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern=re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
#pattern=re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
#pattern=re.compile(r'[cmp]at')

#using quantifers
#pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

#for emails
#pattern=re.compile(r'https?://(www\.)?(\w+)(\.w+)')

#matches=pattern.finditer(urls)
#matches=pattern.findall(text_to_search)
#matches=pattern.match(sentence)
matches=pattern.search(sentence)

#print match
print matches


#for match in matches:
 #  print match 



















