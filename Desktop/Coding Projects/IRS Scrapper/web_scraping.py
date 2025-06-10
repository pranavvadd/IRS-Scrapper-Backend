import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def scrape_irs_data(zip_code, distance, num_pages, include_options):
    driver = webdriver.Chrome()
    driver.get("https://irs.treasury.gov/rpo/rpo.jsf")

    # Select Country
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "form:country")))
    Select(driver.find_element(By.ID, "form:country")).select_by_visible_text("United States")

    # Select ZIP Code
    zip_input = driver.find_element(By.ID, "form:address")
    zip_input.clear()
    zip_input.send_keys(zip_code)
    time.sleep(5)

    # Select Distance
    distance_select = Select(driver.find_element(By.ID, "form:miles"))
    distance_select.select_by_value(str(distance))
    time.sleep(5)

    # Select checkboxes based on user input
    checkbox_options = {
        "form:attorney": include_options["Attorney Credentials"],
        "form:accountant": include_options["CPA Credentials"],
        "form:agent": include_options["Enrolled Agent Credentials"],
        "form:actuary": include_options["Enrolled Actuary Credentials"],
        "form:retirement": include_options["Retirement Plan Agent Credentials"],
        "form:filingSeasonProgram": include_options["Annual Filing Season Credentials"]
    }

    for box_id, include in checkbox_options.items():
        if include:
            checkbox = driver.find_element(By.ID, box_id)
            if not checkbox.is_selected():
                checkbox.click()

    # Click search button
    search_button = driver.find_element(By.ID, "form:search")
    search_button.click()

    # Scrape data
    data_list = []
    rows = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#form\\:data tbody tr"))
    )
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        data_list.append([col.text.strip() for col in cols])

    # Navigate through pages
    for _ in range(num_pages - 1):
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Next >>>']"))
        )
        if next_button.is_enabled():
            next_button.click()
        WebDriverWait(driver, 10).until(EC.staleness_of(rows[0]))
        rows = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#form\\:data tbody tr"))
        )
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            data_list.append([col.text.strip() for col in cols])

    # Convert the data list to a pandas DataFrame
    df = pd.DataFrame(data_list, columns=["Name", "Credential", "Location", "Distance"])

    # Write the DataFrame to a CSV file
    output_file = "output.csv"
    df.to_csv(output_file, index=False)

    # Close the browser
    driver.quit()

    return output_file