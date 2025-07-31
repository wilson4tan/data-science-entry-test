import sys

def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))): #validate input is numeric
        return -1
    x, y = y, x # Swapping the x and y value
    print("Swapped values: x = %s, y = %s" % (x, y)) #print final result
    return

if __name__ == "__main__":
    if len(sys.argv) != 3: #verify total number of arguments (including the script name) not more than 3 arguments
        print("Usage: ./q1.py <x> <y> | example: python q1.py 8 9")
        sys.exit(1)
    try:
        x = float(sys.argv[1]) if '.' in sys.argv[1] else int(sys.argv[1]) #identify the input is float or integer
        y = float(sys.argv[2]) if '.' in sys.argv[2] else int(sys.argv[2]) #identify the input is float or integer
    except ValueError:
        print(-1)
        sys.exit(1)
    result = swap(x, y)
    if result == -1: #if input is not numeric,
        print(-1)