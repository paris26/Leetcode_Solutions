def romanToInt(s):
   values = {
       'I': 1,
       'V': 5,
       'X': 10,
       'L': 50,
       'C': 100,
       'D': 500,
       'M': 1000
   }
   
   result = values[s[-1]]  # Start with last character
   prev_value = result
   
   # Go from second-to-last to first
   for i in range(len(s)-2, -1, -1):
       curr_value = values[s[i]]
       if curr_value < prev_value:
           result -= curr_value
       else:
           result += curr_value
       prev_value = curr_value
       
   return result