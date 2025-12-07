Feature: Catalog view and content
	As a user, I want the katalog (catalog) page to be displayed by default
    when I open the application so that I can immediately see the list of
    books that are available in the library.

	Scenario: Catalog is selected on load
		Given I open the app
		Then the "katalog" nav button should be disabled
		And the catalog should contain 7 books
#

    Scenario Outline: Navigate Between Views
        Given I open the app

#	Scenario Outline: Catalog contains added books at the end
#		Given I open the app
#		When I add a new book with title "<title>" and author "<author>"
#		And I navigate to the catalog
#		Then the last book in the catalog should be '"<title>", <author>'
#		And the catalog should contain at least 8 books

#		Examples:
#		| title                         | author                   |
#		| 48 Laws of Power              | Robert Greene            |
#		| The richest Man in Babylon    | George Clason            |
#		| Things Fall Apart             | Chinua Achebe            |