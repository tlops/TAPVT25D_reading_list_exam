from playwright.sync_api import sync_playwright

BASE_URL = 'https://tap-vt25-testverktyg.github.io/exam--reading-list/'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True, slow_mo=10000)
    page = browser.new_page()
    page.goto(BASE_URL)

    # highlight the last item
    available_books = page.locator('div.catalog > div.book').count()
    #last_book = page.locator('div.catalog > div.book').nth(available_books - 1).inner_text().strip()
    #last_book
    books = page.locator("div.catalog > div.book")
    last_book = books.nth(books.count() - 1).inner_text().strip()
    print(last_book)

    # close browser
    browser.close()
