
def add_digits():
    user_input = input("Please enter a two digit number: ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        add_digits()

add_digits()