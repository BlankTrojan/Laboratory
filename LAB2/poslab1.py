atmPin = input("Make a 4 digit pin:")
def atm_pin(pin):
    if pin == atmPin:
        return True
    else:
        return False

def login():
    print("NOTE:The police will be called if you had three successive failures ")
    tries = 0
    while tries < 3:
        pin = input('Enter Your 4 Digit Pin:')
        if atm_pin(pin):
            print("Accepted!")

            return True
        else:
            print("Incorrect")
            tries += 1
    print("To many incorrect tries. Calling the police. Disabling login button")
    return False

def menu():
    print("Welcome!")
    if login():
        print("Login Successful!")
menu()