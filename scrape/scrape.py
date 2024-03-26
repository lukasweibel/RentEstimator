import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from db.db_accessor import add_entry_to_db, delete_all_entries
import csv
import sys
from pathlib import Path

from utils.utils import extract_zip_code, extract_number, mixed_number_to_decimal

def start_scraping():
    timeout = 3000
    
    # Read cities from file
    with open('cities.txt', 'r') as file:
        cities = [line.strip() for line in file.readlines()]

    def run(playwright):

        #Duplicates are skipped. Because of that no delete_all_entries() are skipped
        #delete_all_entries()
        failures = 0
        
        browser = playwright.chromium.launch(headless=True)

        for city in cities:
            context = browser.new_context()
            page = context.new_page()
            base_url = "https://flatfox.ch/de/search/?&query={}&object_category=APARTMENT"
            page.goto(base_url.format(city))

            page.wait_for_selector('.listing-thumb-title__location')

            index = 0
            while True:
                try:
                    while len(page.query_selector_all('.listing-thumb-title')) <= index:
                        mehr_anzeigen_button = page.locator('text="Mehr anzeigen"')
                        if mehr_anzeigen_button.is_visible():
                            page.get_by_label("Mehr anzeigen").click()
                            page.wait_for_selector('.listing-thumb-title')
                        else:
                            break

                    print("length: "+str(len(page.query_selector_all('.listing-thumb-title'))))

                    current_listing = page.query_selector_all('.listing-thumb-title')[index]
                    current_listing.click()

                    address_value = page.query_selector('h2').text_content()

                    net_rent_selector = 'text="Bruttomiete (inkl. NK):"'
                    page.wait_for_selector(net_rent_selector, timeout=timeout)
                    net_rent_value = page.locator(f'{net_rent_selector} >> xpath=following-sibling::td').first.inner_text()

                    area_selector = 'text="Wohnfläche:"'
                    page.wait_for_selector(area_selector, timeout=timeout)
                    area_value = page.locator(f'{area_selector} >> xpath=following-sibling::td').first.inner_text()

                    rooms_selector = 'text="Anzahl Zimmer:"'
                    page.wait_for_selector(rooms_selector, timeout=timeout)
                    rooms_value = page.locator(f'{rooms_selector} >> xpath=following-sibling::td').first.inner_text()

                    print(f"Nettomiete (exkl. NK): {extract_number(net_rent_value)}\nFläche: {extract_number(area_value)}\nPostleitzahl: {extract_zip_code(address_value)}\nAnzahl Räume: {mixed_number_to_decimal(rooms_value)}")
                    print("")
                    add_entry_to_db(extract_number(net_rent_value), extract_number(area_value), mixed_number_to_decimal(rooms_value), extract_zip_code(address_value))
                except PlaywrightTimeoutError as e:
                    print(f"Encountered a timeout: {e}")
                    failures = failures + 1
                finally:
                    index = index + 1
                    page.go_back()
                    try:
                        page.wait_for_selector('.listing-thumb-title__location', timeout=timeout)
                    except PlaywrightTimeoutError as e:
                        print(f"Encountered a timeout: {e}")
                        break

        context.close()
        browser.close()
        print("fauilures: " + str(failures))

    # Start the Playwright session and run the scraping process
    with sync_playwright() as playwright:
        run(playwright)

# Function to manually start the scraping process
def run_scraping():
    print("Starting scraping process...")
    start_scraping()
    print("Scraping process finished.")

if __name__ == "__main__":
    run_scraping()
