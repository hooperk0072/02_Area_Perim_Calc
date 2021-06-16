print()
print("**** Area Perimeter Calculator *****")
print()
# functions
#checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid: 

        error = ('Please enter a number that is more than zero')

        try:

            # asks user to enter a number
            response = float(input(question))

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

keep_going = ""
while keep_going == "":

    #gets the width and height variables
    width = num_check('Width: ')
    height = num_check('Height: ')

    #calculates perimeter and area
    perim = width * 2 + height * 2
    area = height * width

    #prints outcome
    print('The perimeter is {:.2f} units and the area is {:.2f} square units.'.format(area, perim))
    print()

    keep_going = input("Press <enter> to keep going or any other key to quit: ")

print()
print("Thanks for using the area / perimeter calculator!")