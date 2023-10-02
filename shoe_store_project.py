#========The beginning of the class==========
class Shoe:

    # initialise attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = int(quantity)

    # returns the cost of the shoes
    def get_cost(self):
        return self.cost

    # returns the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # sets new quantity for shoe object
    def set_quantity(self, new_quantity):
        self.quantity += int(new_quantity)

    # returns the code of the shoe
    def get_code(self):
        return self.code

    # returns a string representation of class
    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n".upper()

#=============Shoe list===========
# The list will be used to store a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============
# function to read data from file
def read_shoes_data():
    with open('inventory.txt', 'r') as f:
        try:
            # skip first line of inventory.txt
            next(f)
            # for each line in inventory.txt data is stripped and shoe object added to shoe_list
            for lines in f:
                split_lines = lines.strip('\n').split(',')
                shoe1 = Shoe(split_lines[0], split_lines[1], split_lines[2], split_lines[3], split_lines[4])
                shoe_list.append(shoe1)

        # error handling
        except FileNotFoundError as error:
            print('\n Sorry, this file does not exist!\n')

        # close file
        f.close()

# function to capture user data and create shoe object
def capture_shoes():
    print('''
==================================
 YOU HAVE CHOSEN TO CREATE A SHOE
==================================
''')

    user_country = input('Please enter the country of your shoe: ')
    user_code = input('Please enter the code of your shoe: ')
    user_name = input('Please enter the name of your shoe: ')
    user_cost = input('Please enter the cost of your shoe: ')
    user_quantity = input('Please enter the quantity of your shoe: ')

    # create new shoe object with user data and append to shoe_list
    new_shoe = Shoe(user_country, user_code, user_name, user_cost, user_quantity)
    shoe_list.append(new_shoe)

    print('''
==================================
    A SHOE HAS BEEN CREATED
==================================''')

# function iterates over shoe_list and prints details of shoes
def view_all():
    for pos, i in enumerate(shoe_list):
        print(f'{pos + 1}. {i}')

# function to find the shoe object with the lowest quantity
def re_stock():
    try:
        # sorts list starting with the lowest quantity
        shoe_list.sort(key=lambda x: x.quantity)

        # save first of list as lowest stock variable
        restock_shoe = shoe_list[0]


        print('--------------------------------------------------')
        print(f'The shoe with the lowest stock is: {restock_shoe}')
        print('--------------------------------------------------')

        new_user_quantity = int(input('How many of this shoe would you like to buy?: '))

        # set object quantity as user input
        restock_shoe.set_quantity(new_user_quantity)

        # open inventory.txt in write mode and write updated shoe list
        inventory_write = open("inventory.txt", "w")
        inventory_write.write('Country,Code,Product,Cost,Quantity\n')
        for shoe in shoe_list:
            inventory_write.write(str(shoe))

        # close file
        inventory_write.close()
        print('------------------------------')
        print("Your product has been updated!")

    # error handling
    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

# function to search for specific shoe via code
def search_shoe():
    search_shoe = input('''
==================================
           SHOE SEARCH
==================================
Please enter shoe code: ''')

    # interate through shoe list and check user input against code
    for line in shoe_list:
        if line.get_code() == search_shoe:
            print(f'\n {line}')

    print("\nPlease select another option from the menu below\n")

# fucntion to calculate total value for each item
def value_per_item():
    for line in shoe_list:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f'{line.get_code()} VALUE: £{value}\n')

# function to determine the product with the highest quantity
def highest_qty():
    # sort shoe list with highest quality value at top
    shoe_list.sort(key=lambda x: x.quantity, reverse=True)
    highest_quantity_shoe = shoe_list[0]

    print("\n-------------Highest stock item:--------------\n")
    print(highest_quantity_shoe)

    print("\nThis item has now been marked on sale\n")
    print("\nPlease select an option from the menu below")

#==========Main Menu=============
# call function to populate shoe_list
read_shoes_data()

# while loop to display menu options
while True:

    try:
        menu = int(input('''
==================================
    Welcome to SHOE'S 'R" US! 
==================================
Please select from the menu below:
1. Create Shoe
2. View All Shoes
3. Restock Shoe
4. Search for a Shoe
5. View Item Values
6. View Sale Items
==================================
ENTER: '''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            view_all()
            re_stock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_qty()

        # error handling
        elif menu > 6:
            print("\nYou have selected an invalid option. Please try again by choosing from the menu below.\n")

    # error handling
    except ValueError:
        print("\nYou have selected an invalid option. Please try again by entering a number.\n")

# ====================================================== END ===================