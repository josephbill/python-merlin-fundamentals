# # if - turue, elif - check for other condition if the if condition is not satisfied 
# # elif
# age =  0
# if age > 18:
#     print("This person is a young adult")
# elif age == 18:
#     print("This person's age is at 18")
# else:
#     print("The age comparison does not meet conditions")
    
# age = input("Enter Your Age ")
# attendee_name = input("Enter your name ")
# if int(age) > 18:
#     print(f"{attendee_name} can enter and receive a drink!!")
# elif int(age) >= 16 and int(age) <= 18:
#     print(f"{attendee_name} can enter but recieves a juice pack!")
# elif int(age) < 16:
#     print(f"{attendee_name} is too young cannot enter!!")
    

# # match statement : used to perform different actions based on different condiitions 
# day = 6 
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5 | 6 | 7:
#         print("Looking forward to the weekend!!")
#     case _:
#         print(f"{day} : This day does not exist!!")
        
# loops -programming statements that will allow you to repeat tasks 
# while loop , for loop 
# while loop - we can execute a code logic as long as the/a condition is true 
# the while loop stops when the condition is false 
# incrementors or decrementors  ++ : += 1, -- -= 1 
# break statement : stop the loop completely when condition met  
# / continue statement : skip the condition 
i = 1 
while i < 6:
    if i == 4:
        break
    print(i)
    i += 1
    
# continue 
i = 0
while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)
else:
    print(f"{i} : the condition is no longer true")
    
## For loop : for loop is used for iterating over sequences 
## list , tuple , set , dictionary , string 
x  = "banana"
for char in x:
    print(char)

list_fruits = ["apple","banana","Pear"]
for fruit in list_fruits:
    x = fruit.upper()
    print(x)
    
## range function range(start,stop,step)  step means skip
## FOR LOOP ALSO HAS BREAK , CONTINUE 
for x in range(2,10):
    if x >= 7:
        continue
    print(x)

## nested loops "" for every iteration of the outer loop it must complete the whole iteration of the inner loop
colors  = ["red","yellow","green"]
for x in colors:
    for y in list_fruits:
        print(f"{x} : {y}")

        