
# Background
"Läslistan" är en webbsida där man kan välja ut sina favoriter från en katalog 
med böcker, eller lägga till nya. Beställaren är en organisation som vill öka 
barns och ungas läsande. Nuvarande version har begränsad funktionalitet. 
På sikt vill man utöka webbsidan med funktioner för att dela sina listor, 
skapa quiz och diskutera böcker med varandra. Därför är det viktigt att det 
finns tester för all grundläggande funktionalitet. 

Detta är din uppgift!

# User stories for the Reading List web app
## US-1: View catalog

As a user,
I want to land on the "Katalog" page when I open the app,
So that I can immediately see the list of books available.

**Acceptance criteria:**

**US-1_AC1.** The catalog button is disabled on load to indicate it is selected.

**US-1_AC2.** The catalog lists the pre-loaded books (see list below).

## US-2: Add a book

As a user,
I want to click "Lägg till bok", fill in title and author, and submit,
So that the new book appears at the end of the catalog.

**Acceptance criteria:**

**US-2_AC1.** Clicking the "Lägg till bok" button shows the add-book form.

**US-2_AC2.** Input the "Titel" and "Författare".

**US-2_AC3.** Submitting by clicking the "Lägg till ny bok" button.

**US-2_AC4.** The new book is added to the end of "katalog" page


## US-3: Manage favorite

As a user,
  I want to be able to add and remove favorite books
  So that I can maintain a personal list of "Mina böcker".

**Acceptance criteria:**

**US-3_AC1.** Click heart button by the book, adds the book to "Mina böcker".

**US-3_AC2.** Clicking an already clicked heart removes the book from "Mina böcker".

**US-3_AC3.** "Mina böcker" should contain only my favorites.

## US-4: Navigation
As a user,
I want to be able to navigate through the different pages of the app

**US-4_AC1.** Navigate to "Lägg til bok".

**US-4_AC2.** Navigate to "Mina böcker".


## Pre-Loaded books
These books must appear on load:

- "Hur man tappar bort sin TV-fjärr 10 gånger om dagen", Bertil Flimmer  
- "Kaffekokaren som visste för mycket", Saga Espresson  
- "Min katt är min chef", Kattis Jamsson  
- "100 sätt att undvika måndagar", Göran Snooze  
- "Gräv där du står – och hitta en pizzameny", Maja Skruv  
- "Jag trodde det var tisdag", Kim Vilsen  
- "Att prata med växter – och vad de egentligen tycker om dig", Flora Tistel  


