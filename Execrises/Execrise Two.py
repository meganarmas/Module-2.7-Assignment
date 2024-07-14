def validate_order():
    while True:
        try:
            quantity = int(input("Enter the quanity of books you want to enter: "))
            if quantity > 0:
                print(f"Thank you! You have ordered {quantity} books")
                break
            else:
                print("Invalid answer")
        except ValueError:
             print("Invalid input. Please enter a number")


validate_order()