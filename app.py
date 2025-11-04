# # variables - named storage references for information 
# # variables will receive data types from the values they store 
# # data type - format data  : Joseph - text , 0 - number , 0.23 - decimal 
# # nameofvariable = value 
# # when naming a variable observe the following 
# # variable name should have meaning in reference to the value being stored 
# # variable name should not contain empty spaces - use an underscore to represent a space 
# # variables are case sensitive 
# name = "Joseph" # string : value enclose in quotes - string 
# number_one = 27 # integer: wholesome number - without decimal notations 
# number_two = 22.09 # float : decimal notation 
# boolean_variable = True # boolean : represents True or False 
# list_variable = ["Joseph", 12, 7.45, True, True] # list collection : grouping of elements
# set_variable = {2,3,4,4} # set collection : collection of unique elements {2,3,4}
# tuple_variable = ("Joseph",12) # tuple collection 
# dictionary_variable = {
#     "name" : "Joseph Mbugua", 
#     "class" : "Merlin Class",
#     "student_id" : 89389
# }  # dictionary is a collection of related information
# none_variable = None  # none is the reference for the data type and not empty 
# # how to output - print(specify_what_to_print) method : output will be reflected in the terminal 
# print(name)
# print(set_variable)
# # how to run the file : python filename.py - terminal
# # camelcase - numberOne # snakecase  number_one 
# # for input taking in python via the terminal - input()
# user_name = input("Enter username ")
# user_email = input("Enter User Email ")
# # formatted string print : we can attach statements dynamically with variables 
# print(f"The user's name is {user_name} and the email is {user_email}")
# # variable re-assignment : changing the value that a variable ref. is pointing to.
# user_name = "Not taking username's at the moment"
# print(user_name)

# ## Control Flows 
# ## if , elif run if condition is true , if not it then becomes false and runs the else
# ## else it runs nothing if the else block is not provided 
# # if condition:
# #     execution
# # elif condition:
# #     execution
# # else:
# #     execution
# # code blocks - a group of code that executes a particulr output 
# age =  0
# if age > 18:
#     print("This person is a young adult")
# elif age == 18:
#     print("This person's age is at 18")
# else:
#     print("The age comparison does not meet conditions")

# a = "10"
# b = "20"
# c = int(a) + int(b) 
# print(c)

# # TYPE CASTING - changing a variable value from one data type to another 
# # wrap the value inside the data type method
# # event entry program - is above 18 -> gain admission and receive a complimentary drink 
# # - if user is btw range 16 - 18 -> gain admission and receive a juice 
# # - if user is below 16 -> gain admissions 
age = input("Enter Your Age ")
attendee_name = input("Enter your name ")
if int(age) > 18:
    print(f"{attendee_name} can enter and receive a drink!!")
elif int(age) >= 16 and int(age) <= 18:
    print(f"{attendee_name} can enter but recieves a juice pack!")
elif int(age) < 16:
    print(f"{attendee_name} is too young cannot enter!!")

