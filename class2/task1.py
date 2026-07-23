while True:
    age = int(input("Enter your age: "))

    if age < 13:
        print("Sorry, you're not allowed to pass")

    elif age >= 13 and age < 18:
        print("Call your legal guardian")

    elif age >= 18:
        print("Welcome")