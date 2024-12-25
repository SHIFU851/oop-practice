class Gym:
    def __init__(self, subscriber_number, firstname, lastname, user_id):
        # Initializing subscriber attributes
        self.subscriber = subscriber_number
        self.firstname = firstname
        self.lastname = lastname
        self.user_id = user_id

    def __str__(self):
        # String representation of the Gym class
        return (f"Subscriber number: {self.subscriber}\n"
                f"FirstName: {self.firstname}\n"
                f"LastName: {self.lastname}\n"
                f"user id: {self.user_id}")


# User subscribers list
subscriber_numbers = [
    '128417347417417',
    '484848138831833',
    '484181418318131',
    '414881923194513',
    '919239319393934',
    '140414094904999'
]

# Names dictionary for validation
names = {
    'John': 'Doe',
    'Random': 'levi',
    'Noam': 'Cohen',
    'Jack': 'Williams',
    'Sally': 'Brown',
    'Moshe': 'Cohen'
}

# User IDs list
user_ids = [414141414414, 41414414431, 39491929192, 499219291292, 218281884, 912914819]

# Asking for the subscriber number
user_subscriber = input("Please enter your subscriber number: ")

if user_subscriber not in subscriber_numbers:
    print("You're not a subscriber, please get out!")
else:
    print("Welcome!")

    # Asking for the user's first name
    user_firstname = input("Please enter your firstname: ")

    # If the first name is in the dictionary, ask for the last name
    if user_firstname not in names:
        print("What? You're not a member!")
    else:
        # Asking for the user's last name
        user_lastname = input(f"Please enter your lastname, {user_firstname}: ")

        # Check if the last name matches
        if names[user_firstname] == user_lastname:
            print("Welcome!")
        else:
            print("Your lastname does not match. You're not a member!")

        # Asking for user ID
        user_id = int(input(f"{user_firstname}, please enter your id:"))

        if user_id not in user_ids:
            print("Access Denied!")
        else:
            print('Welcome')

            # Create Gym object if all checks are passed
            gym_member = Gym(user_subscriber, user_firstname, user_lastname, user_id)
            print(gym_member)

