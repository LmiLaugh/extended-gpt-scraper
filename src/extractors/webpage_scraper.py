thonimport playwright.sync_api as p
import logging

def scrape_website(url):
    try:
        browser = p.sync_playwright().start().firefox.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Extract page content
        content = page.content()

        browser.close()
        return content

    except Exception as e:
        logging.error(f"Error scraping website {url}: {e}")
        raise