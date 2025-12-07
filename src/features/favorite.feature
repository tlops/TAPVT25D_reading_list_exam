Feature: Manage favorite books
  As a user
  I want to be able toadd and remove favorite books
  So that I can maintain a personal list of "Mina böcker"

  Background:
    Given I am on the katalog page

  @mark_favorites
  Scenario: Mark three books as favorite
    When I mark the following books as favorite:
      | book_title                                               |
      | Hur man tappar bort sin TV-fjärr 10 gånger om dagen     |
      | Kaffekokaren som visste för mycket                      |
      | Min katt är min chef                                    |
    Then I should see 3 books in my favorites list

  @unmark_favorites
  Scenario: Unmark two books so only one remains
    Given I have marked the following books as favorite:
      | book_title                                               |
      | Hur man tappar bort sin TV-fjärr 10 gånger om dagen     |
      | Kaffekokaren som visste för mycket                      |
      | Min katt är min chef                                    |
    When I unmark the following books from favorites:
      | book_title                           |
      | Kaffekokaren som visste för mycket  |
      | Min katt är min chef                |
    Then I should see 1 book in my favorites list
