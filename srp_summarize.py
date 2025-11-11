def parse_input(user_input):
    '''convert the comma separated string to be a list of float numbers '''
    try:
        numbers  = [float(x.strip()) for x in user_input.split(",") if x.strip()]
        return numbers
    except ValueError:
        # value Error - indicates wrong argument was passed for the funtion 
        # user_input = "joseph,7,brian,jane"
        print("Enter only numeric values")
        return [] # ensuring there is always a return incase of above error 
    
def summarize_data(numbers):
    '''compute the count , min , max , sum , average'''
    if not numbers:
        return {'error': "No numbers data provided"}
    # python math methods - count, sum , min , max , average 
    total = sum(numbers)     # sum : sums up the elements in a list of integers/list of float
    count = len(numbers) # len returns the size of a list i.e. number of elements in the list 
    smallest = min(numbers) # min returns the minimum value in a list 
    largest = max(numbers) # max returns the maximum value in a list 
    average = round(total / count, 2) # round returns a float value with a determined accuracy
    return {
        'count' : count, 
        'sum' : total, 
        'min' : smallest, 
        'max' : largest,
        'average' : average,
     }
    
def display_result(result):
    '''display the summarized dictionary in a readable way '''
    print("Summary of your data:")
    for key,value in result.items():
        print(f"The {key} is {value}")

# first function , main entry function 
def main():
    '''Main function : handle input and output printing'''
    user_input = input("Enter numbers separated by commas ")
    # pass user input to the modular function that hadles cleaning of the input 
    numbers = parse_input(user_input)
    print(numbers)
    result = summarize_data(numbers)
    print(result)  # dictionary 
    display_result(result)
    
if __name__ == '__main__':
    main()