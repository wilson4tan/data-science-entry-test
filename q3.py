import sys
import ast

def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if not isinstance(dct, dict):
        return dct

    if key in dct: #check if key exist in the dictionary
        print(f"Original value for '{key}': {dct[key]}")
    dct[key] = value #update new value into the dictionary
    return dct

if __name__ == "__main__":
    if len(sys.argv) != 4: #verify total number of arguments (including the script name) not more than 4 arguments
        print("Usage: ./q3.py <dictionary> <key> <value> | example: python q3.py \"{'apple':123}\" apple 26") 
        sys.exit(1)
    try:
        dct = ast.literal_eval(sys.argv[1]) #assign variable to 'dct'
        key = sys.argv[2] #assign variable to 'key'
        # Try to parse value as int or float, else use as string
        try:
            value = int(sys.argv[3]) #assign variable to 'key' if it's integer
        except ValueError:
            try:
                value = float(sys.argv[3]) #assign variable to 'key' if it's float
            except ValueError:
                value = sys.argv[3]
    except Exception as e:
        print("Invalid input:", e)
        sys.exit(1)

    result = update_dictionary(dct, key, value)
    print(result)#print final result
