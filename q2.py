import sys
import ast

def find_and_replace(lst, find_val, replace_val):
    """
    Replace all occurrences of find_val in lst with replace_val.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    return [replace_val if item == find_val else item for item in lst] #loop through the list and replace all occurrence of find_val with replace_val

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./q2.py <list> <find_val> <replace_val> | example: python q2.py [1,2,3,4,5] 4 99")
        sys.exit(1)

    try:
        lst = ast.literal_eval(sys.argv[1]) #treat the input as it is
        if not isinstance(lst, list):
            raise ValueError("First argument must be a list.")
        # Parse find_val and replace_val as int, float, or string
        def parse_value(val):
            for cast in (int, float):
                try:
                    return cast(val)
                except ValueError:
                    continue
            return val  # fallback to string

        find_val = parse_value(sys.argv[2])
        replace_val = parse_value(sys.argv[3])

        result = find_and_replace(lst, find_val, replace_val)
        print(result)

    except Exception as e:
        print("Invalid input:", e)
        sys.exit(1)
