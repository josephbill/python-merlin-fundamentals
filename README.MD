### PYTHON
- High-level 
- Interpreted - complilation is not manual - it simply executes the codebase line by line 
- general-purpose - web dev - backend - server scripting , data science ....
- extensive libs. 
- oop - object oriented programming 
- dynamically typed - python will try to assign a data type to a value , sometimes we need to be specific 

### Fundamentals 
- basics 
  a. syntax and structure
     - indentation - use 4 spaces to define code blocks
     - no usage of semi colon 
     - comments in python start with #  
  b. variables 
  c. data types 
  d. input and output 
  e. Type casting
  f. python operators 
  g. data type operations 

- control flows 
  a. conditional statements  - if ,elif, else 
  b. loops 

- functions 
- collections 
- modules and imports 
- oop basics 
- error handling 
- virtual environments and packages


### Python Operators 
Operators are used to perform operations on variables and values 

- Arithmetic Operators : these perform common math operations 
+, - , * , / , % (modulus : returns the reminder from a division operation)
- Assignment Operators : these operators assign values to variables 
= , += (  x += 3 : x = x + 3 ) , -= , *= , /= , %= 
- Comparison Operators : these operators are used to compare two values , the result is normally a boolean result True or False 
== , != , > , < , >= , <= , 
- Logical Operators : these operators are used to chain / combine conditional statements / comparison operators 
   a.  and : return true if both statements are true 
   b.   or : returns true if one of the statements is true 
   c.   not : reverses the result , returns false if the result is true 

- Identity Operators : used to compare objects , not if they are equal , but if they are the same object.
   a. is : returns true if both variables are the same object 
   b. is not : returns true if both variables are not the same objects 

- Membership Operators  :  used to test if a sequence is presented in an object 
   a. in : returns true if a sequence with the value specified is present 
   b. not in : returns true if a sequence with specified value is not present 

- Bitwise Operators  : used to compare values in a binary nature 
  a. and = &
True = 1 False = 0 
  b. or = |
  c. not = ~ , !

### Data Types Operations 
In built operations/methods that enable us to manipulate data 
Each Data type has its own variation for the built operations 

Numbers -> type casting , arithmetics operations


### FUNCTIONS and Single Responsibility Pattern : SRP 
Each function , class or module should have only one reason to change 
one function = one purpose 
### Why it matters 
1. Modularity - each function will do one thing well
2. Maintability - change one function without affecting the others 
3. Reusability - reuse the single functions elsewhere within our codebase 
4. Testability - each part can be unit-tested independetly 
### summarize.py 
Three core responsibilities 
1. Input handling - reading the input from the terminal 
2. Data processing - computing the stats (count, min, max , average etc..)
3. Output formatting- printing and error reporting 

### Modules :: this points to files/tools that have ready functions to enable executions of specifics task 

- Introduce to scripts using import statement 


### OOP : Object Oriented Programming 
- this is organizing our code around objects -> 
  Objects -> attributes : data 
             methods :: actions , independent action  , actions that affect the data 

    eCommerce System 
     - users -> role, full_name, id, password , email ,  -> login() , register(), resetPassword() , updateProfile()
     - products -> category, price , title , descriptions, -> add(), display() , updateProducts()
     - payments -> amount, gateway, useridentity -> makePayment() , generateReports()

## Building blocks of OOP 
- Class : blueprint 
- Object(single entity with attributes and methods) : instance of the class 

Dog class -> attributes - > name  -> breed -> age 
     objects      ->  different dogs created from the blueprint 


Python treats everything like an object 

## FOUR PILLARS OF OOP - a guide on desing thinking for outr oop approach 
1. Encapsulation - bundle data and behaviour(methods) in one place (class) 
- keep related things together
- keeps data safe and ensures no mix up data / behaviour relative to the domain 
2. Abstraction - hiding complex details and showing only the important stuff 
- simple methods that hide complex process 
3. Inheritance - allows once class to use atrributes and methods of another 
-reuse code , make relationships between our classes more clear 
4. Polymorphism - different objects can respond to the same method in different ways 


## DOMAIN EXAMPLE : RETAIL SYSTEM 
- Customers - data and methods sets that are required to represent this ddomain as code 
- Products - data and methods sets that are required to represent this ddomain as code 
- Orders  - data and methods sets that are required to represent this ddomain as code 
- Payments - data and methods sets that are required to represent this ddomain as code 

## Object relationships : The relationship to be established using objects in the system 
## one to one relationship : object to object 
## one to many relationship : object to multiple objects 
## many to many relationship : association class set up : many objects to many objects 
## 3 minutes break