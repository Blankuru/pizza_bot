# Pizza Bot Program
#Bugs - Phone input allows letters
#      - Name input allows numbers



import random
from random import randint

# List of names of the people who will greet the customers
names = ["Shawn", "Karlo", "Louis", "Jodek", "Carlos", "Mikara", "Tomas", "Giancarlo", "Joaquin", "Jacob"]


#Lists of pizza names
pizza_names = ['Margherita', 'Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']

#Lists of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#list to store ordered pizzas
order_list = []

#list to store pizza prices
order_cost = []

# Customer details
customer_details = {}


# validates input to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input (question) #asks the question
        if response != "":
            return response.title()
        else:
            print ("This cannot be blank")



# Welcome message with random names from the list
def welcome ():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None 
    '''
    #random integer which is num
    num = randint(0,9) 

    # name is the list of names within the list with the random integer on it which creates a random name from the list
    name = (names[num]) 

    #prints Welcome to Dream Pizza
    print ("*** Welcome to Dream Pizza ***")
    #prints "My name is" and a name from someone in the list
    print ("*** My name is", name, "***")
    #prints that he/she will be helping with the customer's order
    print ("***I will be here to help your order your delicous Dream Pizza***")


# Menu for pickup or delivery

def pdmenu():   
    print ("Do you want your order to be delivered or picked up?")

    print ("For pickup please enter 1") 
    print ("For delivery please enter 2")
    print ("")


    low = 1
    high = 2

    while True:
        try:
            delivery = int(input("Please enter a number: ")) # The space that the customer will have to input in
            if delivery >= 1 and delivery <= 2:
                if delivery == 1: #if the customer presses d for delivery
                    print ("Pickup")
                    pickup_info()
                    break
                elif delivery == 2: #if the customer presses p for pickup
                    print ("Delivery")
                    delivery_info()
                    break
            else:
                print ("The number must be 1 or 2")
                print ("")
        except ValueError:
            print ("That is not a valid number")
            print ("")
            print ("Please pick a number between 1 or 2")

    

# Pick up information - Name and Phone number

def pickup_info():
    question = ("Please enter your name: ") # Question
    customer_details['name'] = not_blank(question) # goes off with the function not_blank with the question
    #print (customer_details['name'])     


    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    #print (customer_details['phone'])  
    print(customer_details)


# Delivery Information - Name, Adress, Phone





# Basic instruction

def delivery_info():
#Customer name
    question = ("Please enter your name: ") # Question
    customer_details['name'] = not_blank(question) # goes off with the function not_blank with the question
    print (customer_details['name'])     

    #Customer Phone
    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])  

    #Customer house number
    question = ("Please enter your house number: ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])  

    #Customer street name
    question = ("Please enter your street name: ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])  

    #Customer suburb
    question = ("Please enter your suburb: ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb']) 



# Pizza Menu

def menu():
    number_pizzas = 12

    for count in range (number_pizzas):
        print ("{} {} ${:.2f}" .format(count+1, pizza_names[count], pizza_prices[count]))


# Choose total number of pizzas - max 5
# Pizza order - from menu - print each ordered with cost



def order_pizza():
    # ask for total number of pizzas for order
    num_pizzas = 0

    while True:
        try:
            num_pizzas = int(input("How many pizzas do you want to order? "))
            if num_pizzas >= 1 and num_pizzas <= 5:
                break
            else:
                print ("Your order must be between 1 and 5")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")

    #choose pizza from menu 
    for item in range(num_pizzas):
        while num_pizzas > 0:
            while True:
                try:
                    pizza_ordered = int(input("Please choose your pizza by entering the number from the menu: "))
                    if pizza_ordered >= 1 and pizza_ordered <=12:
                        break
                    else:
                        print ("Your order must be between 1 and 12")
                except ValueError:
                    print ("This is not a valid number")
                    print ("Please enter 1 or 12")
            pizza_ordered = pizza_ordered - 1
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            print("{} ${:.2f}" .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))
            num_pizzas = num_pizzas - 1












# Print order out - incl. of order is delivery or pickup and names and price of each pizza - total cost incl. any delivery charge 






# Ability to cancel or proceed the order






# Option for a new order or exit





# Main function
def main():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None 
    '''
    welcome()
    pdmenu()
    menu()
    order_pizza()

main()