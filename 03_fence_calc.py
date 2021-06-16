print()
print("**** Fence Price Calculator *****")
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

    #gets the width, height, and price per unit variables
    width = num_check('Width: ')
    height = num_check('Height: ')
    price_per_unit = num_check('Price per Unit: ')

    #calculates perimeter and price
    perim = width * 2 + height * 2
    price = perim * price_per_unit

    #prints perimeter and price
    print('The perimeter is {:.2f} units. This will cost you ${} in total.'.format(perim, price))
    print()

    keep_going = input("Press <enter> to keep going or any other key to quit: ")

print()
print("Thank you for using the fence price calculator!")