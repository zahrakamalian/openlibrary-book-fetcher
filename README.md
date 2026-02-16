# OpenLibrary Book Fetcher

A simple Python project that searches for books using the public OpenLibrary API, filters books first published after the year 2000, limits results to 50 books, and exports them to CSV.  
Now includes both **CLI (console) version** and **web version** (using Flask).

## Features

- Search books by genre/topic
- Filter books with `first_publish_year` > 2000
- Limit output to maximum 50 books
- Export results to CSV (title, authors, first_publish_year)
- Web interface (Flask) for browser-based search and display
- Dark/light mode auto-detection based on system preference
- Cover images from OpenLibrary (with fallback placeholder)

## Project Structure
openlibrary-book-fetcher/
├── app.py                  # Web version (Flask server)
├── get-books.py          # Console version (original script)
├── templates/
│   └── index.html          # HTML template for web version
├── requirements.txt        # Project dependencies
├── README.md               # This file
├── .gitignore              # Ignore venv, cache, output files
└── books_after_2000.csv    # Sample output (optional)

text## Requirements

- Python 3.8 or higher
- Dependencies (listed in `requirements.txt`):

```bash
pip install -r requirements.txt
```
or manually:

```Bash
pip install flask requests
```

How to Run
1. Console (CLI) Version
Bashpython get-books.py

Enter a genre or topic (e.g. fantasy, crime, science fiction)
Results saved to books_after_2000.csv

2. Web Version (Flask)
Bashpython app.py

Open your browser and go to: http://127.0.0.1:5000/
Enter a topic and search
Results displayed with book covers (if available)

Notes

In some regions (e.g. Iran), you may need a VPN due to connectivity restrictions to openlibrary.org
If fewer than 50 books are found after 2000, try more popular topics (fantasy, romance, young adult, thriller, etc.)
API used: https://openlibrary.org/dev/docs/api/search (no API key required)
Book covers are loaded from: https://covers.openlibrary.org/b/id/{cover_i}-M.jpg
If no cover is available, a simple placeholder is shown
Dark/Light mode automatically follows your system preference

