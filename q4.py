import sys

def string_reverse(s):
    if not isinstance(s, str): #ensure the input is string type
        return s
    return s[::-1] #reverse the string input

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./q4.py <string> | example: python q4.py apple")
        sys.exit(1)

    input_str = sys.argv[1]
    print(string_reverse(input_str))