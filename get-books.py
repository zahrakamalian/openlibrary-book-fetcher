import requests
import csv


# Get user input for search topics
search_query = input(
    "Enter genre or topic (e.g. programming, fantasy, science fiction): ").strip() or "programming"

# Higher limit to increase chance of getting 50+ after filtering
limit = 500
# Build API URL
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
            }
            filtered_books.append(filtered_book)

            if len(filtered_books) >= 50:
                # Stop after reaching project requirement of 50 books
                break

    print(f"Books after 2000: {len(filtered_books)}")

    if not filtered_books:
        print("No books found! Try another topic or check connection.")

    if filtered_books:
        csv_filename = "books_after_2000.csv"
        fieldnames = ["title", "authors", "first_publish_year"]

        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_books)

        print(f"ُSaved to: {csv_filename}")

except requests.exceptions.RequestException as e:
    print(f"error connecting API: {e}")
except Exception as e:
    print(f"unexpected error: {type(e).__name__} → {e}")
