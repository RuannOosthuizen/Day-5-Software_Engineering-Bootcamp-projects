# Here I am asking the user to input their full name (namely atleast two words or names), then saving that data in a variable called user_input.
user_input = input("Enter you name: ")

# Here I am then using the .split() data type to check if there are more then one word, then using the len() function to return that data into a integer to be easily read for the if statments to follow.
# I then save this data value in a variable called num_words.
num_words = len(user_input.split())

# Here I am then using if, elif and else statments with the variable num_words to check if user hase inputted their fullname then printing out the appropriate messages based on the users input.
if num_words == 0:
    print("You havent entered anything. Please enter your fullname.")
elif num_words == 1:
    print("You have entered less then 4 characters. Please make sure that you have entered your name and surname.")
elif num_words >= 4:
    print("You have entered more than 3 names. Please make sure that you have only entered your full name.")
else:
    print("Thank you for ebtering your name")