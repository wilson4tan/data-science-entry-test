import sys

class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
 
    def __init__(self, make, model, year): #Initialize attributes: make, model, year
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print('Make: %s, Model: %s, Year: %s' % (self.make, self.model, self.year))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./q7.py <make> <model> <year> | example: python q7.py toyota ABC123 2025")
        sys.exit(1)

    make = sys.argv[1]
    model = sys.argv[2]
    try:
        year = int(sys.argv[3]) #ensure the year is integer
    except ValueError:
        print("Year must be an integer.") #return error if year not integer
        sys.exit(1)

    car = Car(make, model, year)
    car.describe_car() #call the function to print the result