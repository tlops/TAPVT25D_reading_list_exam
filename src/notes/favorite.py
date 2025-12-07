from playwright.sync_api import sync_playwright

BASE_URL = 'https://tap-vt25-testverktyg.github.io/exam--reading-list/'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=10000)
    page = browser.new_page()
    page.goto(BASE_URL)

    ## My favorites books
    fav_1 = "star-Min katt är min chef"
    fav_2 = "star-Jag trodde det var tisdag"

    # to check items in favorite
    # page.locator("div.book div.star.selected").highlight()

    # Add favorite
    my_favorite = page.locator('[data-testid="star-Min katt är min chef"]')
    #my_favorite = page.locator('[data-testid=fav_1]')
    add_fav_btn = my_favorite.click()
    # [data-testid="star-Min katt är min chef"]

    ## click favorite
    favorite_btn = page.get_by_role('button', name='Mina böcker')
    favorite_btn.click()

    fave_list = page.locator("div.book div.star.selected").count()
    print(fave_list)

    # close browser
    browser.close()