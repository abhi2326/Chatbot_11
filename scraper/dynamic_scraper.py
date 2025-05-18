from playwright.sync_api import sync_playwright

def scrape_dynamic(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until='networkidle')
        content = page.content()
        browser.close()
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text(separator=' ', strip=True)