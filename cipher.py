#The purpose of this program is to encrypt a given message using the Caesar Cipher technique

import sys
#import sys

def caesar_cipher(message, shift):
      result = ""
      for i in range(len(message)):
          char = message[i]
          if char.isupper():
              result += chr((ord(char) + shift - 65) % 26 + 65)
          elif char.islower():
              result += chr((ord(char) + shift - 97) % 26 + 97)
          else:
              result += char
      return result

for line in sys.stdin:
  print(caesar_cipher(line, 3))

