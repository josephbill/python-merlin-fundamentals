"""
- takes in a list of numbers [1,2,3,4]
- process the lists and return a dictionary of key and value pairs for the following info 
{
    "count" : 4,
    "min" : 1,
    "max" : 4,
    "sum" : 10,
    "average" : 2.xx, 
}
- take the input from the terminal
"""
# Analyze this function for a single responsibility perspective - Keep functions short , -> one clear purpose for the function 
def summarize_data(numbers):
    """ reference comments above  [10.0,20.0,30.0]"""
    # if numbers list is empty 
    if not numbers:
        return {"error" : "No data provided"}
    # reference units - total , count , smallest , largest - special string 'inf' '-inf'
    total = 0
    count = 0
    smallest = float('inf')
    largest = float('-inf')
    # loop list 
    for num in numbers:
        # get a total (additional assignment operator)
        total += num
        count += 1 
        # smallest number 
        if num < smallest:
            smallest = num
        # largest number 
        if num > largest:
            largest = num
    # average        
    average = total / count 
    # dict 
    op_dict = { "count" : count, "sum" : total, "min" : smallest, "max" : largest, "average" : round(average,2)}
    return op_dict
        
            
   

# in built variables __name__ and __main__
if __name__  == "__main__":
    # pick up the list from the user 
    user_input = input("Enter numbers separated by commas :: ")
    # split and convert to floats 
    # try(try executing) and except(graciously handles any error that arises without causing module crash) : Error handling :: code block
    try:
        # take users input and return as a list 
        # split inbuilt string method that truncates relative to symbol/char given  10,20,30,40
        # strip inbuilt string method that removes extra white spaces , illegal charactersets /A-z ::  "10,20,30" -> "10" "20" "30" -> 10.0 , 20.0 , 30.0
        numbers = [float(x.strip()) for x in user_input.split(",") if x.strip()]
        result = summarize_data(numbers)
        print(result)
    except ValueError:
        print("Please enter only numeric values")