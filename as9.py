String=str(input("Enter the string:"))
String= String.casefold()
rev_str = reversed(String)
if list(String) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
