from playwright.sync_api import Page
base_url = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = base_url

    #ef goto(self, path="/"):
    def goto(self):
        self.page.goto(self.base_url)
