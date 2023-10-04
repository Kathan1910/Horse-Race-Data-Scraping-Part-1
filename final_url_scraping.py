# import csv

# # Open the CSV file and read the URLs into a list
# csv_file = "filtered_urls.csv"
# url_list = []

# try:
#     with open(csv_file, "r") as file:
#         csv_reader = csv.reader(file)
#         for row in csv_reader:
#             # Assuming the URL is in the first column (index 0)
#             url = row[0]
#             url_list.append(url)
# except FileNotFoundError:
#     print(f"CSV file '{csv_file}' not found.")
# except Exception as e:
#     print(f"An error occurred while reading the CSV file: {str(e)}")

# # Check if URLs were successfully loaded
# if url_list:
#     # Print the count of URLs
#     print(f"Total URLs to process: {len(url_list)}")

#     # Iterate through the URLs and process them one by one
#     for url in url_list:
#         # Construct the complete URL by replacing `{csv url}` in the static URL
#         static_url = "https://photofinish.live/{}".format(url)

#         # Now you have the complete URL, and you can proceed to scrape information from it.
#         # Please specify the information or elements you want to scrape, and I'll help you
#         # write the scraping logic for that.
#         print("Processing URL:", static_url)
# else:
#     print("No URLs found in the CSV file.")


import csv

# Open the CSV file and read the URLs into a list
csv_file = "filtered_urls.csv"
url_list = []

try:
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Assuming the URL is in the first column (index 0)
            url = row[0]
            url_list.append(url)
except FileNotFoundError:
    print(f"CSV file '{csv_file}' not found.")
except Exception as e:
    print(f"An error occurred while reading the CSV file: {str(e)}")

# Check if URLs were successfully loaded
if url_list:
    # Print the count of URLs
    print(f"Total URLs to process: {len(url_list)}")

    # Create a list to store the final URLs
    final_url_list = []

    # Iterate through the URLs and process them one by one
    for url in url_list:
        # Construct the complete URL by replacing `{csv url}` in the static URL
        static_url = "https://photofinish.live/{}".format(url)

        # Now you have the complete URL, and you can proceed to scrape information from it.
        # Please specify the information or elements you want to scrape, and I'll help you
        # write the scraping logic for that.
        print("Processing URL:", static_url)

        # Append the final URL to the list
        final_url_list.append(static_url)

    # Save the final URLs to a CSV file
    final_csv_file = "final_urls.csv"
    with open(final_csv_file, "w", newline="") as final_file:
        csv_writer = csv.writer(final_file)
        for url in final_url_list:
            csv_writer.writerow([url])

    print(f"Final URLs have been saved to '{final_csv_file}'")
else:
    print("No URLs found in the CSV file.")
