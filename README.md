# OpenLibrary Book Fetcher

A simple Python script that searches for books using the public OpenLibrary API, filters books first published after the year 2000, keeps up to 50 results, and saves them to a CSV file.

## Features
- User selects genre/topic via input prompt
- Filters books based on `first_publish_year` > 2000
- Limits output to maximum 50 books (project requirement)
- Exports results to CSV with columns: title, authors, first_publish_year

## Requirements
- Python 3.8 or higher
- `requests` library  
  ```bash
  pip install requests


How to Run

1. Clone or download the repository
2. Open a terminal in the project folder
3. Run the script:

Bash

```
python get-books.py
```

4. Enter your desired genre or topic (e.g. fantasy, crime, science fiction)

Output
* A file named books_after_2000.csv will be created in the same folder
* Columns: title, authors, first_publish_year

Notes
* In some regions (e.g. Iran), you may need a VPN due to connectivity restrictions to openlibrary.org
* If fewer than 50 books are found, try a more popular topic (e.g. fantasy, romance, crime)
* API used: https://openlibrary.org/dev/docs/api/search (no API key required)
* To see available topics, check: https://openlibrary.org/subjects

Project Details

* Created for Python project assignment
* Last updated: February 2025

Enjoy exploring recent books!