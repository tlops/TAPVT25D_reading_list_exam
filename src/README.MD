# Reading List – Automated Tests (Playwright + behave + pytest)

This project contains BDD-style UI tests for the Reading List application:

https://tap-vt25-testverktyg.github.io/exam--reading-list/


##  What the project contains
- Python test framework using **Playwright**, **behave**, **pytest**
- User stories (`STORIES.md`)
- Feature files (`src/features/*.feature`)
- Page Object Model (`src/features/pages/*.py`)
- Step definitions (`src/features/steps/*.py`)
- Playwright environment management (`src/features/environment.py`)


---

## 📌 User stories
See **STORIES.md** for complete user stories.

Summary:
- View catalog on load  
- Add a new book  
- Favorite and unfavorite books  
- View favorites  
- Navigate

---

## 📦 Requirements
- Python 3.9+
- pip
- pip install pytest-playwright behave
---

## How to set up
My environment was linux Ubuntu 22

```bash
git clone git@github.com:tlops/TAPVT25D_reading_list_exam.git
cd TAPVT25D_reading_list_exam/src

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install     # install browsers
```

## ✔️ What I tested
1. **Catalog page loads by default**  
   - “Katalog” button is disabled  
   - All pre-seeded books are displayed  

2. **Add new book**  
   - Navigate to Add Book page  
   - Fill in title + author  
   - Submit  
   - Verify the new book appears last in the catalog  

3. **Favorites functionality**  
   - Click heart icon toggles favorite  
   - Verify favorite appears in “Mina böcker”  
   - Clicking again removes it  

4. **Navigate between pages**
    - Tested implicitly as part of other tests.

5. **Scenario Outline**  
   - Tests adding multiple books from a table  (Not passed)

## 📝 Notes
- The webapp does **not persist data across refresh** → tests do NOT require persistence.
- Tests rely heavily on `data-testid` selectors as it was unique. 

