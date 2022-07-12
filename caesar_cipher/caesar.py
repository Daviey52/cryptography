## download regex and natural language tool kit
import re ,nltk ,ssl

from nltk.corpus import words,names 

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

## Could have used ASCII instead of hardcoded Lower case
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper_case =[]
for letter in lower_case:
   upper_case.append(letter.upper())

def encrypt(plain_text , key):
  encrypted_text = ''

  for char in plain_text:
    if char in lower_case:
      character =(lower_case.index(char) + key) % 26
      encrypted_text += lower_case[character]
    elif char in upper_case:
      character =(upper_case.index(char) + key) % 26
      encrypted_text += upper_case[character]
    else:
      character = re.sub(r'[^A-Za-z]+', ' ', char) # handle whilteshpace and ignore characters
      encrypted_text += char
  return encrypted_text


def decrypt(plain_text,key):
  return encrypt(plain_text, -key)


def crack(plain_text):
  word_list = nltk.words()
  res = ''
  max_word_matched = 0

  for key in range(1,26):
    decrypted = decrypt(plain_text,key)
    word_matched = 0
    for word in decrypted.split(''):
      if word in word_list:
        word_matched += 1
    
    if word_matched > len(plain_text)//2: # if more than 50% match exit 
      return decrypted

    elif word_matched> max_word_matched: # otherwise return the decription with the most match
      max_word_matched= word_matched
      res = decrypted

  return res
