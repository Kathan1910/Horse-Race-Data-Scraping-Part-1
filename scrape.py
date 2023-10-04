# import requests
# from bs4 import BeautifulStoneSoup

# Action ?

# name = email

# password = password

# make payload 

# payload = {"email":"kp5640907@gmail.com","password":"Kathan#1910"}

# login_url = 'https://photofinish.live/'

# request_url = 'https://photofinish.live/marketplace'

# with requests.session() as s:
#     r=s.post(login_url,data=payload)
#     my_data = s.get(request_url)
#     print(my_data.text)


################### Handle Popup With Cross Button    #######################

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time  # Import the time module

# # Initialize the web driver (Chrome WebDriver should be in your PATH)
# driver = webdriver.Chrome()

# # Website URL
# url = 'https://photofinish.live/marketplace'

# try:
#     # Navigate to the URL
#     driver.get(url)

#     # Find the login button and click it
#     login_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//button[@data-cy="top-widget-login-button"]'))
#     )
#     login_button.click()

#     # Find the email and password input fields and enter the credentials
#     email = driver.find_element(By.NAME, 'email')
#     password = driver.find_element(By.NAME, 'password')

#     email.send_keys("kp5640907@gmail.com")
#     password.send_keys("Kathan#1910")

#     # Submit the login form
#     password.send_keys(Keys.RETURN)

#     # Wait for the login to complete (you may need to adjust the wait time)
#     WebDriverWait(driver, 10).until(EC.url_to_be(url))

#     # Handle the popup and click the top right corner cross button
#     try:
#         popup_close_cross_button = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//svg[@data-cy="modal-close-button"]'))
#         )
#         popup_close_cross_button.click()
#     except:
#         # If the cross button doesn't appear, or there's any issue, continue without handling it
#         pass

#     # Scroll down until no more new elements are loaded
#     while True:
#         current_height = driver.execute_script("return document.body.scrollHeight;")
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
#         # Add a delay to allow time for new elements to load (adjust the sleep duration as needed)
#         time.sleep(8)  # You can adjust the sleep duration
        
#         # Check if there are more elements loaded or if we've reached the end
#         new_height = driver.execute_script("return document.body.scrollHeight;")
#         if new_height == current_height:
#             break

#     # Find all the horse name elements
#     horse_name_elements = driver.find_elements(By.XPATH, '//p[@class="text-white w-full font-semibold truncate whitespace-nowrap"]')

#     # Extract and print horse names
#     total_horses = len(horse_name_elements)
#     print(f"Total Horse Names: {total_horses}")

#     for element in horse_name_elements:
#         print(element.text)

# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# finally:
#     # Close the WebDriver session
#     driver.quit()


################### Handle Popup With Continue Button #########################


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time  # Import the time module

# # Initialize the web driver (Chrome WebDriver should be in your PATH)
# driver = webdriver.Chrome()

# # Website URL
# url = 'https://photofinish.live/marketplace'

# try:
#     # Navigate to the URL
#     driver.get(url)

#     # Find the login button and click it
#     login_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//button[@data-cy="top-widget-login-button"]'))
#     )
#     login_button.click()

#     # Find the email and password input fields and enter the credentials
#     email = driver.find_element(By.NAME, 'email')
#     password = driver.find_element(By.NAME, 'password')

#     email.send_keys("kp5640907@gmail.com")
#     password.send_keys("Kathan#1910")

#     # Submit the login form
#     password.send_keys(Keys.RETURN)

#     # Wait for the login to complete (you may need to adjust the wait time)
#     WebDriverWait(driver, 10).until(EC.url_to_be(url))

#     # Handle the popup and click the "Continue" button
#     try:
#         popup_continue_button = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//button[text()="Continue"]'))
#         )
#         popup_continue_button.click()
#     except:
#         # If the "Continue" button doesn't appear, or there's any issue, continue without handling it
#         pass

