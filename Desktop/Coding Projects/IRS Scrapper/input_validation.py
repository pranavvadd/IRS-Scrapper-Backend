# Helper functions for input validation
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_zip(prompt):
    while True:
        try:
            zip_code = input(prompt).strip()
            if zip_code.isdigit() and len(zip_code) <= 10:
                return zip_code
            print("Invalid ZIP code. Please enter a valid numeric ZIP code.")
        except Exception as e:
            print(f"Error during ZIP code input: {e}")

def get_boolean_input(prompt):
    while True:
        try:
            response = input(prompt).strip().lower()
            if response in ["yes", "no"]:
                return response == "yes"
            print("Invalid input. Please enter 'yes' or 'no'.")
        except Exception as e:
            print(f"Error during yes/no input: {e}")
