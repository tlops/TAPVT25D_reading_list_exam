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
    
"""
  Scenario Outline: Add several books and verify each appears last
    When I click the 'Lägg till bok' navigation button
    Then I should see inputs for title and author
    When I fill Titel "<title>" and Författare "<author>"
    When I click the "Lägg till ny bok" button
    Then I navigate to the katalog
    And I should be on the katalog page
    And the last book in the catalog should be '"<title>", <author>'

    Examples:
      | title                     | author         |
      | Horse in a Spaceship      | Luna G. Rider  |
      | Zero Gravity Cooking      | Chef Orbit     |
      | My New Book               | An Author      |

 """
