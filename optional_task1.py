# Here I am asking the user to input an integer using the input function within the int() function. Then storing that data value in a variable called user_num
user_num = int(input("Please enter a whole number here: "))

# Here I am using the modulus operator to return the remainder obtained after a divison is performed using the number 2.
# then using the if and else statments to check if there are any remaining values or not to calculate if the number enterd is even or not.
# I use the print functions with the f-string I can then print appropriate messages and the inputted number, according to what number the uer inputed
if user_num % 2 == 0:
    print(f"{user_num} This number is an even number.")
else:
    print(f"{user_num} This number is an odd number.")