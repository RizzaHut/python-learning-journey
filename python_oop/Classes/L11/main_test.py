import pytest
from main import Book, Library

run_cases = [
    (
        "Jane's Library",
        ["The Trial"],
        ["Franz Kafka"],
        Book("The Trial", "Franz Kafka"),
        "Kafka",
        [],
    ),
    (
        "John's Library",
        ["The Catcher in the Rye", "To Kill a Mockingbird", "1984"],
        ["J.D. Salinger", "Harper Lee", "George Orwell"],
        Book("1984", "George Orwell"),
        "mock",
        ["To Kill a Mockingbird"],
    ),
]

submit_cases = [
    pytest.param(
        "Lane's Library",
        [
            "The Great Gatsby",
            "Pride and Prejudice",
            "The Lord of the Rings",
            "Great Expectations",
            "To Kill a Mockingbird",
        ],
        [
            "F. Scott Fitzgerald",
            "Jane Austen",
            "J.R.R. Tolkien",
            "Charles Dickens",
            "Harper Lee",
        ],
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        "great",
        ["Great Expectations"],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "Blane's Library",
        ["The Hobbit"],
        ["J.R.R. Tolkien"],
        Book("The Hobbit", "George R.R. Martin"),
        "tolkien",
        ["The Hobbit"],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    (
        "library_name",
        "book_titles",
        "book_authors",
        "book_to_remove",
        "search_query",
        "expected_search_results",
    ),
    run_cases + submit_cases,
)
def test_library(
    library_name,
    book_titles,
    book_authors,
    book_to_remove,
    search_query,
    expected_search_results,
):
    print("\n---------------------------------")
    print(f"Testing Library: {library_name}")

    library = Library(library_name)
    for title, author in zip(book_titles, book_authors):
        library.add_book(Book(title, author))
        print(f"Adding book {title} by {author}")

    print(f"Removing book {book_to_remove.title} by {book_to_remove.author}")
    library.remove_book(book_to_remove)

    print(f"Searching for '{search_query}'")
    search_results = library.search_books(search_query)
    results_titles = [book.title for book in search_results]
    print(f"Expected: {expected_search_results}")
    print(f"Actual: {results_titles}")
    assert results_titles == expected_search_results