#     # Scroll down until no more new elements are loaded
#     while True:
#         current_height = driver.execute_script("return document.body.scrollHeight;")
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
#         # Add a delay to allow time for new elements to load (adjust the sleep duration as needed)
#         time.sleep(8)  # You can adjust the sleep duration
        
#         # Check if there are more elements loaded or if we've reached the end
#         new_height = driver.execute_script("return document.body.scrollHeight;")
#         if new_height == current_height:
#             break

#     # Find all the horse name elements
#     horse_name_elements = driver.find_elements(By.XPATH, '//p[@class="text-white w-full font-semibold truncate whitespace-nowrap"]')

#     # Extract and print horse names
#     total_horses = len(horse_name_elements)
#     print(f"Total Horse Names: {total_horses}")

#     for element in horse_name_elements:
#         print(element.text)

# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# finally:
#     # Close the WebDriver session
#     driver.quit()


################# Scrape And Store Data In The CSV ##################
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import csv

# # Initialize the web driver (Chrome WebDriver should be in your PATH)
# driver = webdriver.Chrome()

# # Website URL
# url = 'https://photofinish.live/marketplace'

# try:
#     # Navigate to the URL
#     driver.get(url)

#     # Find the login button and click it
#     login_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//button[@data-cy="top-widget-login-button"]'))
#     )
#     login_button.click()

#     # Find the email and password input fields and enter the credentials
#     email = driver.find_element(By.NAME, 'email')
#     password = driver.find_element(By.NAME, 'password')

#     email.send_keys("kp5640907@gmail.com")
#     password.send_keys("Kathan#1910")

#     # Submit the login form
#     password.send_keys(Keys.RETURN)

#     # Wait for the login to complete (you may need to adjust the wait time)
#     WebDriverWait(driver, 10).until(EC.url_to_be(url))

#     # Handle the popup and click the "Continue" button
#     try:
#         popup_continue_button = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//button[text()="Continue"]'))
#         )
#         popup_continue_button.click()
#     except:
#         # If the "Continue" button doesn't appear, or there's any issue, continue without handling it
#         pass

#     # Initialize an empty list to store horse details
#     horse_details_list = []

#     # Scroll down until no more new elements are loaded
#     while True:
#         current_height = driver.execute_script("return document.body.scrollHeight;")
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#         # Add a delay to allow time for new elements to load (adjust the sleep duration as needed)
#         time.sleep(8)  # You can adjust the sleep duration

#         # Check if there are more elements loaded or if we've reached the end
#         new_height = driver.execute_script("return document.body.scrollHeight;")
#         if new_height == current_height:
#             break

#     # Find all the horse name elements
#     horse_name_elements = driver.find_elements(By.XPATH, '//p[@class="text-white w-full font-semibold truncate whitespace-nowrap"]')

#     # Extract and print horse details
#     for element in horse_name_elements:
#         horse_details = {'Horse Name': element.text}

#         # Find and add age if available
#         age_element = element.find_elements(By.XPATH, './/p[@class="text-white/75 text-xs pfmd:text-sm"]')
#         horse_details['Age'] = age_element[0].text if age_element else 'N/A'

#         # Find and add gender if available
#         gender_element = element.find_elements(By.XPATH, './/p[@class="text-xs pfmd:test-sm flex flex-row items-center text-pink-300"]')
#         horse_details['Gender'] = gender_element[0].text if gender_element else 'N/A'

#         # Find and add stable name if available
#         stable_element = element.find_elements(By.XPATH, './/p[@class="text-white/75 flex-1 text-xs truncate pfmd:text-sm"]')
#         horse_details['Stable Name'] = stable_element[0].text if stable_element else 'N/A'

#         # Find and add horse status if available
#         status_element = element.find_elements(By.XPATH, './/p[@class="text-white ml-1"]')
#         horse_details['Horse Status'] = status_element[0].text if status_element else 'N/A'

