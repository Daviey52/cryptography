import re

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
      character = re.sub(r'[^A-Za-z]+', ' ', char)
      encrypted_text += char
  return encrypted_text


def decrypt(plain_text,key):
  return encrypt(plain_text, -key)


def crack(encrypted):
  pass
