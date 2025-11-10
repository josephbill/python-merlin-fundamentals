# # # if - turue, elif - check for other condition if the if condition is not satisfied 
# # # elif
# # age =  0
# # if age > 18:
# #     print("This person is a young adult")
# # elif age == 18:
# #     print("This person's age is at 18")
# # else:
# #     print("The age comparison does not meet conditions")
    
# # age = input("Enter Your Age ")
# # attendee_name = input("Enter your name ")
# # if int(age) > 18:
# #     print(f"{attendee_name} can enter and receive a drink!!")
# # elif int(age) >= 16 and int(age) <= 18:
# #     print(f"{attendee_name} can enter but recieves a juice pack!")
# # elif int(age) < 16:
# #     print(f"{attendee_name} is too young cannot enter!!")
    

# # # match statement : used to perform different actions based on different condiitions 
# # day = 6 
# # match day:
# #     case 1:
# #         print("Monday")
# #     case 2:
# #         print("tuesday")
# #     case 3:
# #         print("wednesday")
# #     case 4:
# #         print("thursday")
# #     case 5 | 6 | 7:
# #         print("Looking forward to the weekend!!")
# #     case _:
# #         print(f"{day} : This day does not exist!!")
        
# # loops -programming statements that will allow you to repeat tasks 
# # while loop , for loop 
# # while loop - we can execute a code logic as long as the/a condition is true 
# # the while loop stops when the condition is false 
# # incrementors or decrementors  ++ : += 1, -- -= 1 
# # break statement : stop the loop completely when condition met  
# # / continue statement : skip the condition 
# i = 1 
# while i < 6:
#     if i == 4:
#         break
#     print(i)
#     i += 1
    
# # continue 
# i = 0
# while i < 6:
#     i += 1
#     if i == 4:
#         continue
#     print(i)
# else:
#     print(f"{i} : the condition is no longer true")
    
# ## For loop : for loop is used for iterating over sequences 
# ## list , tuple , set , dictionary , string 
# x  = "banana"
# for char in x:
#     print(char)

# list_fruits = ["apple","banana","Pear"]
# for fruit in list_fruits:
#     x = fruit.upper()
#     print(x)
# # else:
# #     # execution
    
# ## range function range(start,stop,step)  step means skip
# ## FOR LOOP ALSO HAS BREAK , CONTINUE 
# for x in range(2,10):
#     if x >= 7:
#         continue
#     print(x)

# ## nested loops "" for every iteration of the outer loop it must complete the whole iteration of the inner loop
# colors  = ["red","yellow","green"]
# for x in colors:
#     for y in list_fruits:
#         print(f"{x} : {y}")


# password = "" #empty string 
# while password != "letmein":
#     password = input("Give me your password::   ")
    
# print("Access Granted!!")

# # python methods for looping actions 
# # enumerate() : useful when we want both index and value
# names = ["Bill", "Jane", "Isak"]
# for index,name in enumerate(names):
#     print(index,name)
        
# # comprehensions : list comprehension : loop one liners 
# squares = []
# for x in range(5):
#     squares.append(x)
    
# print(squares)

# #list comprehension 
# squares = [i * i for i in range(5)]
# print(f"squares list comprehension {squares}")

# # traditional loop 
# t_squares=[]
# for i in range(5):
#     multiples = i * i
#     t_squares.append(multiples)
    
# print(f"traditional loop returning a list {t_squares}")


# Functions 
# reusable block of code designed to perform a specific task. 
# a function will receive input(arguments or parameters) -> it processes the input in accordance to logic in ocde block  -> gives back a desired output (single value)
# define a function in python : def nameofthefunction(): 
# process -> absent of process indicate pass (marks a code block as void)
# return -> specifies the return value of a function 
# None -> specifies no return was specified for the function  
# to be executed functions require to be called : call a function : functionName() 
        
def greet_function():
    greeting = f"Hello , this is the sum of the two numbers given "
    return greeting 
# parameters are placeholders for inputs to be processed in a function - max 6 - functions are reusable 
def add(a ,b):
    result = greet_function()
    sum = a  + b
    return f"{result} : {sum}" 

# a function with default parameters 
def multiplication(a=20,b=10):
    return a * b 

## Special types of python functionality in functions 
# one liner functions : lambda functions :: quick functionalities 
square = lambda x: x * x    
# multiple values return 
def math_ops(x,y):
    return x * y , x / y , x - y

multi, divis, sub = math_ops(10,10)

print(greet_function())
print(add(20,10))    # 20,10 function arguments -> fulfillment for the parameters 
print(multiplication())
print(square(4))
print(multi,divis,sub)

"""
Why Use functions
1. Reusability  :: write once , use everywhere 
2. Organization :: keeps code modular and readable 
3. Debugging :: Smaller chunks lead to ease in debugging 
4. Collaboration :  makes it easier to work with other code sets

Pro Tips 
1. Keep functions short , -> one clear purpose for the function 
2. Name them clearly -> use verb like words 
3. Avoid side effects unless intential 
4. Document with doc strings -> always document the intent of your function 
"""

def calculate_area(radius):
    """   calculate the area of a circle given the radius   """
    import math
    return math.pi * radius **  2


print(calculate_area(10))