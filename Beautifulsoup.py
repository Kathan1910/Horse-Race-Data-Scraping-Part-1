# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
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
#         # If the "Continue" button doesn't appear or there's any issue, continue without handling it
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

#     # Get the HTML source of the page
#     page_source = driver.page_source

#     # Parse the HTML content with BeautifulSoup
#     soup = BeautifulSoup(page_source, 'html.parser')

#     # Now you have the entire HTML content of the page in 'soup'

#     # For example, let's find and print all links on the page
#     all_links = soup.find_all('a')
#     for link in all_links:
#         print(link.get('href'))

# finally:
#     # Close the browser when done
#     driver.quit()


#################### Scraping Actual Elements #####################

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
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

#     # Get the HTML source of the page
#     page_source = driver.page_source

#     # Parse the HTML content with BeautifulSoup
#     soup = BeautifulSoup(page_source, 'html.parser')

#     # Find and print the specific elements you want to scrape
#  # Find and print the specific elements you want to scrape
#     horse_name_element = soup.find('div', class_='text-white text-[14px] font-bold')
#     horse_name = horse_name_element.text if horse_name_element else 'N/A'

#     horse_age_element = soup.find('div', class_='').find('span', text='Age:')
#     horse_age = horse_age_element.next_sibling.strip() if horse_age_element else 'N/A'

#     fleet_figure_element = soup.find('span', class_='text-xs')
#     fleet_figure = fleet_figure_element.text if fleet_figure_element else 'N/A'

#     horse_status_element = soup.find('div', class_='flex flex-row')
#     horse_status = horse_status_element.text if horse_status_element else 'N/A'

#     gender_element = soup.find('div', class_='ml-1 pl-1 border-l border-gray-100/20').find('span')
#     gender = gender_element.text if gender_element else 'N/A'

#     price_element = soup.find('div', class_='flex items-center flex-row space-x-1').find('span')
#     price = price_element.text.strip() if price_element else 'N/A'

#     print(f'Horse Name: {horse_name}')
#     print(f'Horse Age: {horse_age}')
#     print(f'Fleet Figure: {fleet_figure}')
#     print(f'Horse Status: {horse_status}')
#     print(f'Gender: {gender}')
#     print(f'Price: {price}')

# finally:
#     # Close the browser when done
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
#         # If the "Continue" button doesn't appear or there's any issue, continue without handling it
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

#     # Find the outermost container
#     outer_container = driver.find_element(By.CLASS_NAME, 'infinite-scroll-component__outerdiv')

#     # Find the container that holds the horse details
#     horse_container = outer_container.find_element(By.CLASS_NAME, 'flex flex-col gap-3 striped-list')

#     # Find all the horse elements within the container
#     horse_elements = horse_container.find_elements(By.XPATH, './/div[contains(@class, "duration-150 transition-all flex overflow-hidden box-border")]')

#     # Iterate through each horse element and extract the details
#     for horse_element in horse_elements:
#         # Extract horse name
#         horse_name_element = horse_element.find_element(By.XPATH, './/div[@class="text-white text-[14px] font-bold"]')
#         horse_name = horse_name_element.text if horse_name_element else 'N/A'

#         # Extract horse age
#         horse_age_element = horse_element.find_element(By.XPATH, './/div[contains(span, "Age:")]/span')
#         horse_age = horse_age_element.text if horse_age_element else 'N/A'

#         # Extract fleet figure
#         fleet_figure_element = horse_element.find_element(By.XPATH, './/span[@class="text-xs"]')
#         fleet_figure = fleet_figure_element.text if fleet_figure_element else 'N/A'

#         # Extract horse status
#         horse_status_element = horse_element.find_element(By.XPATH, './/div[@class="flex flex-row"]')
#         horse_status = horse_status_element.text if horse_status_element else 'N/A'

#         # Extract gender
#         gender_element = horse_element.find_element(By.XPATH, './/div[@class="ml-1 pl-1 border-l border-gray-100/20"]/span')
#         gender = gender_element.text if gender_element else 'N/A'

#         # Extract price
#         price_element = horse_element.find_element(By.XPATH, './/div[@class="flex items-center flex-row space-x-1"]/span')
#         price = price_element.text.strip() if price_element else 'N/A'

#         # Print or process the collected data as needed
#         print(f'Horse Name: {horse_name}')
#         print(f'Horse Age: {horse_age}')
#         print(f'Fleet Figure: {fleet_figure}')
#         print(f'Horse Status: {horse_status}')
#         print(f'Gender: {gender}')
#         print(f'Price: {price}')
#         print('-' * 40)

# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# finally:
#     # Close the browser when done
#     driver.quit()

############ Horse Name Elemets ##############
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.webdriver.common.keys import Keys

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



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

    # Find all the horse elements
    horse_elements = driver.find_elements(By.XPATH, '//div[@class="duration-150 transition-all flex overflow-hidden box-border h-[88px] w-full relative pr-2 border-transparent border bg-[#0F303E] hover:cursor-pointer hover:bg-primary-600 hover:bg-opacity-30 md:h-auto"]')

    # Iterate through each horse element and extract details
    for horse_element in horse_elements:
        horse_name = horse_element.find_element(By.XPATH, './/div[@class="text-white text-[14px] font-bold"]').text
        horse_age_element = horse_element.find_element(By.XPATH, './/div[@class=""]/span[contains(text(), "Age:")]')
        horse_age = horse_age_element.text.replace('Age:', '').strip()
        fleet_figure_element = horse_element.find_element(By.XPATH, './/span[@class="text-xs"]')
        fleet_figure = fleet_figure_element.text
        horse_status_element = horse_element.find_element(By.XPATH, './/div[@class="flex flex-row"]')
        horse_status = horse_status_element.text
        gender_element = horse_element.find_element(By.XPATH, './/div[@class="ml-1 pl-1 border-l border-gray-100/20"]/span')
        gender = gender_element.text
        price_element = horse_element.find_element(By.XPATH, './/div[@class="flex items-center flex-row space-x-1"]/span')
        price = price_element.text.strip()

        # Print the extracted details
        print(f"Horse Name: {horse_name}")
        print(f"Horse Age: {horse_age}")
        print(f"Fleet Figure: {fleet_figure}")
        print(f"Horse Status: {horse_status}")
        print(f"Gender: {gender}")
        print(f"Price: {price}")
        print()

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the WebDriver session
    driver.quit()
