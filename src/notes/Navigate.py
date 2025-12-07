from playwright.sync_api import sync_playwright

BASE_URL = 'https://tap-vt25-testverktyg.github.io/exam--reading-list/'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=30000)
    page = browser.new_page()
    page.goto(BASE_URL)


    # Locators

    ## go to add new book
    add_book_btn = page.get_by_role('button', name='Lägg till bok')
    add_book_btn.click()

    ## select the Title input
    add_title = page.get_by_label('Titel')
    add_title.highlight()

    ##  select authors input
    add_author = page.get_by_label('Författare')
    add_author.highlight()

    ## click favorite
    favorite_btn = page.get_by_role('button', name='Mina böcker')
    favorite_btn.click()

    browser.close()