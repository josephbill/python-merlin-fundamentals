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

# ## Control Flows  ctrl + shift + I 
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
# age = input("Enter Your Age ")
# attendee_name = input("Enter your name ")
# if int(age) > 18:
#     print(f"{attendee_name} can enter and receive a drink!!")
# elif int(age) >= 16 and int(age) <= 18:
#     print(f"{attendee_name} can enter but recieves a juice pack!")
# elif int(age) < 16:
#     print(f"{attendee_name} is too young cannot enter!!")
    
    
a =  10 
b = a + 20

f_name = "Joseph"
l_name = "mbugua"
print(f_name + "" + l_name)

c = 7
d = 3
e = c * d
print(e)
d *= 10 # d = d * 10
print(d)
d %= 3 # d = d % 3 
print(d)

x = 10 
y = 6
print(x == y) # false
print(x != y) # true
print(x <= y) # false
print(10 < x and x > 1) # false 
print(10 < x or x > 1) # true 
print(not(10 < x and x > 1))  # result is false - true 
print(not(10 < x or x > 1)) # result is true - false 

x = ["jeep","suv"]
y = ["jeep", "suv"]
z = x 

print(x is z) # true 
print(x is y) # false 

print("jeep" in x )
print("jeep" not in x)
name = "Joseph Mbugua"
print("M" in name) # true

x = 6 # 0110 
y = 3 # 0011  - 0111 - 7 
print(6 | 3)

# strings (str)
# use for text manipulation 
example_string= "Python" # size/len = 6  # index position of each letter starts from 0
# common operations 
print(len(example_string)) # 6 
# convert to uppercase
print(example_string.upper())
print(example_string.lower()) # lower case 
# substring : slice a string and return the portion selected  : hon
print(example_string[3:6])
print(example_string[0:3]) # pyt
# join : create a string by joining separate letters in a list datatype 
list_letters = ["a","b","c"]
# "abc" 
# .join 
joined_statement  = "".join(list_letters)
print(joined_statement)

# isinstance()
x = 100
print(isinstance(x, int)) # true , or false 
# collections / sequences : grouping of data - immutable , mutable 
# lists , tuples , set and dictionary 
# lists - List items are ordered , changeable , and allow duplicate values 
# ordering in lists is referenced as index positioning - start 0 
# size : number of items inside the list - len() 3 
# index position in collections = size - 1 
# access of items in the list is via index positioning 
# changeable : ability to be able add(append) remove , update 
# list items can be of any data type
list_fruits = ["apple", "banana", "orange", 7, True, "apple", "orange"]
print(list_fruits)
# operations 
print(len(list_fruits))  #len 
# access items - via the index position
print(list_fruits[4]) # true
print(list_fruits[0]) # apple 
print(list_fruits[-1]) # access last item in a list 
print(list_fruits[2:5]) # range indexing  : items 3 - 5
# append allows adding of elements in the list 
list_fruits.append("Pear")
print(list_fruits)
# remove items from the list 
list_fruits.pop(0)
print(list_fruits)
# update 
list_fruits[0] = "Cherry"
print(list_fruits)

# tuples - immutables sequences , they cannot be changed , items are of the same data type / mixed data types
coordinates = (5,10,15,5,15)
one_item_tuple = (1,)
# operations 
print(len(coordinates))
# ordered : index positioning 
print(coordinates[0]) # 5 
print(coordinates[-1]) # 15 
print(coordinates[0:4])
# update values in a tuple (type casting) ( remove , update ) tuple -> list -> tuple
changed_coordinates = list(coordinates)
print(changed_coordinates) 
changed_coordinates.pop(1)  # remove ("element")
changed_coordinates[1] = 9.05
coordinates = tuple(changed_coordinates)
print(coordinates)
# delete a tuple completely 
del one_item_tuple

# sets - unordered , unchangeable, unindexed , on print it only prints unique items i.e. remove duplicates 
# sets see false as 0
set_fruits = {"apple","banana","pear","apple",False,0}
print(set_fruits)
print(len(set_fruits)) # unique items
# access items in a set : reference for...in loop
# loops : allows you to repeat tasks 
for fruit in set_fruits:
    print(fruit)
    
# sets cannot change but will allow additions : add() 
set_fruits.add("Orange")
print(set_fruits)
# sets will also allow addition of any collection : update()
set_fruits.update(list_fruits)
print(set_fruits)    
# remove items 
set_fruits.remove(7)
print(set_fruits)
set_fruits.update(list_fruits)
print(set_fruits)
set_fruits.discard('banana')
print(set_fruits)

# dictionary  - storage of data values in key and value pairs 
# ordered , changeables , won't allow duplicates keys
my_vehicle = {
    "brand" : "Toyota","model" : "Corolla","year"  : 2007,"engineNo" : "EF6790","ntsaReg" : False
}
print(my_vehicle)
# access items from a dictionary using the key 
print(my_vehicle["brand"])
print(my_vehicle.get("engineNo"))
print(len(my_vehicle))
print(my_vehicle.keys()) # list all the keys for the dictionary tagged 
print(my_vehicle.values()) # list all the values in the dictionary 
print(my_vehicle.items()) # list all key:value pairs for the dictionary 
print("brand" in my_vehicle) # true  : check if a key exists in a dictionary 
# change value that a key points to 
my_vehicle["model"] = "X78"
my_vehicle["year"] = 2008
print(my_vehicle)
# update a dict. = adding a new key:value pair 
my_vehicle["reg_name"] = "Joseph Mbugua"
my_vehicle.update({"chassis_no" : 89483948})
print(my_vehicle)
# remove items from the dict .
print(my_vehicle.pop("reg_name"))
print(my_vehicle)
del my_vehicle["ntsaReg"]
print(my_vehicle)

### nested collections 
x = [ ["apple","pear"] , "Joseph" , "Jane" , (1,90.09) , False, {"fullname" : "J Mbugua","Staff_id" : 49839} ]
# access the staff_id and print it 
print(x[5]["Staff_id"]) # 49839

myFamily = {
    "father" : {
        "name" : "John",
        "year" : 1985
    }, 
    "mother" : {
        "name" : "Jane",
        "year" : 1990
    }
}
mother_name = myFamily["mother"]["name"]
print(mother_name)
print(f"The mother's name is {mother_name}")