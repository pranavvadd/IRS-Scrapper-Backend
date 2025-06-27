from input_validation import get_valid_int, get_valid_zip, get_boolean_input
from web_scraping import scrape_irs_data
from utils import open_file

# Prompt user for input
try:
    user_num_pages = get_valid_int("Enter the number of pages to navigate: ")
    user_zip_code = get_valid_zip("Enter the ZIP code: ")
    
    user_distance = get_valid_int("Enter the distance in miles (5, 10, 25, 50, 100, 250): ")
    while user_distance not in [5, 10, 25, 50, 100, 250]:
        print("Invalid distance. Please enter one of the following: 5, 10, 25, 50, 100, or 250.")
        user_distance = get_valid_int("Enter the distance in miles (5, 10, 25, 50, 100, 250): ")

    include_options = {
        "Attorney Credentials": get_boolean_input("Do you want to include Attorney Credentials? (yes/no): "),
        "CPA Credentials": get_boolean_input("Do you want to include CPA Credentials? (yes/no): "),
        "Enrolled Agent Credentials": get_boolean_input("Do you want to include Enrolled Agent Credentials? (yes/no): "),
        "Enrolled Actuary Credentials": get_boolean_input("Do you want to include Enrolled Actuary Credentials? (yes/no): "),
        "Retirement Plan Agent Credentials": get_boolean_input("Do you want to include Retirement Plan Agent Credentials? (yes/no): "),
        "Annual Filing Season Credentials": get_boolean_input("Do you want to include Annual Filing Season Credentials? (yes/no): "),
    }
except Exception as e:
    print(f"Error during input: {e}")
    exit()

# Perform web scraping
output_file = scrape_irs_data(user_zip_code, user_distance, user_num_pages, include_options)

# Open the output file
open_file(output_file)