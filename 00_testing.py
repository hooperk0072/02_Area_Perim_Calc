
def number_check(question):
    valid = False
    while not valid: 

        error = ('Please enter a number that is more than zero')

        try:

            # asks user to enter a number
            response = float(input('Enter a number: '))

            # checks if numer is more than zero
            if response > 0:
                return response

            # outputs error if numer is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()

number_check(width = int(input('Hello, user! This program will claculate the area and the perimeter of a rectangular shape. First, I need the width! Please enter a number larger than zero. ')))
