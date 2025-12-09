Feature: Add book
  As a user
  I want to add a new book using the 'Lägg till bok' form
  So it appears at the end of the catalog
  

  Scenario: Open add-book page and add a single book
    Given I open the app
    When I click the 'Lägg till bok' navigation button
    Then I should see inputs for title and author
    When I fill Titel "My New Book" and Författare "An Author"
    When I click the "Lägg till ny bok" button
    Then I navigate to the katalog
    And the last book in the catalog should be '"My New Book", An Author'

  Scenario Outline: Open add-book page and add multiple books
    Given I open the app
    When I click the 'Lägg till bok' navigation button
    Then I should see inputs for title and author
    When I fill Titel "<title>" and Författare "<author>"
    And I click the "Lägg till ny bok" button 
    And I navigate to the katalog
    Then the last book in the catalog should be '"<title>", <author>'
    And the catalog should contain at least 8 books 
    #And the catalog should contain at least 10 books 

    Examples:
	| title                       | author                   |
        | 48 Laws of Power            | Robert Greene            |
	| The richest Man in Babylon  | George Clason            |
	| Things Fall Apart           | Chinua Achebe            |
