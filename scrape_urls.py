# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from bs4 import BeautifulSoup

# # # Initialize the web driver (Chrome WebDriver should be in your PATH)
# # driver = webdriver.Chrome()

# # # Website URL
# # url = 'https://photofinish.live/marketplace'

# # try:
# #     # Navigate to the URL
# #     driver.get(url)

# #     # Find the login button and click it
# #     login_button = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.XPATH, '//button[@data-cy="top-widget-login-button"]'))
# #     )
# #     login_button.click()

# #     # Find the email and password input fields and enter the credentials
# #     email = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.NAME, 'email'))
# #     )
# #     password = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.NAME, 'password'))
# #     )

# #     email.send_keys("kp5640907@gmail.com")
# #     password.send_keys("Kathan#1910")

# #     # Submit the login form
# #     password.send_keys(Keys.RETURN)

# #     # Wait for the login to complete (you may need to adjust the wait time)
# #     WebDriverWait(driver, 10).until(EC.url_to_be(url))

# #     # Handle the popup and click the "Continue" button
# #     try:
# #         popup_continue_button = WebDriverWait(driver, 10).until(
# #             EC.presence_of_element_located((By.XPATH, '//button[text()="Continue"]'))
# #         )
# #         popup_continue_button.click()
# #     except:
# #         # If the "Continue" button doesn't appear, or there's any issue, continue without handling it
# #         pass

# #     # Scroll down until no more new elements are loaded
# #     while True:
# #         current_height = driver.execute_script("return document.body.scrollHeight;")
# #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# #         # Wait for a short duration to allow time for new elements to load
# #         driver.implicitly_wait(8)

# #         # Check if there are more elements loaded or if we've reached the end
# #         new_height = driver.execute_script("return document.body.scrollHeight;")
# #         if new_height == current_height:
# #             break

# #     # Get the page source after logging in
# #     page_source = driver.page_source

# #     # Parse the page source with BeautifulSoup
# #     soup = BeautifulSoup(page_source, 'html.parser')

# #     # Find all anchor elements with class "w-full h-auto"
# #     anchor_elements = soup.find_all('a', class_='w-full h-auto')

# #     # Extract the href URLs from the anchor elements
# #     href_urls = [a['href'] for a in anchor_elements]

# #     # Print the extracted href URLs
# #     for href in href_urls:
# #         print(href)

# # except Exception as e:
# #     print(f"An error occurred: {str(e)}")

# # finally:
# #     # Close the WebDriver session
# #     driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# from selenium import webdriver
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
#     email = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, 'email'))
#     )
#     password = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, 'password'))
#     )

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


#     # Scroll down to load all the content (you can modify the scroll height if needed)
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(8)  # Adjust the sleep duration as needed
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height

#     # Execute JavaScript to extract all href links
#     href_links = driver.execute_script('''
#         const links = [];
#         const elements = document.querySelectorAll('a');
#         elements.forEach(function(element) {
#             const href = element.getAttribute('href');
#             if (href) {
#                 links.push(href);
#             }
#         });
#         return links;
#     ''')

#     # Print the extracted href links
#     for link in href_links:
#         print(link)

# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# finally:
#     # Close the WebDriver session
#     driver.quit()

############ Filtering The Urls ##############


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv
import re

# Initialize the web driver (Chrome WebDriver should be in your PATH)
driver = webdriver.Chrome()

# Website URL
url = 'https://photofinish.live/marketplace'

# Regular expression pattern to match the specified format
pattern = r'^/marketplace/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'

try:
    # Navigate to the URL
    driver.get(url)

    # Find the login button and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@data-cy="top-widget-login-button"]'))
    )
    login_button.click()

    # Find the email and password input fields and enter the credentials
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    )
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )

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

    # Scroll down to load all the content (you can modify the scroll height if needed)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(8)  # Adjust the sleep duration as needed
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Execute JavaScript to extract all href links
    href_links = driver.execute_script('''
        const links = [];
        const elements = document.querySelectorAll('a');
        elements.forEach(function(element) {
            const href = element.getAttribute('href');
            if (href) {
                links.push(href);
            }
        });
        return links;
    ''')

    # Filter URLs based on the pattern
    filtered_urls = [link for link in href_links if re.match(pattern, link)]

    # Count the filtered URLs
    count = len(filtered_urls)

    # Print the extracted href links
    for link in filtered_urls:
        print(link)

    # Store filtered URLs in a CSV file
    with open('filtered_urls.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Filtered URLs'])
        csvwriter.writerows([[url] for url in filtered_urls])

    print(f"Filtered URLs count: {count}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the WebDriver session
    driver.quit()
