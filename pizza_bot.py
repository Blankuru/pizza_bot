# Pizza Bot Program

import random
from random import randint

#List of names of the people who will greet the customers
names = ["Shawn", "Karlo", "Louis", "Jodek", "Carlos", "Mikara", "Tomas", "Giancarlo", "Joaquin", "Jacob"]

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
                    break

                elif delivery == 2: #if the customer presses p for pickup
                    print ("Delivery")
                    break
            else:
                print ("The number must be 1 or 2")
                print ("")
        except ValueError:
            print ("That is not a valid number")
            print ("")
            print ("Please pick a number between 1 or 2")

    

# Pick up information - Name and Phone number


# Delivery Information - Name, Adress, Phone


# Choose total number of pizzas - max 5


# Pizza Menu


# Pizza order - from menu - print each ordered with cost


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

main()