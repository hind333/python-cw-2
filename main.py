# write your code here
my_name = input("Whats your name?")
my_age = input("How old are you?")
print(f"My name is {my_name} and I am {my_age} years old")
first_number = 5
second_number = 15
user_input = input("operation")
if  user_input ==  "+":
 print(first_number+second_number) 
elif  user_input == "-":
 print(first_number-second_number)
elif  user_input == "/":
 print(first_number/second_number)
elif  user_input == "*":
 print(first_number*second_number)
else: print("operation is not valid")

number = input("Enter a number from 1 to 12")
noun = input("Enter a noun (plural)")
name = input("Enter a name")
sentence = input("Enter any sentence")
verb = input("Enter a verb")
print(f"It was {number} o'clock when I heard a knock at the door.I opened the door and there was a box full of {noun} with a note saying From Ms.{name}.Just as I closed the door I heard a scream {sentence}.I froze in place and all I could do was {verb}.")