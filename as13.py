punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
x=str(input("Enter the string :"))
no_punct = ""
for char in x:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)