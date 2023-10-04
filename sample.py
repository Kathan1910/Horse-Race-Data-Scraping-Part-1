# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import re

# # Initialize the web driver (Chrome WebDriver should be in your PATH)
# driver = webdriver.Chrome()

# # Website URL
# url = 'https://photofinish.live//marketplace/f0581bd3-7210-43b9-ae76-e0112668882e'  # Your specific URL here

# try:
#     # Navigate to the URL
#     driver.get(url)

#     # Wait for the page to load (you may need to adjust the wait time)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="flex flex-row gap-2"]')))

#     # Get the page source after navigating to the specific link
#     page_source = driver.page_source

#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(page_source, 'html.parser')

#      # Scrape the desired information
#     horse_name = soup.find('div', class_='flex flex-row gap-2').find('span', class_='text-2xl').text.strip() if soup.find('div', class_='flex flex-row gap-2') else None
#     age = soup.find('div', class_='flex flex-row max-w-full whitespace-nowrap sm:text-xs').find('span').text.strip() if soup.find('div', class_='flex flex-row max-w-full whitespace-nowrap sm:text-xs') else None
#     fleet_figure = soup.find('span', class_='text-xs').text.strip() if soup.find('span', class_='text-xs') else None
#     gender = soup.find('div', class_='flex flex-row justify-start items-center text-sky-300').text.strip() if soup.find('div', class_='flex flex-row justify-start items-center text-sky-300') else None
#     stable_name = soup.find('a', class_='text-secondary-100/80 hover:text-secondary-400 underline block pl-1 cursor-pointer').text.strip() if soup.find('a', class_='text-secondary-100/80 hover:text-secondary-400 underline block pl-1 cursor-pointer') else None
    
#     # Extracting the price using a regular expression
#     price_pattern = r'Purchase (\d+,\d+\.\d+)'
#     price_match = re.search(price_pattern, page_source)
#     if price_match:
#         horse_price = price_match.group(1)
#     else:
#         horse_price = None

#    # Extracting the horse's status
#     status_elements = soup.find_all('div', class_='flex flex-row') + soup.find_all('p', class_='text-white ml-1')
#     horse_status = None

#     for element in status_elements:
#         if 'Retired' in element.text:
#             horse_status = 'Retired'
#             break
#         elif 'Exhausted' in element.text:
#             horse_status = 'Exhausted'
#             break
#         elif 'Foal' in element.text:
#             horse_status = 'Foal'
#             break
#         elif 'Ready to Race!' in element.text:
#             horse_status = 'Ready to Race!'
#         break

#     # Extracting Starts(W-P-S)
#     starts_element = soup.find('p', class_='text-sm text-white font-inter')
#     starts_data = starts_element.text.strip() if starts_element else None

#     # Extracting Career Earnings
#     earnings_element = soup.find('p', class_='text-sm text-slate-300')
#     career_earnings = earnings_element.text.strip() if earnings_element else None

#     # Extracting Largest Purse
#     purse_element = soup.find('p', class_='text-sm text-slate-300')
#     largest_purse = purse_element.text.strip() if purse_element else None

#     # Extracting Career Injuries
#     injuries_element = soup.find('p', class_='font-inter text-sm text-white')
#     career_injuries = injuries_element.text.strip() if injuries_element else None

#     # Print the scraped information
#     print("Horse Name:", horse_name)
#     print("Age:", age)
#     print("Fleet Figure:", fleet_figure)
#     print("Gender:", gender)
#     print("Stable Name:", stable_name)
#     print("Horse Price:", horse_price)
#     print("Horse Status:", horse_status)
#     print("Starts(W-P-S):", starts_data)
#     print("Career Earnings:", career_earnings)
#     print("Largest Purse:", largest_purse)
#     print("Career Injuries:", career_injuries)

#     # Save the scraped data to a DataFrame
#     scraped_data = pd.DataFrame({
#         'Horse Name': [horse_name],
#         'Age': [age],
#         'Fleet Figure': [fleet_figure],
#         'Gender': [gender],
#         'Stable Name': [stable_name],
#         'Horse Price': [horse_price],
#         'Horse Status': [horse_status],
#         'Starts(W-P-S)': [starts_data],
#         'Career Earnings': [career_earnings],
#         'Largest Purse': [largest_purse],
#         'Career Injuries': [career_injuries]
#     })

#     # Save the DataFrame to a CSV file
#     scraped_data.to_csv('scraped_data.csv', index=False)
   
#    # Scroll to the CSV download button
#     csv_download_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download CSV")]'))
# )
#     csv_download_button.click()

#     # Wait for the download to complete (you may need to adjust the wait time)
#     time.sleep(10)  # Adjust as needed

# except Exception as e:
#     print("An error occurred:", str(e))

# finally:
#     # Close the browser window when done
#     driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

# Initialize the web driver (Chrome WebDriver should be in your PATH)
driver = webdriver.Chrome()

