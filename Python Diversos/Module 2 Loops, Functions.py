#for i in range(10):
#print(i)
#      
#for x in range(2, 10):
#      print(i)
#
#for i in range(0, 10, 3):
#      print(i)
#
#for i in "hello!":
#  print(i)
#
#string = "hello world!"
#for i in range(0, len(string), 2):
#  print(str(i) + "th letter is "+ string[i])

#count = 0
#while (count < 10):
#  print(count)
 #count +=1

#while True:
#  user = input("Digite algo a ser repetido: ")
#  if user=="end":
#    print("Finalizado!!!")
#    break
#    print(user)
#
#end  =  False 
#while  end  ==  False : 
#  user  =  input ( "Digite algo a ser repetido:" ) 
#  if  user == "end" : 
#    print ( "programa Finalizado" ) 
#    end  =  True 
#  else : 
#    print ( user )

#count = 1

# WHILE loop implementation
#while count + 1 <= 20:
#  if count % 5 == 0:
#    print("SKIP")
#    count += 1
#    continue
#  print(count)
#  count += 1

#for i in range (1, 20):
#  if i % 5 == 0:
#    print("SKIP")
#    continue
#    print(i)
#    
#
#def isRightTriangle(a, b, c):
#    
#  # Reassign variable values to ensure c is the longest length
#  if (max(a,b,c) != c):
#
#    # tmp stores the previous c values, that's not the longest length
#    tmp = c
#    c = max(a,b,c)
#
#    if a == c:
#      a = tmp
#    elif b == c:
#      b = tmp   
#
# # Apply the formula  
#  if a**2 + b**2 == c**2:
#    print("Right Triangle")
#
#    # If the program sees a return statement, this is the END of the program/function
#    return True
#  
#  # These two lines will ONLY run when the IF condition is false
#  print("NOT a right triangle")
#  return False
#
#
## Prompt the user to enter 3 lengths
#def main():
#  a = input("Enter the length for the first edge of the traingle:")
#  b = input("Enter the length for the second edge of the traingle:")
#  c = input("Enter the length for the last edge of the traingle:")
#
#  # User inputs are stored as a string, so we cast them to be int
#  return isRightTriangle(int(a), int(b), int(c))
#
#if __name__ == "__main__":
#    main() 
# 
# import the string package
# We will go over packages/libraries more in Module 5
import string


# This implementation of the function RETURN a boolean value, True/False
def isPalindrome(str):

  # Since we could not control what user enters for the sentence, let's sanitize the sentence first.
  # We will remove all punctuations and white spaces from the sentence, make all letters lowercase
  exclude = set(string.punctuation)
  str = ''.join(ch for ch in str if ch not in exclude)
  str = str.replace(" ", "").lower()

  # Compare the original string with the string in reversed order
    # Notation of str[::-1]: first 2 numbers define the start and end of string, last number of -1 means in reversed order

  # Check if the string is the same in reversed order as the original order
#  if str == str[::-1]:
#    return True
#  else:
#    return False
#
## Prompt the user to enter the sentence
#def main():
#  userSentence = input("Enter a sentence to be tested as a palindrome:")
#
#  if (isPalindrome(userSentence)):
#    print(userSentence + " is a palindrome!")
#  else:
#    print(userSentence + " is NOT a palindrome!")
#
#if __name__ == "__main__":
#    main()       
#

# Consider this implementation of the function that RETURN a string.
# Take note of the difference between the main() and isPalindrom() following this change. 
'''
import string

def isPalindrome(str):
  exclude = set(string.punctuation)
  str = ''.join(ch for ch in str if ch not in exclude)
  str = str.replace(" ", "").lower()
  if str == str[::-1]:
    return str + " is a palindrome!"
  else:
    return str + " is NOT a palindrome!"

def main():
  userSentence = input("Enter a sentence to be tested as a palindrome:")
  print(isPalindrome(userSentence))

if __name__ == "__main__":
    main()


Above we worked through an example that test whether a sentence is a palindrome. 
Now it's your turn.

Exercise: write a function to test if a word from the user is a palindrome. 

Function declarations are provided for you. 



Above we worked through an example that test whether a sentence is a palindrome. 
Now it's your turn.

Exercise: write a function to test if a word from the user is a palindrome. 

Function declarations are provided for you. 
'''

# One implementation of solution for above exercise. 

def isPalindrome(str):
  str = str.lower()
  if (str == str[::-1]):
    return True
  else:
    return False


# Prompt the user to enter the sentence
def main():
  userInput = input("Enter a WORD to be tested as a palindrome:")

  if (isPalindrome(userInput)):
    print(userInput + " is a palindrome!")
  else:
    print(userInput + " is NOT a palindrome!")
    
if __name__ == "__main__":
    main()