from behave import given, when, then
from pages.catalog_page import CatalogPage

# 1. Start the app
@given("I open the app")
def open_app(context):
    context.page.goto(context.base_url)
    context.catalog = CatalogPage(context.page)

# 2. Verify that the katalog page is the default page
# US-1_AC1
@then('the "katalog" nav button should be disabled')
def catalog_selected(context):
    disabled = context.page.locator('button[data-testid="catalog"]').get_attribute('disabled')
    assert disabled is not None, "Catalog nav button should be disabled on load."

#3. The Katalog page contains the pre-loaded books
# US-1_AC2
@then("the catalog should contain {expected_count:d} books")
def check_count(context, expected_count):
    actual = context.catalog.catalog_count()
    assert actual == expected_count, f"Expected {expected_count} books but found {actual}"


@when("I navigate to the catalog")
def goto_catalog(context):
    context.catalog.click_catalog_nav()
