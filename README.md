# Coffee Machine

This is a Python program for a coffee machine implemented using classes and objects. The program allows users to order various drinks from a menu, checks if there are sufficient resources to make the ordered drink, accepts payment, and deducts the required ingredients from the resources.

## MenuItem Class

This class represents a menu item in the coffee machine. It has the following attributes:

- `name` (str): The name of the drink.
  - Example: "latte"
- `cost` (float): The price of the drink.
  - Example: 1.5
- `ingredients` (dict): The ingredients and amounts required to make the drink.
  - Example: {"water": 100, "coffee": 16}

## Menu Class

This class manages the menu items available in the coffee machine. It provides the following methods:

- `get_items()`: Returns all the names of the available menu items as a concatenated string.
  - Example: "latte/espresso/cappuccino"
- `find_drink(order_name)`: Searches the menu for a particular drink by name. Returns a MenuItem object if it exists, otherwise returns None.
  - Parameter `order_name` (str): The name of the drink order.

## CoffeeMaker Class

This class represents the coffee maker. It has methods to manage the resources and make drinks. The class provides the following methods:

- `report()`: Prints a report of all resources.
  - Example:
    ```
    Water: 300ml
    Milk: 200ml
    Coffee: 100g
    ```
- `is_resource_sufficient(drink)`: Checks if there are sufficient ingredients to make the specified drink.
  - Parameter `drink` (MenuItem): The MenuItem object to make.
  - Returns True when the drink order can be made, False if ingredients are insufficient.
  - Example: True
- `make_coffee(order)`: Makes the specified drink by deducting the required ingredients from the resources.
  - Parameter `order` (MenuItem): The MenuItem object to make.

## MoneyMachine Class

This class handles the payment processing for the coffee machine. It keeps track of the profit and provides methods to manage payments. The class includes the following methods:

- `report()`: Prints the current profit.
  - Example: Money: $0
- `make_payment(cost)`: Accepts payment for the specified cost.
  - Parameter `cost` (float): The cost of the drink.
  - Returns True when payment is accepted, or False if insufficient.
  - Example: False

## Usage

To interact with the coffee machine program, follow these steps:

1. Run the program.
2. The program will greet you and ask for your preferred drink. It might prompt something like: "What is your preferred drink?"
3. Enter the name of the drink you want. For example, if you want a latte, type "latte" and press Enter.
4. The program will check if the drink is available on the menu.
5. If the drink is found on the menu, the program will check if there are sufficient resources to make the drink.
6. If there are enough resources, the program will display a message indicating that the resources are sufficient.
7. The program will then calculate the cost of the drink and ask for payment.
8. Enter the amount you want to pay for the drink. For example, if the drink costs $2.50, you can enter "2.50" and press Enter.
9. The program will check if the payment is sufficient.
10. If the payment is accepted, the program will display a message indicating that the payment is accepted and proceed to make the drink.
11. The program will deduct the required ingredients from the available resources.
12. Finally, the program will display a message indicating that your drink is ready.

Note: If at any point there are insufficient resources or the payment is not sufficient, the program will display the corresponding message and you may need to choose a different drink or provide a different payment amount.

Enjoy your coffee!

Please refer to the source code and class definitions for more details on the implementation.
