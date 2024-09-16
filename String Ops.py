# Ask user for name and remove whitespace and capitalize in full
name= input("What's your name? ").strip().title()


#Split user's name intro first name and last name
first, last =name.split(" ")

#Say hello to user
print (f"hello, {first}" )

