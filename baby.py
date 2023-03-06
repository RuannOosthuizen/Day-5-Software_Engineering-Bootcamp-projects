print("To gain access to this amaizng party!")
#  Here I am using the input function to ask the user to input the year they wer born and saving that data in a variable called user_year
# I also use the int() function to make sure the input is an integer for easier calculations down the line.
user_year = int(input("Please enter the year you were born:\n"))

# Here I am now calculating the users age by using the mathemiatical operator minussymbol "-" to subtract the current year I am using "2023" with the year the user inputed using the variable user_year.
# Then saving the data value in a varaible called user_age.
user_age = 2023 - user_year

# Here I am then using the if statments to see if they are 18 or older or younger then 18 and then take action accordingly using the if and else statements and print functions.
if user_age >= 18: print("Congrats you are old enough.")

else:
    print("Sorry you are not old enough and must find the kids sections.")