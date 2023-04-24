#The purpose of this program is to encrypt a given message using the Caesar Cipher technique. This is an assignment for Linux Lab.

import sys
#import sys

def caesar_cipher(message, shift):    #takes in two parameters, message and shift.
      result = ""                      #utilizes an empty string which stores encrpyted message
      for i in range(len(message)):     #iterates over each letter in the 'message'
          char = message[i]
          if char.isupper():             #evaluates if letters are uppercase and shitfts accordingly
              result += chr((ord(char) + shift - 65) % 26 + 65)
          elif char.islower():         #evaluates if letters are lowercase and shifts accordingly  
              result += chr((ord(char) + shift - 97) % 26 + 97)
          else:
              result += char
      return result

shift = int(input("Enter shift value:")   #person can choose the shift value to encryt the message. 
                                          #After entering what shift you want, the program will wait for message input by the user. 
            
for line in sys.stdin:    #reads the lines of the given input 
  print(caesar_cipher(line, shift))     #prints the results of now encrypted string 