#         # Find and add price if available
#         price_element = element.find_elements(By.XPATH, './/div[@class="flex items-center flex-row space-x-1"]/span')
#         horse_details['Price'] = price_element[0].text if price_element else 'N/A'

#         horse_details_list.append(horse_details)

#     # Now you have a list of dictionaries containing horse details
#     # Print the details to verify
#     for horse in horse_details_list:
#         print(horse)

#     # Create and write horse details to a CSV file with UTF-8 encoding
#     with open('horse_details.csv', mode='w', newline='', encoding='utf-8') as csv_file:
#         fieldnames = ['Horse Name', 'Age', 'Gender', 'Stable Name', 'Horse Status', 'Price']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction='ignore')

#         writer.writeheader()
#         writer.writerows(horse_details_list)

# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# finally:
#     # Close the WebDriver session
#     driver.quit()


#####################  New Method ######################


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Initialize the web driver (Chrome WebDriver should be in your PATH)
# driver = webdriver.Chrome()

# # Website URL
# url = 'https://photofinish.live/marketplace'

# try:
#     # Navigate to the URL
#     driver.get(url)

#     # Find the login button and click it
#     login_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//button[@data-cy="top-widget-login-button"]'))
#     )
#     login_button.click()

#     # Find the email and password input fields and enter the credentials
#     email = driver.find_element(By.NAME, 'email')
#     password = driver.find_element(By.NAME, 'password')

#     email.send_keys("kp5640907@gmail.com")
#     password.send_keys("Kathan#1910")

#     # Submit the login form
#     password.send_keys(Keys.RETURN)

#     # Wait for the login to complete (you may need to adjust the wait time)
#     WebDriverWait(driver, 10).until(EC.url_to_be(url))

#     # Handle the popup and click the "Continue" button
#     try:
#         popup_continue_button = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//button[text()="Continue"]'))
#         )
#         popup_continue_button.click()
#     except:
#         # If the "Continue" button doesn't appear, or there's any issue, continue without handling it
#         pass

#     # Scroll down until no more new elements are loaded
#     while True:
#         current_height = driver.execute_script("return document.body.scrollHeight;")
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
#         # Add a delay to allow time for new elements to load (adjust the sleep duration as needed)
#         time.sleep(8)  # You can adjust the sleep duration
        
#         # Check if there are more elements loaded or if we've reached the end
#         new_height = driver.execute_script("return document.body.scrollHeight;")
#         if new_height == current_height:
#             break

#     # Find all the elements with class "text-white/75 text-xs pfmd:text-sm"
#     elements = driver.find_elements(By.XPATH, '//p[contains(@class, "text-white/75") and contains(@class, "text-xs") and contains(@class, "pfmd:text-sm")]')

#     # Extract and print the text within these elements
#     total_elements = len(elements)
#     print(f"Total Elements: {total_elements}")

#     for element in elements:
#         text = element.text
#         print(text)

# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# finally:
#     # Close the WebDriver session
#     driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Initialize the web driver (Chrome WebDriver should be in your PATH)
# driver = webdriver.Chrome()

# # Website URL
# url = 'https://photofinish.live/marketplace'

# try:
#     # Navigate to the URL
#     driver.get(url)

#     # Find the login button and click it
#     login_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//button[@data-cy="top-widget-login-button"]'))
#     )
#     login_button.click()

#     # Find the email and password input fields and enter the credentials
#     email = driver.find_element(By.NAME, 'email')
#     password = driver.find_element(By.NAME, 'password')

#     email.send_keys("kp5640907@gmail.com")
#     password.send_keys("Kathan#1910")

#     # Submit the login form
#     password.send_keys(Keys.RETURN)

#     # Wait for the login to complete (you may need to adjust the wait time)
#     WebDriverWait(driver, 10).until(EC.url_to_be(url))

#     # Handle the popup and click the "Continue" button
#     try:
#         popup_continue_button = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//button[text()="Continue"]'))
#         )
#         popup_continue_button.click()
#     except:
#         # If the "Continue" button doesn't appear, or there's any issue, continue without handling it
#         pass

