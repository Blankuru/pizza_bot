customer_details = {}


print ("Please enter your pickup information")

#Customer name
valid = False
while not valid:
    customer_details['name'] = input("Please enter your name: ")
    print ("")
    if customer_details['name'] != "":
        print (customer_details['name'])
        break
    else:
        print ("Sorry this cannot be blank") 
        
#Customer phone
valid = False
while not valid:
    customer_details['phone'] = input("Please enter your phone number: ")
    if customer_details['phone'] != "":
        print (customer_details['phone'])
        break
    else:
        print ("Sorry this cannot be blank")

