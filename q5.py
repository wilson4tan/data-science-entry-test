import sys

def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))): #ensure Both num and divisor must be numeric
        return False 
    if divisor == 0: 
        return False #Return False if num is not divisible by divisor
    return num % divisor == 0 #Return True if num is divisible by divisor

if __name__ == "__main__":
    if len(sys.argv) != 3: #verify total number of arguments (including the script name) not more than 3 arguments
        print("Usage: ./q5.py <num> <divisor> | example: python q5.py 10 2")
        sys.exit(1)

    try:
        num = float(sys.argv[1]) #assign variable to num
        divisor = float(sys.argv[2]) #assign variable to divisor
        print(check_divisibility(num, divisor)) #print final result
    except ValueError:
        print("Please provide numeric input.")
        sys.exit(1)
        