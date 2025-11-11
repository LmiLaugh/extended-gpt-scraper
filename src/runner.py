thonimport sys
import os
import json
import logging
from extractors.webpage_scraper import scrape_website
from processors.gpt_integration import process_with_gpt
from config.settings import CONFIG

logging.basicConfig(level=logging.INFO)

def main():
    try:
        # Load start URLs and configuration
        with open(CONFIG['input_file'], 'r') as f:
            start_urls = f.readlines()

        scraped_data = []
        for url in start_urls:
            url = url.strip()
            content = scrape_website(url)
            gpt_result = process_with_gpt(content, CONFIG['gpt_instructions'])
            scraped_data.append(gpt_result)

        # Save the results
        with open(CONFIG['output_file'], 'w') as f:
            json.dump(scraped_data, f, indent=4)

    except Exception as e:
        logging.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()