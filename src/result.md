```bash
(myenv) tlops@ubuntu:~/python_NBI/src$ behave
USING RUNNER: behave.runner:Runner
Feature: Add book # features/add_book.feature:1
  As a user
  I want to add a new book using the 'Lägg till bok' form
  So it appears at the end of the catalog
  Scenario: Open add-book page and add a single book                      # features/add_book.feature:7
    Given I open the app                                                  # features/steps/katalog_steps.py:5 0.284s
    When I click the 'Lägg till bok' navigation button                    # features/steps/add_book_steps.py:11 0.362s
    Then I should see inputs for title and author                         # features/steps/add_book_steps.py:19 0.020s
    When I fill Titel "My New Book" and Författare "An Author"            # features/steps/add_book_steps.py:26 0.061s
    When I click the "Lägg till ny bok" button                            # features/steps/add_book_steps.py:36 0.055s
    Then I navigate to the katalog                                        # features/steps/add_book_steps.py:46 0.052s
    And the last book in the catalog should be '"My New Book", An Author' # features/steps/add_book_steps.py:58
    And the last book in the catalog should be '"My New Book", An Author' # features/steps/add_book_steps.py:58 0.019s       Scenario Outline: Add several books and verify each appears last
      """ When I click the 'Lägg till bok' navigation button
        Scenario Outline: Add several books and verify each appears last
          When I click the 'Lägg till bok' navigation buttonr>"
          Then I should see inputs for title and author
          When I fill Titel "<title>" and Författare "<author>"
          When I click the "Lägg till ny bok" button
          Then I navigate to the katalogog should be '"<title>", <author>'
          And I should be on the katalog page
          And the last book in the catalog should be '"<title>", <author>'
            | title                     | author         |
          Examples: in a Spaceship      | Luna G. Rider  |
            | title                     | author         |
            | Horse in a Spaceship      | Luna G. Rider  |
            | Zero Gravity Cooking      | Chef Orbit     |
            | My New Book               | An Author      |

      """

Feature: Manage favorite books # features/favorite.feature:1
  As a user
  I want to be able toadd and remove favorite books
  So that I can maintain a personal list of "Mina böcker"
  Feature: Manage favorite books  # features/favorite.feature:1

  @mark_favorites
  Scenario: Mark three books as favorite           # features/favorite.feature:10
    Given I am on the katalog page                 # features/steps/favorite_steps.py:5 0.048s
    When I mark the following books as favorite:   # features/steps/favorite_steps.py:20 0.205s
      | book_title                                          |
      | Hur man tappar bort sin TV-fjärr 10 gånger om dagen |
      | Kaffekokaren som visste för mycket                  |
      | Min katt är min chef                                |
    Then I should see 3 books in my favorites list # features/steps/favorite_steps.py:34 0.073s

  @unmark_favorites
  Scenario: Unmark two books so only one remains         # features/favorite.feature:19
    Given I am on the katalog page                       # features/steps/favorite_steps.py:5 0.049s
    Given I have marked the following books as favorite: # features/steps/favorite_steps.py:11 0.203s
      | book_title                                          |
      | Hur man tappar bort sin TV-fjärr 10 gånger om dagen |
      | Kaffekokaren som visste för mycket                  |
      | Min katt är min chef                                |
    When I unmark the following books from favorites:    # features/steps/favorite_steps.py:26 0.114s
      | book_title                         |
      | Kaffekokaren som visste för mycket |
      | Min katt är min chef               |
    Then I should see 1 books in my favorites list       # features/steps/favorite_steps.py:34 0.057s

Feature: Catalog view and content # features/katalog.feature:1
  As a user, I want the katalog (catalog) page to be displayed by default
  when I open the application so that I can immediately see the list of
  books that are available in the library.
  Scenario: Catalog is selected on load              # features/katalog.feature:6
    Given I open the app                             # features/steps/katalog_steps.py:5 0.033s
    Then the "katalog" nav button should be disabled # features/steps/katalog_steps.py:12 0.053s
    And the catalog should contain 7 books           # features/steps/katalog_steps.py:19 0.006s

3 features passed, 0 failed, 0 skipped
4 scenarios passed, 0 failed, 0 skipped
17 steps passed, 0 failed, 0 skipped
Took 0min 1.695s
```
