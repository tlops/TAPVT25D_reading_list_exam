from behave import given, when, then
from features.pages.favorite_page import FavoritePage

# US-4_AC1 
@given("I am on the katalog page")
def step_impl(context):
    context.page.goto(context.base_url)
    context.favorite_page = FavoritePage(context.page)

# US-3_AC2
@given("I have marked the following books as favorite:")
def step_impl(context):
    context.favorite_page = FavoritePage(context.page)
    for row in context.table:
        title = row["book_title"]
        context.favorite_page.mark_favorite(title)

# Adding books to "mina böcker" by favorite
# US-3_AC1
@when("I mark the following books as favorite:")
def step_impl(context):
    for row in context.table:
        title = row["book_title"]
        context.favorite_page.mark_favorite(title)

@when("I unmark the following books from favorites:")
def step_impl(context):
    for row in context.table:
        title = row["book_title"]
        context.favorite_page.unmark_favorite(title)

# Navigate to "Mina böcker"
# US-4_AC1 US-3_AC3
@then("I should see {count:d} books in my favorites list")
@then("I should see {count:d} book in my favorites list")
def step_impl(context, count):
    actual = context.favorite_page.count_favorites()
    assert actual == count, f"Expected {count} favorites but got {actual}"
