# Functions go here
def yes_no(question):
    """Checks that users enter yes or no to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please choose an option from ('yes', 'no') \n")


# Main routine goes here
while True:
    want_instructions = yes_no("Do you want to read the instructions?")
    print(f"You chose {want_instructions}\n")
