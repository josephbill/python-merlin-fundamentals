import srp_summarize # imports the whole file , . access the methods 
# from srp_summarize import display_result,parse_input,summarize_data  # importing by mentioning function to sues 
uncleaned_string  = "10,20,0,5,6,100"
# parse_input(uncleaned_string)

cleaned_string = srp_summarize.parse_input(uncleaned_string)
print(cleaned_string)
summarized_results = srp_summarize.summarize_data(cleaned_string)
print(summarized_results)
display_result = srp_summarize.display_result(summarized_results)
print(display_result)
# write out the functions 
