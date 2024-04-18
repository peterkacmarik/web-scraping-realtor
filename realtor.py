import pandas as pd  # Importing the pandas library and aliasing it as pd
import logging  # Importing the logging module for logging purposes
import aiohttp  # Importing the aiohttp library for asynchronous HTTP requests
import asyncio  # Importing the asyncio library for asynchronous programming
import time  # Importing the time library for timing the operation


# Configure logging to provide detailed information about the scraping process
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

async def fetch_page(session, url, current_page):
    payload = f"ZoomLevel=4&LatitudeMax=66.10272&LongitudeMax=-43.94531&LatitudeMin=39.46164&LongitudeMin=-154.68750&Sort=6-D&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=0&Currency=FXUSDCAD&IncludeHiddenListings=false&RecordsPerPage=12&ApplicationId=1&CultureId=1&Version=7.0&CurrentPage={str(current_page)}"
    headers = {
    'accept': '*/*',
    'accept-language': 'sk-SK,sk;q=0.9,cs;q=0.8,en-US;q=0.7,en;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'visid_incap_2271082=AICSi4LfRE6XNZSJ0uE5UFbWDGYAAAAAQUIPAAAAAADR3RzQ2U3OPQMSxTuki1ig; nlbi_2271082=Klp1YFyRtWgJAE7sVPrQ3QAAAAA1WMxLF0pZhgMdmzZphhhx; nlbi_2271082_2147483392=nOAVEtA6UUwLrsL+VPrQ3QAAAAC8xQ1YsKQiFt1/ugWVbcbV; reese84=3:HyKnBQ/uhBEn8otu8GwPpw==:VegbjOAUs8j9imq8vDHfkUXGzlKk+0sUyIAGq2Pwps0eWCYzE6jJrfuvgOSztbEzXu/NQv74CzupClANAyv3xCZ+jA/9P8lK6n+0NpTzzFaGKouRtc6x9ukuAa7EH4iMRvNNhSgB0WgDDtyloOhkXqrYMaPxtGid+atcmDzirSKTArioUQFJx8ksZ4U5ktKRlRb0BGaHpdNOnan3GuezfiSNCiW9lvB4fOiSN+hlX2bsutKQJyaAUESg8ZERFSvdxBB40KWnJ4COLJxNm0iK4cWPwnTZ0dDypbsa9IlA/wtXG0F2Dj6YqQk2RLiYIb7v9H2HwVIAOgO2McCNOedCafBqXOKxCIUDP9S4nHzfrgHTI+4gHS8qiriF5BNSoCktwrXxRWu7o6YNZ5FUitf8uTRFVobaXQGdFYfIxk7NCx7PMAqzX29giEui1X73AYzCKN+vmGRHNHtdnuVQ0vaRbwt/LHGGeHZoa2ATOhyU/+mjILWZPBlSF4AeF++v/+Ti9P9ZNOxWWWnRAEWyCewh1A==:aIWqVhCBS2QLxieWPhVIqyeec94OQvlNWHUzkE8eD6E=; visid_incap_2269415=bs6Tz8gSTxinionzwKNPEC7WDGYAAAAAQkIPAAAAAACAyXKzAbL/qOAg7yuyIClbmSVCWJVPZQJX; incap_ses_471_2269415=FH07a2csC0I2N8nRDFSJBlUbIGYAAAAAMKTTf4MrwBAiEgUH3XjLaA==; reese84=3:+H5GZnFBSRrwmr8gvIa1aA==:KnCFx2s/D+jkBQbaKr0excmr5ANeb+Tgk8TaKWk5ykGR7oA0vd9TwzvsxuFM2yUlG4rhPyq6stIKPi36X6uctBFLklk/f4XapqZaUo9IkALBDmtun2tYzEugBBLE9dU4YiGsV0KLarh0MGnOOp3EAr8O5+DT/FgmBmRgt+asXGjmZN6nPPkrSWylS/u/X7ufOg+IWt1bmNCnHAFWoy8K5arHVG19MN6Zhqza5Q2PPWrU9uGkpR8habdNt8Ns/BEMdpbQq0TnXLhu1eQlMvaZFVR9BzDozqY6SVAKgvRzsC64fqQ1C0bF/6MMI6fJkNDuAGko0C0mQ/bvGrtSWq//bRdGZU9td2zqVSqA0LQHR5sEun/tcFDfPz80otl4iH4zVRSo7e2Lamy85qh4/smUW6soqa4oMvbVOM8wLku2cosIO7IwOMKk6B5bksMnMC3aKUvEZP92mIq8UvXoNYCkvW4U5mWscG204Cb9KRhTQp8=:kfIjwx7LUkOM6ip4hyKG/1tGBSQUjfi7jPZhX316EFs=; incap_ses_471_2271082=gRDSGrMeGwFkwcnRDFSJBpcbIGYAAAAA9AnOWHoTc+fn43RNXUilRg==; incap_ses_9197_2269415=dXV7cWtXIUD+GnRfyk6if5gbIGYAAAAA3HCUTv19COZUfZmgYevR9A==; incap_ses_471_2271082=0lvbXUqsVC0ZjsrRDFSJBgEcIGYAAAAA45OztjeDeCQjmIY36uoPyA==; visid_incap_2269415=4Mg4cvEXRF+jxMJWBHWemNzYDGYAAAAAQUIPAAAAAADdXudBGFMP1GY87B+J1CB4',
    'origin': 'https://www.realtor.ca',
    'referer': 'https://www.realtor.ca/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    async with session.post(url, headers=headers, data=payload) as response:
        # Check if the response status is 200 (OK)
        if response.status == 200:
            # Parse the JSON response
            json_data = await response.json()
            # Extract the 'Results' from the JSON data
            start_point = json_data['Results']
            detail_data = []
            
            # Check if 'start_point' contains any data
            if start_point:
                # Iterate through each item in 'start_point'
                for item in start_point:
                    # Extract relevant details from each item
                    list_data = {
                        'id': item['Id'],
                        'detail_url': item['RelativeDetailsURL'],
                        'province_name': item['ProvinceName'],
                        'postal_code': item['PostalCode'],
                        'bathrooms': item['Building'].get('BathroomTotal'),
                        'bedrooms': item['Building'].get('Bedrooms'),
                        'size_interior': item['Building'].get('SizeInterior'),
                        'ammenities': item['Building'].get('Ammenities'),
                        'type': item['Building'].get('Type'),
                        'price': item['Property'].get('Price'),
                      # another.....
                        'address': item['Property']['Address'].get('AddressText'),  # Extract address data
                    }
                    detail_data.append(list_data)
                # Log success message and return the list of extracted details
                logging.info(f'Successfully fetched page {current_page}')
                return detail_data
            else:
                # Log a warning if no estates are found on the page
                logging.warning(f'No estates found on page {current_page}')
                return False
        else:
            # Log an error message if fetching data fails
            logging.error(f"Error fetching data from {url}: {response.status}")
            return False

async def main():
    """
    The main function that handles the scraping process of multiple pages.
    It initializes necessary variables, fetches page details, processes and stores the data,
    and logs information about the operation's duration.
    """
    try:
        # Create an asynchronous context manager that will handle the session
        async with aiohttp.ClientSession() as session:
            # Set the URL for the API endpoint that serves the property listings
            url = "https://api2.realtor.ca/Listing.svc/PropertySearch_Post"

            # Set the starting page number
            page_number = 49

            # Initialize a flag to control the while loop
            running = True

            # Initialize an empty list to store page fetch results
            detail_tasks = []

            # Record the start time of the operation
            start_time = time.time()

            # Log a message to indicate that the scraping process has started
            logging.info("Scraping process started")

            # Continue looping as long as 'running' is True
            while running:
                try:
                    # Log a message to indicate the current page being processed
                    logging.info(f"Fetching page {page_number}")

                    # Asynchronously fetch the details of the current page
                    page_fetched = await fetch_page(session, url, page_number)

                    # If 'page_fetched' is empty or None, stop the loop
                    if page_fetched:
                        # Extend the 'detail_tasks' list with the results
                        detail_tasks.extend(page_fetched)
                        # Increment the current page number
                        page_number += 1
                    else:
                        running = False

                except Exception as e:
                    # Log an error message if an exception occurs
                    logging.error(f"Error while fetching page {page_number}: {e}")
                    # Stop the loop
                    running = False

            # If 'detail_tasks' is not empty, create a pandas DataFrame from the results
            if detail_tasks:
                df = pd.DataFrame(detail_tasks)

                # Print the DataFrame for debugging purposes
                print(df)

                # Save the DataFrame to a CSV file
                # df.to_csv("scrape realtor/realtor_output_data.csv", index=False, encoding="utf-8-sig")

                # Log a success message
                logging.info("Successfully created DataFrame with scraped data")

                # Calculate the duration of the operation
                end_time = time.time()
                duration = end_time - start_time

                # Convert the duration to minutes and seconds
                minutes, seconds = divmod(duration, 60)

                # Log the duration of the operation
                logging.info(
                    f"This operation took {int(minutes)} minutes {int(seconds):.0f} seconds"
                )
            # If 'detail_tasks' is empty, log an error message
            else:
                logging.error("No data scraped, aborting.")

    # Log an error message if an unhandled exception occurs
    except Exception as e:
        logging.exception(f"Unhandled exception in main(): {e}")

if __name__ == "__main__":
    asyncio.run(main())
