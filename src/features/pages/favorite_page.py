class FavoritePage:
    def __init__(self, page):
        self.page = page

    # ---------------------------
    # Helpers for locating stars
    # ---------------------------
    def _star_selector(self, title):
        """
        The data-testid has this format:
        star-<full title>
        """
        return f"[data-testid='star-{title}']"

    # ---------------------------
    # Actions
    # ---------------------------
    def mark_favorite(self, title):
        selector = self._star_selector(title)
        element = self.page.locator(selector)

        # Click only if NOT selected
        classes = element.get_attribute("class") or ""
        if "selected" not in classes:
            element.click()

    def unmark_favorite(self, title):
        selector = self._star_selector(title)
        element = self.page.locator(selector)

        # Click only if it IS selected
        classes = element.get_attribute("class") or ""
        if "selected" in classes:
            element.click()

    # ---------------------------
    # Navigation
    # ---------------------------
    def go_to_favorites(self):
        self.page.locator("[data-testid='favorites']").click()

    # ---------------------------
    # Validation
    # ---------------------------
    def count_favorites(self):
        self.go_to_favorites()
        return self.page.locator(".book").count()