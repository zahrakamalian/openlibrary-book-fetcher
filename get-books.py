import requests
import csv

search_query = input(
    "Enter genre or topic (e.g. crime, fantasy, science fiction): ").strip()
if not search_query:
    search_query = "crime"

limit = 500
url = f"https://openlibrary.org/search.json?q={search_query}&limit={limit}"

print(f"searching for: {search_query}...")

filtered_books = []

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()
    books = data.get("docs", [])

    for book in books:
        year = book.get("first_publish_year")
        if isinstance(year, int) and year > 2000:
            filtered_book = {
                "title": book.get("title", "unknown"),
                "authors": ", ".join(book.get("author_name", ["unknown"])),
                "first_publish_year": year,
                "edition_count": book.get("edition_count", "unknown"),
                "cover_i": book.get("cover_i"),
                "key": book.get("key", "unknown")
            }
            filtered_books.append(filtered_book)

            if len(filtered_books) >= 50:
                break

    print(f"past 2000 books num: {len(filtered_books)}")

    if not filtered_books:
        print("no book found! try a different topic or check internet")

    if filtered_books:
        csv_filename = "books_after_2000.csv"
        fieldnames = ["title", "authors", "first_publish_year",
                      "edition_count", "cover_i", "key"]

        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_books)

        print(f"csv file saved!: {csv_filename}")
        print("first 3 books:")
        for book in filtered_books[:3]:
            print(book)

except requests.exceptions.RequestException as e:
    print(f"error connecting API: {e}")
except Exception as e:
    print(f"unexpected error: {type(e).__name__} → {e}")
