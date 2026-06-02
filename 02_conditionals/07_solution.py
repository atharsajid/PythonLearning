order_size = input("Which coffee would like to have Small, Medium or Large? \n")
option = input("Would you like to have Extra Shot of express? Yes or No \n")

option = option.lower().strip()

if not order_size or not option: #Check empty
    print("Please enter correct ans")
    exit()


order = "Here is your {} Coffee".format(order_size)

if  option == "yes" or option == "y":
    order += ", wit Extra Shots of espresso"

print(order)