#     # Scroll down until no more new elements are loaded
#     while True:
#         current_height = driver.execute_script("return document.body.scrollHeight;")
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
#         # Add a delay to allow time for new elements to load (adjust the sleep duration as needed)
#         time.sleep(8)  # You can adjust the sleep duration
        
#         # Check if there are more elements loaded or if we've reached the end
#         new_height = driver.execute_script("return document.body.scrollHeight;")
#         if new_height == current_height:
#             break

#     # Find all the elements with class "text-white/75 text-xs pfmd:text-sm" and "text-xs pfmd:test-sm flex flex-row items-center text-sky-300"
#     elements = driver.find_elements(By.XPATH, '//p[contains(@class, "text-white/75") and contains(@class, "text-xs") and contains(@class, "pfmd:text-sm")] | //p[contains(@class, "text-xs") and contains(@class, "pfmd:test-sm") and contains(@class, "flex flex-row items-center text-sky-300")]')

#     # Extract and print the text within these elements
#     total_elements = len(elements)
#     print(f"Total Elements: {total_elements}")

#     for element in elements:
#         text = element.text
#         print(text)

# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# finally:
#     # Close the WebDriver session
#     driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Initialize the web driver (Chrome WebDriver should be in your PATH)
driver = webdriver.Chrome()

# Website URL
url = 'https://photofinish.live/marketplace'

try:
    # Navigate to the URL
    driver.get(url)

    # Find the login button and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@data-cy="top-widget-login-button"]'))
    )
    login_button.click()

    # Find the email and password input fields and enter the credentials
    email = driver.find_element(By.NAME, 'email')
    password = driver.find_element(By.NAME, 'password')

    email.send_keys("kp5640907@gmail.com")
    password.send_keys("Kathan#1910")

    # Submit the login form
    password.send_keys(Keys.RETURN)

    # Wait for the login to complete (you may need to adjust the wait time)
    WebDriverWait(driver, 10).until(EC.url_to_be(url))

    # Handle the popup and click the "Continue" button
    try:
        popup_continue_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[text()="Continue"]'))
        )
        popup_continue_button.click()
    except:
        # If the "Continue" button doesn't appear, or there's any issue, continue without handling it
        pass

    # Scroll down until no more new elements are loaded
    while True:
        current_height = driver.execute_script("return document.body.scrollHeight;")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Add a delay to allow time for new elements to load (adjust the sleep duration as needed)
        time.sleep(8)  # You can adjust the sleep duration
        
        # Check if there are more elements loaded or if we've reached the end
        new_height = driver.execute_script("return document.body.scrollHeight;")
        if new_height == current_height:
            break

    # Find all the elements with class "text-white/75 text-xs pfmd:text-sm" and "text-xs pfmd:test-sm flex flex-row items-center text-sky-300"
    elements = driver.find_elements(By.XPATH, '//p[contains(@class, "text-white/75") and contains(@class, "text-xs") and contains(@class, "pfmd:text-sm")] | //p[contains(@class, "text-xs") and contains(@class, "pfmd:test-sm") and contains(@class, "flex flex-row items-center text-sky-300")]')

    # Extract and print the text within these elements
    total_elements = len(elements)
    print(f"Total Elements: {total_elements}")

    # Create a CSV file to save the data
    with open('horse_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Horse Age', 'Gender', 'Stable Name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header row to the CSV file
        writer.writeheader()

        for element in elements:
            text = element.text
            # Split the text based on "|" to separate the data
            data = [item.strip() for item in text.split(',')]
            
            # Check if the data list has enough elements
            if len(data) == 3:
                writer.writerow({'Horse Age': data[0], 'Gender': data[1], 'Stable Name': data[2]})
            else:
                print(f"Skipping invalid data: {text}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the WebDriver session
    driver.quit()
