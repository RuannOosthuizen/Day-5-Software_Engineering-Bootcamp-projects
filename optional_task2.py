print("Please answer the questions below to determine your outfit for the day!")
# Here I am assaign the value 2 to the variables "temp20" for the temperatur question, "weekend" for the weekend question and "sunny" for the sunny question.
# This will become clearly as we go but I intend to use the len() function to determine how many letters the user types in "3" for "Yes" and "2" for "No".
# Then by using the mathematical symbol minus "-" I will then minus the the boolean variables by the users answers for each question, this gives me a value of either 1 or 0
# Then using the bool() funtion I can determine a True or False value wher 1 will return a True statement and 0 returning a False statment.
temp20 = 2
weekend = 2
sunny = 2

# Here I am asking the user the questions weather its 20degrees or higher, is it the weekend and if its sunny outside.
# Then by using the len() function I can then determine the values for each answer where yes will have the value of 3 and no the value of 2.
# Then storing those values in variables called quest1, quest2 and quest3 for each question respectively.
quest1 = len(input("Is the temperature outside higher then 20degrees? Yer or No:\n"))
quest2 = len(input("Is it the weekend? Yes or No:\n"))
quest3 = len(input("Is it sunny outside? Yes or No:\n"))

# Here I am determining the True or False values for each question by taking the (quest1, quest2 and quest3) variables and minusing the variables (temp20, weekend and sunny) respectively
# This in turn gives me a value of 1 or 0, then by using the bool() function that will give me a True or Values value. I store this value in a variables called value1, value2 and value3.
value1 = bool(quest1 - temp20)
value2 = bool(quest2 - weekend)
value3 = bool(quest3 - sunny)

# Here I am then determining the outcome of all three questions to respone to the user, using the if(and nested if), elif, else statments.
if value1 == True:
    if value2 == True:
        if value3 == True:
            print("Your outfit for today is wearing a!\n Short-Sleeved Shirt,\n Shorts\n and a Cap.")
        else:
            print("Your outfit for today is wearing a!\n Short-Sleeved Shirt,\n Shorts\n and a Raincoat.")
    else:
        if value3 == True:
            print("Your outfit for today is wearing a!\n Short-Sleeved Shirt,\n Jeans\n and a Cap.")
        else:
           print("Your outfit for today is wearing a!\n Short-Sleeved Shirt,\n Jeans\n and a Raincoat.")
        
else:
    if value2 == True:
        if value3 == True:
            print("Your outfit for today is wearing a!\n Long-Sleeved Shirt,\n Shorts\n and a Cap.")
        else:
            print("Your outfit for today is wearing a!\n Long-Sleeved Shirt,\n Shorts\n and a Raincoat.")
    else:
        if value3 == True:
            print("Your outfit for today is wearing a!\n Long-Sleeved Shirt,\n Jeans\n and a Cap.")
        else:
           print("Your outfit for today is wearing a!\n Long-Sleeved Shirt,\n Jeans\n and a Raincoat.")
