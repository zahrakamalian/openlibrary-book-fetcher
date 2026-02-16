from flask import Flask, render_template, request
import requests
from typing import Any, List, Dict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_books() -> str:
    books: List[Dict[str, Any]] = []
    error: str | None = None
    query: str = ""

    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        if not query:
            error = "Please enter a genre or topic."
        else:
            try:
                limit: int = 500
                url: str = f"https://openlibrary.org/search.json?q={query}&limit={limit}"

                response: requests.Response = requests.get(url, timeout=30)
                response.raise_for_status()

                data: Dict[str, Any] = response.json()
                raw_books: List[Dict[str, Any]] = data.get("docs", [])

                for book in raw_books:
                    year: Any = book.get("first_publish_year")
                    if isinstance(year, int) and year > 2000:
                        filtered_book: Dict[str, Any] = {
                            "title": book.get("title", "unknown"),
                            "authors": ", ".join(book.get("author_name", ["unknown"])),
                            "first_publish_year": year,
                            "cover_id": book.get("cover_i"),
                        }
                        books.append(filtered_book)

                        if len(books) >= 50:
                            break

                if not books:
                    error = "No books found after 2000. Try another topic."

            except requests.exceptions.RequestException as e:
                error = f"Error connecting to API: {e}"
            except Exception as e:
                error = f"Unexpected error: {type(e).__name__} → {e}"

    return render_template('index.html', books=books, error=error, query=query)


if __name__ == '__main__':
    app.run(debug=True)