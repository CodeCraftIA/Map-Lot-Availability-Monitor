import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

# Suppress info messages from WebDriver
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('selenium').setLevel(logging.WARNING)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")  # Set log level to SEVERE

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

url = "https://myscp.ml3ds-icon.com/scp/86530/site-map/90023?standalone=true"

driver.get(url)

# Wait for the page to fully load (adjust the sleep time as needed)
time.sleep(15)

# Get the page source after JavaScript execution
page_source = driver.page_source

driver.quit()

# List of lots to monitor
lots_to_monitor = [1, 2, 3, 69, 70, 68, 71]

# Function to check if a lot is available
def check_lot_availability(source, lot):
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(source, 'html.parser')

    container = soup.find('div', class_="svg-container")

    # Find the <g> element with aria-label="Lot 70"
    lots = container.find('g', id='Lots')
    lot_number = 'Lot ' + str(lot)
    specific_lot = lots.find('g', attrs={'aria-label': lot_number})

    # Convert find_arial to a string
    lot_str = str(specific_lot)

    # Check if the color is in the string representation of find_arial
    if 'rgb(242, 169, 0)' in lot_str:
        return True
    else:
        return False
    

for lot in lots_to_monitor:
    print("checking lot number: ", lot, "...")
    if check_lot_availability(page_source, lot):
        print("Orange color found")
    else:
        print("No orange color")
