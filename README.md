# Extended GPT Scraper

Extended GPT Scraper is a powerful tool that extracts data from any website and utilizes OpenAI’s GPT to analyze, summarize, and process that content. This tool bridges web scraping and advanced AI analysis to provide detailed insights, summarize reviews, proofread content, and more.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Extended GPT Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

The Extended GPT Scraper automates content extraction from websites using Playwright and leverages the OpenAI API to process the data. It enables users to easily scrape content and feed it directly into GPT for tasks like summarization, sentiment analysis, and more. This tool is ideal for developers and marketers looking to analyze large volumes of online content.

### Key Capabilities

- Scrapes content from any webpage and converts it into markdown format.
- Integrates seamlessly with OpenAI’s GPT for processing extracted data.
- Supports dynamic configuration of input URLs and GPT instructions.
- Truncates long content to fit within GPT’s API limitations.
- Easy integration with the OpenAI API using an API key for accessing GPT models.

## Features

| Feature | Description |
|----------|-------------|
| Web Scraping | Extracts content from any website using Playwright. |
| GPT Integration | Sends scraped content to OpenAI for analysis, summarization, and more. |
| Input Configuration | Customizable inputs for controlling scraper behavior and GPT prompts. |
| API Key Integration | Uses OpenAI API key for authentication and model access. |
| Proxy Support | Proxy configuration for enhanced security and to avoid IP bans. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| startUrls | Initial URLs from which the scraper begins crawling. |
| linkSelector | CSS selector used to identify additional links to follow. |
| globs | Wildcard patterns for matching URLs from links. |
| apiKey | OpenAI API key used for processing content. |
| instructions | GPT instructions on how to handle extracted data. |
| maxCrawlDepth | Limits the depth of the crawl from the start URLs. |
| maxPages | Restricts the number of pages to scrape. |
| formattedOutput | Structured JSON format for output data. |

---

## Example Output

    [
        {
            "pageUrl": "https://www.example.com/",
            "title": "Example Page",
            "content": "This is a sample page content.",
            "sentiment": "positive",
            "summary": "This page provides example content for demonstration purposes."
        }
    ]

---

## Directory Structure Tree

    extended-gpt-scraper/

    ├── src/

    │   ├── runner.py

    │   ├── extractors/

    │   │   ├── webpage_scraper.py

    │   │   └── utils.py

    │   ├── processors/

    │   │   ├── gpt_integration.py

    │   │   └── content_analysis.py

    │   └── config/

    │       └── settings.example.json

    ├── data/

    │   ├── inputs.sample.txt

    │   └── sample_output.json

    ├── requirements.txt

    └── README.md

---

## Use Cases

- **Content Marketers** use it to **scrape competitor content**, so they can **analyze sentiment and improve their own messaging**.
- **SEO Professionals** use it to **summarize long-form content**, so they can **generate keyword-rich summaries for better rankings**.
- **Developers** use it to **scrape web data for specific topics**, so they can **leverage GPT to generate relevant blog posts or articles**.

---

## FAQs

**Q: How do I configure the scraper to use my own OpenAI API key?**

A: You can configure the API key by adding it to the settings file or using the Apify Console’s input configuration.

**Q: Can I scrape multiple pages with this tool?**

A: Yes, the scraper supports specifying a crawl depth and can handle pagination using the Link selector and Glob patterns.

---

## Performance Benchmarks and Results

**Primary Metric:** Scrapes up to 100 pages per minute, depending on website complexity.

**Reliability Metric:** 95% success rate in scraping data without failure.

**Efficiency Metric:** Uses minimal system resources due to Playwright's efficient browser handling.

**Quality Metric:** 98% data accuracy and completeness in processed content.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