# Website URL
url = 'https://photofinish.live//marketplace/ca1d0990-470d-4d7f-b87e-468671458921'  # Your specific URL here

try:
    # Navigate to the URL
    driver.get(url)

    # Wait for the page to load (you may need to adjust the wait time)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="flex flex-row gap-2"]')))

    # Get the page source after navigating to the specific link
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Scrape the desired information
    horse_name = soup.find('div', class_='flex flex-row gap-2').find('span', class_='text-2xl').text.strip() if soup.find('div', class_='flex flex-row gap-2') else None
    age = soup.find('div', class_='flex flex-row max-w-full whitespace-nowrap sm:text-xs').find('span').text.strip() if soup.find('div', class_='flex flex-row max-w-full whitespace-nowrap sm:text-xs') else None
    fleet_figure = soup.find('span', class_='text-xs').text.strip() if soup.find('span', class_='text-xs') else None
    # gender = soup.find('div', class_='flex flex-row justify-start items-center text-sky-300').text.strip() if soup.find('div', class_='flex flex-row justify-start items-center text-sky-300') else None
    stable_name = soup.find('a', class_='text-secondary-100/80 hover:text-secondary-400 underline block pl-1 cursor-pointer').text.strip() if soup.find('a', class_='text-secondary-100/80 hover:text-secondary-400 underline block pl-1 cursor-pointer') else None
    
    # Check for gender in the first location
    gender_element = soup.find('div', class_='flex flex-row justify-start items-center text-sky-300')
    if gender_element:
        gender = gender_element.text.strip()
    else:
    # If not found in the first location, check the second location
        gender_element = soup.find('div', class_='flex flex-row justify-start items-center text-pink-300')
        if gender_element:
            gender = gender_element.text.strip()
        else:
            gender = None
    
    # Extracting the price using a regular expression
    price_pattern = r'Purchase (\d+,\d+\.\d+)'
    price_match = re.search(price_pattern, page_source)
    if price_match:
        horse_price = price_match.group(1)
    else:
        horse_price = None

   # Extracting the horse's status
    status_elements = soup.find_all('div', class_='flex flex-row') + soup.find_all('p', class_='text-white ml-1')
    horse_status = None

    for element in status_elements:
        if 'Retired' in element.text:
            horse_status = 'Retired'
            break
        elif 'Exhausted' in element.text:
            horse_status = 'Exhausted'
            break
        elif 'Foal' in element.text:
            horse_status = 'Foal'
            break
        elif 'Ready to Race!' in element.text:
            horse_status = 'Ready to Race!'
        elif 'Pregnant' in element.text:
            horse_status = 'Pregnant'
            break

    # Extracting Starts(W-P-S)
    starts_element = soup.find('p', class_='text-sm text-white font-inter')
    starts_data = starts_element.text.strip() if starts_element else None

    # Example code for extracting career earnings
    career_earnings_element = soup.find_all('p', class_='text-sm text-slate-300')
    if len(career_earnings_element) >= 1:
        career_earnings = career_earnings_element[0].text.strip()
    else:
        career_earnings = None

    # Example code for extracting largest purse
    if len(career_earnings_element) >= 2:
        largest_purse = career_earnings_element[1].text.strip()
    else:
        largest_purse = None


    # Extracting Career Injuries
    injuries_element = soup.find('p', class_='font-inter text-sm text-white')
    career_injuries = injuries_element.text.strip() if injuries_element else None

    # Print the scraped information
    print("Horse Name:", horse_name)
    print("Age:", age)
    print("Fleet Figure:", fleet_figure)
    print("Gender:", gender)
    print("Stable Name:", stable_name)
    print("Horse Price:", horse_price)
    print("Horse Status:", horse_status)
    print("Starts(W-P-S):", starts_data)
    print("Career Earnings:", career_earnings)
    print("Largest Purse:", largest_purse)
    print("Career Injuries:", career_injuries)

    # Save the scraped data to a DataFrame
    scraped_data = pd.DataFrame({
        'Horse Name': [horse_name],
        'Age': [age],
        'Fleet Figure': [fleet_figure],
        'Gender': [gender],
        'Stable Name': [stable_name],
        'Horse Price': [horse_price],
        'Horse Status': [horse_status],
        'Starts(W-P-S)': [starts_data],
        'Career Earnings': [career_earnings],
        'Largest Purse': [largest_purse],
        'Career Injuries': [career_injuries]
    })


    # Save the DataFrame to a CSV file (customize the filename and path as needed)
    scraped_data.to_csv('scraped_data.csv', index=False)

    try:
        # Scroll to the CSV download button
        csv_download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download CSV")]'))
        )
        csv_download_button.click()

        # Wait for the download to complete (you may need to adjust the wait time)
        time.sleep(10)  # Adjust as needed

    except Exception as e:
        print("CSV not available.")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser window when done
    driver.quit()

