from playwright.sync_api import Page

class CatalogPage:
    def __init__(self, page: Page):
        self.page = page

    # --- NAVIGATION ---
    def click_add_book_nav(self):
        self.page.locator('button[data-testid="add-book"]').click()

    def click_catalog_nav(self):
        self.page.locator('button[data-testid="catalog"]').click()

    def click_favorites_nav(self):
        self.page.locator('button[data-testid="favorites"]').click()

    # --- CATALOG LIST ---
    def catalog_list(self):
        return self.page.locator('div.catalog > div.book')
    
   
    def catalog_items(self):
        book_list = self.page.locator('div.catalog > div.book')
        return [book_list.nth(i).inner_text().strip() for i in range(book_list.count())]
    
    """
    def catalog_items(self):
        book_list = self.catalog_list()
        return [book_list.nth(i).inner_text().strip() for i in range(book_list.count())]
    """

    def catalog_count(self):
        #return self.catalog_list.count()
        return self.page.locator('div.catalog > div.book').count()

    """
    # test new code
    def last_catalog_item_text(self):
        #books = self.catalog_list()
        books = self.page.locator("div.catalog > div.book")
        last_book = books.nth(self.catalog_count() - 1)
        #
        # Get only the direct text nodes of the book 
        title_author_text = last_book.locator("xpath=./text()").all_text_contents() 

        return  title_author_text[0].strip()

    """
    def last_catalog_item_text(self):
        count = self.catalog_count()
        return self.page.locator('div.catalog > div.book').nth(count - 1).inner_text().strip()

    def wait_until_loaded(self):
        self.page.wait_for_selector("div.catalog", timeout=5000)
    


## test function
"""
from playwright.sync_api import sync_playwright
url = 'https://tap-vt25-testverktyg.github.io/exam--reading-list/'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True, slow_mo=10000)
    page = browser.new_page()
    page.goto(url)
    
    homepage = CatalogPage(page)
    addbookpage = homepage.click_add_book_nav()

    browse = homepage.click_catalog_nav()
    list_book = browse.catalog_items() 

    last_item = CatalogPage.last_catalog_item_text()
    print(last_item)


    # close browser
    browser.close()

"""
