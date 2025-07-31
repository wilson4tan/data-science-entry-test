import sys
import ast

def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    i = 0
    while i < len(lst): #loop through the list of value
        if lst[i] < 0: #verify if number is negative
            return lst[i] #verify if number is negative
        i += 1
    return "No negatives"

if __name__ == "__main__":
    if len(sys.argv) != 2: #verify total number of arguments (including the script name) not more than 2 arguments
        print("Usage: ./q6.py <list> | example: python q6.py [1,2,3,6,7,7,7,-99]")
        sys.exit(1)
    
    try:
        lst = ast.literal_eval(sys.argv[1])
        if not isinstance(lst, list): #ensure the input should be a list
            raise ValueError("Input must be a list.")
        print(find_first_negative(lst)) #print final result
    except Exception as e:
        print("Invalid input:", e)
        sys.exit(1)