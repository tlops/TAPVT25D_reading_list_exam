from playwright.sync_api import sync_playwright

BASE_URL = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)
    context.page = context.browser.new_page()
    context.base_url = BASE_URL

    context.page.goto(context.base_url)
    context.page.default_timeout = 100

def before_scenario(context, scenario):
    # Reset navigation only, do NOT recreate browser
    # needed to pass adding multiple bookss
    context.page.goto(context.base_url)

def after_all(context):
    #context.page.close()
    context.browser.close()
    context.playwright.stop()
